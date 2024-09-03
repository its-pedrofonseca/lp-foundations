"""Tests for the life_expectancy cleaning module.

This module contains unit tests for the functions in the cleaning module,
specifically testing the clean_data function to ensure it produces the expected output.
"""

import pandas as pd

from life_expectancy.cleaning import clean_data

def test_clean_data(pt_life_expectancy_expected, eu_life_expectancy_expected):
    """Run unit test of function `clean_data`"""
    actual_data = clean_data(eu_life_expectancy_expected).reset_index(drop=True)
    expected_data = pt_life_expectancy_expected
    pd.testing.assert_frame_equal(actual_data, expected_data)
