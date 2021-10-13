from typing import NamedTuple


class GeneForMHC(NamedTuple):
    """Argument type for get_mhc_category, to mimic pd.DataFrame.itertuples element."""

    chromosome: str
    seq_region_start: int
    seq_region_end: int
