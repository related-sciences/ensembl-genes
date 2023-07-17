import logging

import typer

from ensembl_genes.ensembl_genes import (
    Ensembl_Gene_Catalog_Writer,
    Ensembl_Gene_Queries,
)
from ensembl_genes.releases import check_ensembl_release

cli = typer.Typer()


class Commands:
    @staticmethod
    @cli.command(name="datasets")
    def export_datasets(species: str = "human", release: str = "latest") -> None:
        """Export datasets to output directory."""
        ensgc = Ensembl_Gene_Catalog_Writer(species=species, release=release)
        logging.info(
            f"exporting ensembl genes to {ensgc.output_directory}: version {ensgc.release}"
        )
        logging.info(f"connection_url: {ensgc.connection_url}")
        ensgc.export_datasets()

    @staticmethod
    @cli.command(name="notebooks")
    def export_notebooks(species: str = "human", release: str = "latest") -> None:
        """Execute notebooks using papermill and save results in output directory."""
        logging.info("Executing notebooks with papermill")
        ensgc = Ensembl_Gene_Catalog_Writer(species=species, release=release)
        ensgc.export_notebooks()

    @classmethod
    @cli.command(name="all")
    def export_all(cls, species: str = "human", release: str = "latest") -> None:
        """Export datasets and then notebooks."""
        cls.export_datasets(species=species, release=release)
        cls.export_notebooks(species=species, release=release)

    @staticmethod
    @cli.command(name="ensembl_release")
    def get_ensembl_release(release: str = "latest") -> None:
        """
        Check that ensembl release is properly formatted and resolve 'latest'.
        """
        release = check_ensembl_release(release=release)
        print(release)

    @staticmethod
    @cli.command(name="ensembl_database")
    def get_ensembl_database(species: str = "human", release: str = "latest") -> None:
        """
        Return ensembl core database string for a species & release.
        See <http://ftp.ensembl.org/pub/current_mysql/> for a list of current ensembl databases.
        """
        ensgc = Ensembl_Gene_Queries(species=species, release=release)
        print(ensgc.database)

    @classmethod
    def command(cls) -> None:
        """
        Run like `poetry run ensembl_genes`
        """
        logging.basicConfig()
        logging.getLogger().setLevel(logging.INFO)
        cli()
