import pytest

from ..ensembl_genes import Ensembl_Gene_Queries
from ..ensembl_genes import GeneForMHC as Gene
from ..ensembl_genes import check_ensembl_release, get_latest_ensembl_release


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
def test_get_mhc_category(gene: Gene, category: str) -> None:
    assert Ensembl_Gene_Queries.get_mhc_category(gene) == category


def test_get_latest_ensembl_release() -> None:
    release = get_latest_ensembl_release()
    assert int(release) >= 104


def test_check_ensembl_release() -> None:
    assert check_ensembl_release("104") == "104"
    with pytest.raises(
        ValueError,
        match="release should be convertible to an int, like '104'. Received 'v104'",
    ):
        check_ensembl_release("v104")
