"""Pytest configuration file for setting up test fixtures."""

import pandas as pd
import pytest

from life_expectancy.data import load_data_from_zip
from . import FIXTURES_DIR

@pytest.fixture(scope="session")
def pt_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output for Portugal."""
    return pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv")


@pytest.fixture(scope="session")
def eu_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected raw EU life expectancy data (TSV)."""
    return pd.read_csv(FIXTURES_DIR / "eu_life_expectancy_raw_fixture.tsv", sep="\t")


@pytest.fixture(scope="session")
def json_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected raw EU life expectancy data (JSON)."""
    return pd.read_json(FIXTURES_DIR / "eu_life_expectancy_raw_fixture.json")


@pytest.fixture(scope="session")
def zip_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected raw EU life expectancy data from a ZIP file."""
    zip_path = FIXTURES_DIR / "eu_life_expectancy_raw_fixture.zip"
    return load_data_from_zip(zip_path)  # Use the function from data.py
