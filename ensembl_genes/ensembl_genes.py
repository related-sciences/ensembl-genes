import logging
import pathlib
import subprocess
from dataclasses import dataclass, field
from enum import Enum
from functools import cached_property
from typing import Dict, List, Set, Tuple, Union

import pandas as pd

from ensembl_genes.releases import check_ensembl_release

from .species import Species, get_species, human


class Ensembl_Gene_Queries:

    _column_dtypes: Dict[str, str] = {
        "alt_allele_is_representative": "bool",
        "primary_assembly": "bool",
    }
    """
    pandas.read_sql does not always preserve column types (e.g. converts bool columns to int).
    Convert columns listed to the specified type.
    """

    def __init__(self, species: Union[str, Species] = "human", release: str = "latest"):
        """Example release '104'."""
        self.species = get_species(species)
        self.release = check_ensembl_release(release)
        self.database = (
            f"{self.species.name}_core_{self.release}_{self.species.reference_genome}"
        )

    @property
    def connection_url(self) -> str:
        """
        Ensembl public MySQL Servers information at
        https://uswest.ensembl.org/info/data/mysql.html
        """
        import sqlalchemy

        url = sqlalchemy.engine.url.URL.create(
            drivername="mysql+mysqlconnector",
            username="anonymous",
            host="ensembldb.ensembl.org",  # From Ensembl 48 onwards only
            # host="useastdb.ensembl.org",  # Current and previous Ensembl version only
            port=3306,
            database=self.database,
        )
        return str(url)

    @staticmethod
    def get_query(name: str) -> str:
        path = pathlib.Path(__file__).parent.joinpath(f"queries/{name}.sql")
        return path.read_text()

    def run_query(self, name: str) -> pd.DataFrame:
        query = self.get_query(name)
        df = pd.read_sql_query(sql=query, con=self.connection_url)
        for column, dtype in self._column_dtypes.items():
            if column in df:
                df[column] = df[column].astype(dtype)
        logging.info(
            f"Ran {name!r} query returning {len(df):,} rows. Head:\n\n{df.head(4)}"
        )
        return df

    @cached_property
    def gene_df(self) -> pd.DataFrame:
        gene_df = (
            self.run_query("genes")
            # Add Locus Reference Genomic (LRG) gene identifiers for genes that have them.
            # Refs internal Related Sciences issue 289.
            .merge(self.xref_lrg_df, how="left")
        )
        # add MHC category
        gene_df["mhc"] = [
            self.species.get_mhc_category(x) for x in gene_df.itertuples()
        ]
        # add ensembl_representative_gene_id column
        gene_repr_df = gene_df.merge(
            self.alt_allele_df[["ensembl_gene_id", "ensembl_representative_gene_id"]],
            how="left",
        )
        gene_repr_df.ensembl_representative_gene_id = (
            gene_repr_df.ensembl_representative_gene_id.fillna(
                gene_repr_df.ensembl_gene_id
            )
        )
        self._check_gene_df(gene_repr_df)
        return gene_repr_df

    def _check_gene_df(self, gene_df: pd.DataFrame) -> None:
        # ensure genes are distinct by their ensembl_gene_id
        gene_duplicate_df = gene_df[gene_df.ensembl_gene_id.duplicated(keep=False)]
        assert gene_duplicate_df.empty
        # check all ensembl IDs match the expected pattern
        # ensures LRG gene IDs are filtered (e.g. LRG_47)
        invalid_id_df = gene_df[
            ~gene_df.ensembl_gene_id.str.fullmatch(self.species.ensembl_gene_pattern)
        ]
        assert invalid_id_df.empty
        # ensure all genes have a symbol
        # https://github.com/cogent3/ensembldb3/issues/7
        gene_symbol_missing_df = gene_df[gene_df.gene_symbol.isna()]
        assert gene_symbol_missing_df.empty
        # check chromosome values (scaffolds can cause problems)
        # Refs internal Related Sciences issue 606#issuecomment-929609041.
        bad_chromosome_df = gene_df.dropna(subset=["chromosome"])
        bad_chromosome_df = bad_chromosome_df[
            ~bad_chromosome_df.chromosome.isin(self.species.chromosomes)
        ]
        assert bad_chromosome_df.empty

    @cached_property
    def alt_allele_df(self) -> pd.DataFrame:
        alt_allele_df = self.run_query("gene_alt_alleles")
        expected_cols = [
            *alt_allele_df.columns,
            "ensembl_representative_gene_id",
            "is_representative_gene",
            "representative_gene_method",
        ]
        alt_allele_df = (
            alt_allele_df.groupby("alt_allele_group_id").apply(
                self._alt_allele_add_representative
            )
            # Force expected output columns, since groupby-apply does not add columns
            # from _alt_allele_add_representative when alt_allele_df is empty.
            .reindex(columns=expected_cols)
            # ensembl_gene_id can be duplicated due to multiple alt_allele_attrib values
            .drop_duplicates("ensembl_gene_id", keep="first")
        )
        self._check_alt_allele_df(alt_allele_df)
        return alt_allele_df

    @staticmethod
    def _check_alt_allele_df(alt_allele_df: pd.DataFrame) -> None:
        dup_df = alt_allele_df[alt_allele_df.ensembl_gene_id.duplicated(keep=False)]
        assert dup_df.empty

    @staticmethod
    def _alt_allele_get_representative(df: pd.DataFrame) -> "Tuple[str, str]":
        """
        For a subset of the alt_allele_df corresponding to a single `alt_allele_group_id`,
        return a (ensembl_representative_gene_id, representative_gene_method) tuple,
        where `ensembl_representative_gene_id` is the selected representative gene from this group
        and `representative_gene_method` is the method by which it was selected.
        The following methods are used in this order of precedence:

        1. alt_allele_is_representative: the ensembl alt_allele table declares a single gene as IS_REPRESENTATIVE.
        2. primary_assembly: a single gene is on the primary assembly.
        3. first_added: the gene first added to the Ensembl database.
        """
        representatives = list(
            df.loc[df.alt_allele_is_representative.astype("bool"), "ensembl_gene_id"]
        )
        if len(representatives) == 1:
            return representatives[0], "alt_allele_is_representative"
        if len(representatives) > 1:
            raise ValueError(
                "expected at most 1 IS_REPRESENTATIVE gene per alt_allele_group"
            )
        representatives = list(
            df.loc[df.primary_assembly.astype("bool"), "ensembl_gene_id"]
        )
        if len(representatives) == 1:
            return representatives[0], "primary_assembly"
        if len(representatives) > 1:
            raise ValueError(
                "expected at most 1 primary assembly gene per alt_allele_group"
            )
        return (
            df.sort_values(
                ["ensembl_created_date", "ensembl_gene_id"]
            ).ensembl_gene_id.iloc[0],
            "first_added",
        )

    @staticmethod
    def _alt_allele_add_representative(df: pd.DataFrame) -> pd.DataFrame:
        """
        Apply to alt_allele_df grouped by `alt_allele_group_id` to add columns:
        `ensembl_representative_gene_id`, `is_representative_gene`, `representative_gene_method`.
        """
        representative, method = Ensembl_Gene_Queries._alt_allele_get_representative(df)
        df["ensembl_representative_gene_id"] = representative
        df["is_representative_gene"] = (
            df.ensembl_gene_id == df.ensembl_representative_gene_id
        )
        df["representative_gene_method"] = method
        # the ordering of alt_allele_df should always place the representative gene first.
        # at some point we might be able to move all logic to SQL
        assert df["is_representative_gene"].iloc[0]
        return df

    @cached_property
    def old_to_new_df(self) -> pd.DataFrame:
        return self.run_query("gene_events")

    @cached_property
    def old_to_news(self) -> Dict[str, str]:
        old_to_news = {}
        groups = self.old_to_new_df.groupby("old_ensembl_gene_id").new_ensembl_gene_id
        for old, news in groups:
            for new in news:
                assert isinstance(new, str)
            old_to_news[old] = news
        return old_to_news

    def _update_ensembl_gene(self, old_id: str) -> Set[str]:
        """
        Recursive function to return newest identifiers for an old identifier.
        A newest identifier is not necessarily current, but does have no replacement in gene_history.
        """
        if old_id not in self.old_to_news:
            return {old_id}
        new_ids = set()
        for id_ in self.old_to_news[old_id]:
            new_ids |= self._update_ensembl_gene(id_)
        return new_ids

    @cached_property
    def old_to_newest_df(self) -> pd.DataFrame:
        rows = list()
        for old_id in sorted(self.old_to_new_df.old_ensembl_gene_id.unique()):
            for new_id in sorted(self._update_ensembl_gene(old_id)):
                rows.append(
                    dict(old_ensembl_gene_id=old_id, newest_ensembl_gene_id=new_id)
                )
        old_to_newest_df = pd.DataFrame(rows)
        old_to_newest_df["is_current"] = old_to_newest_df.newest_ensembl_gene_id.isin(
            self.gene_df.ensembl_gene_id
        )
        return old_to_newest_df

    @cached_property
    def update_df(self) -> pd.DataFrame:
        """
        The omni-updater dataset is designed to convert ensembl gene IDs from input data to the current, representative ensembl_gene_ids for this ensembl release.
        It assumes:

        - users want to update outdated genes with their replacements
        - users want a dataset of representative genes only, and want to convert alternative alleles to representative genes

        An inner join of a dataset with `update_df` on `input_ensembl_gene_id` will do the following:

        - produce output ensembl_gene_ids that are current and representatives
        - update outdated genes with their current identifiers. Outdated genes with no current replacement will be removed by the inner join.
        - update alternative gene alleles with their representatives
        - genes that are already representative and current will map to themselves
        """
        update_alt_df = (
            self.gene_df.assign(input_current=True)
            .eval(
                "input_representative = ensembl_gene_id == ensembl_representative_gene_id"
            )
            .rename(
                columns={
                    "ensembl_gene_id": "input_ensembl_gene_id",
                    "ensembl_representative_gene_id": "ensembl_gene_id",
                }
            )[
                [
                    "input_ensembl_gene_id",
                    "ensembl_gene_id",
                    "input_current",
                    "input_representative",
                ]
            ]
        )
        update_old_df = (
            self.old_to_newest_df.merge(
                self.gene_df[["ensembl_gene_id", "ensembl_representative_gene_id"]],
                left_on="newest_ensembl_gene_id",
                right_on="ensembl_gene_id",
            )
            .assign(input_current=False)
            .eval(
                "input_representative = newest_ensembl_gene_id == ensembl_representative_gene_id"
            )
            .drop(columns="ensembl_gene_id")
            .rename(
                columns={
                    "old_ensembl_gene_id": "input_ensembl_gene_id",
                    "ensembl_representative_gene_id": "ensembl_gene_id",
                }
            )
            .drop_duplicates(["input_ensembl_gene_id", "ensembl_gene_id"])[
                [
                    "input_ensembl_gene_id",
                    "ensembl_gene_id",
                    "input_current",
                    "input_representative",
                ]
            ]
        )
        update_df = (
            pd.concat([update_alt_df, update_old_df])
            .drop_duplicates()
            .sort_values(["input_ensembl_gene_id", "ensembl_gene_id"])
        )
        assert update_df[
            update_df[["input_ensembl_gene_id", "ensembl_gene_id"]].duplicated(
                keep=False
            )
        ].empty
        update_df["input_maps_to_n_genes"] = update_df.input_ensembl_gene_id.map(
            update_df.input_ensembl_gene_id.value_counts()
        )
        update_df["n_inputs_map_to_gene"] = update_df.ensembl_gene_id.map(
            update_df.ensembl_gene_id.value_counts()
        )
        return update_df

    @cached_property
    def xref_df(self) -> pd.DataFrame:
        return self.run_query("gene_xrefs")

    @cached_property
    def xref_ncbigene_df(self) -> pd.DataFrame:
        return (
            self.xref_df.query("xref_source == 'EntrezGene'")
            .merge(
                self.gene_df[
                    ["ensembl_gene_id", "ensembl_representative_gene_id", "seq_region"]
                ]
            )
            .rename(columns={"xref_accession": "ncbigene_id"})[
                ["ensembl_representative_gene_id", "ncbigene_id"]
            ]
            .drop_duplicates(["ensembl_representative_gene_id", "ncbigene_id"])
            .sort_values(["ensembl_representative_gene_id", "ncbigene_id"])
        )

    @cached_property
    def xref_lrg_df(self) -> pd.DataFrame:
        """
        Mappings between ensembl and Locus Reference Genomic (LRG) gene identifiers.
        Refs internal Related Sciences issue 289.
        """
        xref_lrg_df = self.xref_df.query("xref_source == 'ENS_LRG_gene'").rename(
            columns={"xref_accession": "lrg_gene_id"}
        )[["ensembl_gene_id", "lrg_gene_id"]]
        self._check_xref_lrg_df(xref_lrg_df)
        return xref_lrg_df

    @staticmethod
    def _check_xref_lrg_df(xref_lrg_df: pd.DataFrame) -> None:
        # ensure ensembl genes map to at most one LRG gene
        dup_df = xref_lrg_df[xref_lrg_df.ensembl_gene_id.duplicated(keep=False)]
        assert dup_df.empty

    @cached_property
    def xref_go_df(self) -> pd.DataFrame:
        xref_go_df = self.run_query("gene_xrefs_go").merge(
            self.gene_df[["ensembl_gene_id", "ensembl_representative_gene_id"]]
        )
        self._check_xref_go_df(xref_go_df)
        return xref_go_df

    def _check_xref_go_df(self, xref_go_df: pd.DataFrame) -> None:
        # check distinct on ensembl_gene_id-go_id pair
        dup_df = xref_go_df[
            xref_go_df.duplicated(subset=["ensembl_gene_id", "go_id"], keep=False)
        ]
        assert dup_df.empty
        if self.species == human:
            # spot check a single GO annotation for TYK2 and protein tyrosine kinase activity
            # Refs internal Related Sciences pull request 322#issuecomment-756789203.
            check_df = xref_go_df.query(
                "ensembl_gene_id=='ENSG00000105397' and go_id=='GO:0004713'"
            )
            assert len(check_df) == 1


