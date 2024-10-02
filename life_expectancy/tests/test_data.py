"""Tests for the pipeline module"""

from unittest.mock import patch

import pandas as pd
import pytest

from life_expectancy.data import (
    TSVDataLoader,
    JSONDataLoader,
    ZIPDataLoader,
    get_data_loader,
    load_data,
    save_data,
)
from . import FIXTURES_DIR, OUTPUT_DIR


def test_load_data_tsv(eu_life_expectancy_expected):
    """Test loading data from a TSV file using load_data function."""
    actual_data = load_data(FIXTURES_DIR / "eu_life_expectancy_raw_fixture.tsv")
    expected_data = eu_life_expectancy_expected
    pd.testing.assert_frame_equal(actual_data, expected_data)


def test_load_data_json(json_life_expectancy_expected):
    """Test loading data from a JSON file using load_data function."""
    actual_data = load_data(FIXTURES_DIR / "eu_life_expectancy_raw_fixture.json")
    expected_data = json_life_expectancy_expected
    pd.testing.assert_frame_equal(actual_data, expected_data)


def test_load_data_zip(zip_life_expectancy_expected):
    """Test loading data from a ZIP file using load_data function."""
    actual_data = load_data(FIXTURES_DIR / "eu_life_expectancy_raw_fixture.zip")
    expected_data = zip_life_expectancy_expected
    pd.testing.assert_frame_equal(actual_data, expected_data)


def test_tsv_data_loader(eu_life_expectancy_expected):
    """Test loading data using the TSVDataLoader."""
    loader = TSVDataLoader()
    actual_data = loader.load_data(FIXTURES_DIR / "eu_life_expectancy_raw_fixture.tsv")
    expected_data = eu_life_expectancy_expected
    pd.testing.assert_frame_equal(actual_data, expected_data)


def test_json_data_loader(json_life_expectancy_expected):
    """Test loading data using the JSONDataLoader."""
    loader = JSONDataLoader()
    actual_data = loader.load_data(FIXTURES_DIR / "eu_life_expectancy_raw_fixture.json")
    expected_data = json_life_expectancy_expected
    pd.testing.assert_frame_equal(actual_data, expected_data)


def test_zip_data_loader(zip_life_expectancy_expected):
    """Test loading data using the ZIPDataLoader."""
    loader = ZIPDataLoader()
    actual_data = loader.load_data(FIXTURES_DIR / "eu_life_expectancy_raw_fixture.zip")
    expected_data = zip_life_expectancy_expected
    pd.testing.assert_frame_equal(actual_data, expected_data)


def test_get_data_loader():
    """Test the get_data_loader factory function."""
    loader = get_data_loader("data/file.tsv")
    assert isinstance(loader, TSVDataLoader)
    loader = get_data_loader("data/file.json")
    assert isinstance(loader, JSONDataLoader)
    loader = get_data_loader("data/file.zip")
    assert isinstance(loader, ZIPDataLoader)
    with pytest.raises(ValueError):
        get_data_loader("data/file.unsupported")


def test_save_data(pt_life_expectancy_expected):
    """Test saving data using the save_data function."""
    expected_file = OUTPUT_DIR.joinpath("pt_life_expectancy.csv")
    with patch.object(pt_life_expectancy_expected, "to_csv") as to_csv_mock:
        save_data(pt_life_expectancy_expected, country="pt")
        to_csv_mock.assert_called_with(expected_file, index=False)
