import pytest

from ensembl_genes.ensembl_genes import Ensembl_Gene_Queries


def test_ensembl_gene_queries() -> None:
    Ensembl_Gene_Queries()


@pytest.mark.parametrize(
    "raw_description,expect_description,expect_src,expect_id",
    [
        (
            "G protein subunit gamma 5 pseudogene 3 [Source:HGNC Symbol;Acc:HGNC:33552]",
            "G protein subunit gamma 5 pseudogene 3",
            "HGNC Symbol",
            "HGNC:33552",
        ),
        ("Y RNA [Source:RFAM;Acc:RF00019]", "Y RNA", "RFAM", "RF00019"),
        (
            "syndecan binding protein (syntenin) 2 [Source:MGI Symbol;Acc:MGI:2385156]",
            "syndecan binding protein (syntenin) 2",
            "MGI Symbol",
            "MGI:2385156",
        ),
        ("novel protein", "novel protein", None, None),
    ],
)
def test_ensembl_gene_description_regex(
    raw_description: str,
    expect_description: str | None,
    expect_src: str | None,
    expect_id: str | None,
) -> None:
    """
    See https://regex101.com/r/wbW1Qc/1/
    """
    match = Ensembl_Gene_Queries.description_pattern.match(raw_description)
    assert match
    assert match.group("gene_description") == expect_description
    assert match.group("gene_description_source_db") == expect_src
    assert match.group("gene_description_source_id") == expect_id
