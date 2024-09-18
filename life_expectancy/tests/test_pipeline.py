"""Tests for the pipeline module"""
from unittest.mock import patch
import pandas as pd
from life_expectancy.pipeline import main
from . import FIXTURES_DIR


@patch("life_expectancy.pipeline.save_data")
def test_main(mock, pt_life_expectancy_expected):
    """Run the `main` function and compare the output to the expected output"""
    mock.side_effect = print("Mocking save data")
    actual_data = main(
        file_name=f"{FIXTURES_DIR}/eu_life_expectancy_raw_fixture.tsv", regions="PT"
    ).reset_index(drop=True)
    expected_data = pt_life_expectancy_expected.reset_index(drop=True)
    pd.testing.assert_frame_equal(actual_data, expected_data)
    