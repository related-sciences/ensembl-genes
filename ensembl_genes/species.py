from dataclasses import dataclass
from typing import Optional, Union

from ensembl_genes.models import GeneForMHC


@dataclass
class Species:
    name: str
    common_name: str
    reference_genome: str
    ensembl_gene_pattern: str
    enable_mhc: bool
    mhc_chromosome: str
    mhc_lower: int
    mhc_upper: int
    xmhc_lower: int
    xmhc_upper: int
    chromosomes: list[str]

    def get_mhc_category(self, gene: GeneForMHC) -> Optional[str]:
        """Assign MHC status of MHC, xMHC, or no to an ensembl gene record."""
        if not self.enable_mhc:
            return None
        import pandas as pd

        chromosome: str = gene.chromosome
        start: int = gene.seq_region_start
        end: int = gene.seq_region_end
        if chromosome != self.mhc_chromosome:
            return "no"
        # Ensembl uses 1 based indexing, such that the interval should include
        # the end (closed) as per https://www.biostars.org/p/84686/.
        gene_interval = pd.Interval(left=start, right=end, closed="both")
        mhc = pd.Interval(left=self.mhc_lower, right=self.mhc_upper, closed="both")
        xmhc = pd.Interval(left=self.xmhc_lower, right=self.xmhc_upper, closed="both")
        if gene_interval.overlaps(mhc):
            return "MHC"
        if gene_interval.overlaps(xmhc):
            return "xMHC"
        return "no"


human = Species(
    name="homo_sapiens",
    common_name="human",
    # GRCh38
    reference_genome="38",
    # Regex pattern that valid human ensembl gene IDs should match.
    # https://bioinformatics.stackexchange.com/a/15044/9750
    ensembl_gene_pattern=r"^ENSG[0-9]{11}$",
    # Refs MHC boundary discussion internal Related Sciences issue 127.
    # https://bioinformatics.stackexchange.com/a/14719/9750
    enable_mhc=True,
    mhc_chromosome="6",
    mhc_lower=28_510_120,
    mhc_upper=33_480_577,
    xmhc_lower=25_726_063,
    xmhc_upper=33_410_226,
    # Chromosome names applied to genes on the primary assembly rather than alternative sequences.
    # Refs internal Related Sciences issue 241.
    chromosomes=[*map(str, range(1, 22 + 1)), "X", "Y", "MT"],
)
mouse = Species(
    name="mus_musculus",
    common_name="mouse",
    reference_genome="39",  # GRCm39
    ensembl_gene_pattern=r"^ENSMUSG[0-9]{11}$",
    # FIXME: mhc coordinates (H2 complex)
    # https://doi.org/10.1002/9780470015902.a0000921.pub4
    enable_mhc=False,
    mhc_chromosome="17",
    mhc_lower=28_510_120,
    mhc_upper=33_480_577,
    xmhc_lower=25_726_063,
    xmhc_upper=33_410_226,
    chromosomes=[*map(str, range(1, 19 + 1)), "X", "Y", "MT"],
)
rat = Species(
    name="rattus_norvegicus",
    common_name="rat",
    # Rnor_6.0
    reference_genome="6",
    # https://github.com/related-sciences/ensembl-genes/issues/4#issuecomment-941556912
    ensembl_gene_pattern=r"^ENSRNOG[0-9]{11}$",
    # FIXME: mhc coordinates
    # https://github.com/related-sciences/ensembl-genes/pull/6#discussion_r729259953
    enable_mhc=False,
    mhc_chromosome="20",
    mhc_lower=28_510_120,
    mhc_upper=33_480_577,
    xmhc_lower=25_726_063,
    xmhc_upper=33_410_226,
    chromosomes=[*map(str, range(1, 20 + 1)), "X", "Y", "MT"],
)


all_species = [human, mouse, rat]


def get_species(species: Union[str, Species]) -> Species:
    """Lookup species string from defined Species."""
    if isinstance(species, Species):
        return species
    for match in all_species:
        if species.lower() in {match.name, match.common_name}:
            return match
    raise ValueError(f"species {species!r} not found.")
