import subprocess


def test_cli_ensembl_release() -> None:
    release = subprocess.check_output(
        ["ensembl_genes", "ensembl_release", "--release=109"], text=True
    ).strip()
    assert release == "109"