class ExportFormat(str, Enum):
    parquet = "parquet"
    tsv = "tsv"
    excel = "excel"
    json = "json"


@dataclass
class DatasetExport:
    name: str
    query_fxn: str
    description: str
    export_formats: List[ExportFormat] = field(
        default_factory=lambda: [ExportFormat.parquet, ExportFormat.tsv]
    )


class Ensembl_Gene_Catalog_Writer(Ensembl_Gene_Queries):

    exports: List[DatasetExport] = [
        DatasetExport(
            name="genes",
            query_fxn="gene_df",
            description=(
                "Primary table of ensembl genes with IDs, symbols, and genomic location information. "
                "Most users will want to filter this dataset to representative genes only, "
                "via the `is_representative_gene` column."
            ),
            export_formats=list(ExportFormat),
        ),
        DatasetExport(
            name="alt_alleles",
            query_fxn="alt_allele_df",
            description=(
                "This is an intermediate table that groups genes if they are alternate alleles of eachother. "
                "A representative gene is selected from each group."
            ),
        ),
        DatasetExport(
            name="old_to_newest",
            query_fxn="old_to_newest_df",
            description=(
                "This table maps outdated gene symbols to their newest gene symbol, "
                "traversing multiple levels of replacement if necessary. "
                "When `is_current` is False, then the newest replacement is not a current gene."
            ),
        ),
        DatasetExport(
            name="updates",
            query_fxn="update_df",
            description=(
                "This dataset updates ensembl genes to current, representative ensembl genes. "
                "We refer to it as the 'omni-updater'. "
                "When ingesting external datasets that use Ensembl gene IDs, we recommend joining with this table. "
                "Current, representative genes map to themselves."
            ),
            export_formats=list(ExportFormat),
        ),
        DatasetExport(
            name="xrefs",
            query_fxn="xref_df",
            description=(
                "This dataset contains cross-references (xrefs) from Ensembl genes to various external gene resources."
            ),
            export_formats=list(ExportFormat),
        ),
        DatasetExport(
            name="xref_ncbigene",
            query_fxn="xref_ncbigene_df",
            description=(
                "This dataset contains cross-references (xrefs) from Ensembl genes to NCBI (Entrez) genes."
            ),
            export_formats=list(ExportFormat),
        ),
        DatasetExport(
            name="xref_go",
            query_fxn="xref_go_df",
            description=(
                "This dataset contains cross-references (xrefs) from Ensembl genes to Gene Ontology terms, "
                "as asserted by Gene Ontology annotations."
            ),
        ),
    ]
    ipynb_exports = [
        "ensembl_genes_output.ipynb",
        "ensembl_genes_eda.ipynb",
    ]

    def __init__(self, species: Union[str, Species], release: str):
        release = str(release)  # protect against fire
        super().__init__(species=species, release=release)
        directory = pathlib.Path("output", self.release)
        directory.mkdir(exist_ok=True, parents=True)
        self.output_directory = directory

    def export_datasets(self) -> None:
        for export in self.exports:
            logging.info(f"exporting {export.name} data")
            self.write_dataset(export)

    def write_dataset(self, export: DatasetExport) -> None:
        df = getattr(self, export.query_fxn)
        assert isinstance(df, pd.DataFrame)
        gz_compression = {"method": "gzip", "mtime": 0}
        if ExportFormat.parquet in export.export_formats:
            path = self.output_directory.joinpath(f"{export.name}.snappy.parquet")
            df.to_parquet(path, compression="snappy", index=False)
        if ExportFormat.tsv in export.export_formats:
            path = self.output_directory.joinpath(f"{export.name}.tsv.gz")
            df.to_csv(path, index=False, sep="\t", compression=gz_compression)
        if ExportFormat.json in export.export_formats:
            path = self.output_directory.joinpath(f"{export.name}.json.gz")
            df.to_json(path, orient="records", compression=gz_compression, indent=2)
        if ExportFormat.excel in export.export_formats:
            path = self.output_directory.joinpath(f"{export.name}.xlsx")
            df.to_excel(
                path,
                sheet_name=export.name,
                freeze_panes=(1, 0),
                float_format="%.4g",
                engine="openpyxl",
                index=False,
            )

    def export_notebooks(self) -> None:
        for ipynb_export in self.ipynb_exports:
            self.export_notebook(notebook=ipynb_export)
        # export ensembl_genes_output.ipynb to README.md
        output_ipynb = self.output_directory.joinpath("ensembl_genes_output.ipynb")
        command = [
            "jupyter",
            "nbconvert",
            output_ipynb.as_posix(),
            "--to=markdown",
            # outputs by default to the directory of each notebook.
            "--output=README.md",
            # exclude input/code cells
            "--no-input",
        ]
        subprocess.check_call(command)
        output_ipynb.unlink()

    def export_notebook(self, notebook: str) -> None:
        import papermill

        logging.info(f"Executing {notebook} with papermill")
        papermill.execute_notebook(
            input_path=f"ensembl_genes/notebooks/{notebook}",
            output_path=self.output_directory.joinpath(notebook),
            parameters=dict(release=self.release),
        )


