import pytest

from ensembl_genes.species import get_species, human


def test_get_species() -> None:
    assert get_species("homo_sapiens") is human
    assert get_species("human") is human
    assert get_species("HUMAN") is human
    with pytest.raises(ValueError, match="species 'bad' not found"):
        get_species("bad")
