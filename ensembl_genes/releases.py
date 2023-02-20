from functools import lru_cache


@lru_cache
def get_latest_ensembl_release() -> str:
    """Return the latest Ensembl release as provided by bioversions."""
    import requests

    url = "https://github.com/biopragmatics/bioversions/raw/main/src/bioversions/resources/versions.json"
    results = requests.get(url).json()
    versions = {
        entry["prefix"]: entry["releases"][-1]["version"]
        for entry in results["database"]
        if "prefix" in entry
    }
    ensembl_release = versions["ensembl"]
    assert isinstance(ensembl_release, str)
    return ensembl_release


def check_ensembl_release(release: str = "latest") -> str:
    """
    Check that ensembl release is properly formatted, like '104'.
    If release is 'latest', get latest release using bioversions.
    https://github.com/related-sciences/ensembl-genes/issues/1
    """
    release = str(release)  # protect against fire
    if release == "latest":
        release = get_latest_ensembl_release()
    try:
        int(release)
    except ValueError as error:
        raise ValueError(
            f"release should be convertible to an int, like '104'. Received {release!r}"
        ) from error
    return release
