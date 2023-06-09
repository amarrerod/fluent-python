"""Main module."""


from .chapter_1_data_model.__main__ import run_card_examples
from .chapter_2_arrays.__main__ import (
    list_comprehension,
    list_comps_vs_mapfilter,
    cartesian_shirts,
    cartesian_cards,
    genexps_examples,
)

if __name__ == "__main__":
    run_card_examples()
    list_comprehension()
    list_comps_vs_mapfilter()
    cartesian_shirts()
    cartesian_cards()
    genexps_examples()