class Commands:
    @staticmethod
    def export_datasets(species: str = "human", release: str = "latest") -> None:
        """Export datasets to output directory."""
        ensgc = Ensembl_Gene_Catalog_Writer(species=species, release=release)
        logging.info(
            f"exporting ensembl genes to {ensgc.output_directory}: version {ensgc.release}"
        )
        logging.info(f"connection_url: {ensgc.connection_url}")
        ensgc.export_datasets()

    @staticmethod
    def export_notebooks(species: str = "human", release: str = "latest") -> None:
        """Execute notebooks using papermill and save results in output directory."""
        logging.info("Executing notebooks with papermill")
        ensgc = Ensembl_Gene_Catalog_Writer(species=species, release=release)
        ensgc.export_notebooks()

    @classmethod
    def export_all(cls, species: str = "human", release: str = "latest") -> None:
        """Export datasets and then notebooks."""
        cls.export_datasets(species=species, release=release)
        cls.export_notebooks(species=species, release=release)

    @classmethod
    def command(cls) -> None:
        """
        Run like `poetry run ensembl_genes`
        """
        import fire

        logging.basicConfig()
        logging.getLogger().setLevel(logging.INFO)
        commands = {
            "datasets": cls.export_datasets,
            "notebooks": cls.export_notebooks,
            "all": cls.export_all,
            "ensembl_release": check_ensembl_release,
        }
        fire.Fire(commands)
