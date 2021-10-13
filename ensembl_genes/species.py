from dataclasses import dataclass
from typing import Union


@dataclass
class Species:
    name: str
    common_name: str
    reference_genome: str
    ensembl_gene_pattern: str
    mhc_chromosome: str
    mhc_lower: int
    mhc_upper: int
    xmhc_lower: int
    xmhc_upper: int
    chromosomes: list[str]


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
    mhc_chromosome="6",
    mhc_lower=28_510_120,
    mhc_upper=33_480_577,
    xmhc_lower=25_726_063,
    xmhc_upper=33_410_226,
    # Chromosome names applied to genes on the primary assembly rather than alternative sequences.
    # Refs internal Related Sciences issue 241.
    chromosomes=[*map(str, range(1, 23)), "X", "Y", "MT"],
)

all_species = [human]


def get_species(species: Union[str, Species]) -> Species:
    """Lookup species string from defined Species."""
    if isinstance(species, Species):
        return species
    for match in all_species:
        if species.lower() in {match.name, match.common_name}:
            return match
    raise ValueError(f"species {species!r} not found.")
