import pytest

from ensembl_genes.releases import check_ensembl_release, get_latest_ensembl_release


def test_get_latest_ensembl_release() -> None:
    release = get_latest_ensembl_release()
    assert int(release) >= 104


def test_check_ensembl_release() -> None:
    assert check_ensembl_release("104") == "104"
    assert int(check_ensembl_release("latest")) >= 104
    with pytest.raises(
        ValueError,
        match="release should be convertible to an int, like '104'. Received 'v104'",
    ):
        check_ensembl_release("v104")
