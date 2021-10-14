import pytest

from ensembl_genes.models import GeneForMHC as Gene
from ensembl_genes.species import get_species, human, rat


def test_get_species() -> None:
    assert get_species("homo_sapiens") is human
    assert get_species("human") is human
    assert get_species("HUMAN") is human
    with pytest.raises(ValueError, match="species 'bad' not found"):
        get_species("bad")


@pytest.mark.parametrize(
    "gene, category",
    [
        # from ENSG00000112493
        (Gene("6", 33_221_298, 33_235_989), "MHC"),
        # fictitious gene interval outside of xMHC
        (Gene("6", 0, 1), "no"),
        # from ENSG00000196126, HLA-DRB1
        (Gene("6", 32_578_769, 32_589_848), "MHC"),
        # not on chromosome 6
        (Gene("7", 32_578_769, 32_589_848), "no"),
        # H2AC1, ENSG00000164508, lower boundary gene of xMHC
        (Gene("6", 25_726_063, 25_726_562), "xMHC"),
        # ENSG00000237649, KIFC1, upper bound of MHC
        (Gene("6", 33_391_823, 33_409_896), "MHC"),
    ],
)
def test_get_mhc_category_human(gene: Gene, category: str) -> None:
    assert human.get_mhc_category(gene) == category


def test_get_mhc_category_rat() -> None:
    gene = Gene("20", 0, 0)
    assert rat.enable_mhc is False
    assert rat.get_mhc_category(gene) is None
