"""Tests for the pipeline module."""

import pandas as pd

from life_expectancy.pipeline import main
from . import FIXTURES_DIR, OUTPUT_DIR


def test_pipeline_for_tsv():
    """Test the pipeline with a TSV input file."""
    # Set up the arguments
    args = {
        "file_name": FIXTURES_DIR / "eu_life_expectancy_raw_fixture.tsv",
        "regions": "PT",
    }

    # Run the pipeline
    main(**args)

    # Load expected output
    expected_output = pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv")

    # Load actual output
    actual_output = pd.read_csv(OUTPUT_DIR / "pt_life_expectancy.csv")

    # Compare
    pd.testing.assert_frame_equal(actual_output, expected_output)


def test_pipeline_for_zip():
    """Test the pipeline with a ZIP input file."""
    # Set up the arguments
    args = {
        "file_name": FIXTURES_DIR / "eu_life_expectancy_raw_fixture.zip",
        "regions": "PT",
    }

    # Run the pipeline
    main(**args)

    # Load expected output
    expected_output = pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv")

    # Load actual output
    actual_output = pd.read_csv(OUTPUT_DIR / "pt_life_expectancy.csv")

    # Compare
    pd.testing.assert_frame_equal(actual_output, expected_output)
