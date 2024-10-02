"""Pytest configuration file"""
import pandas as pd
import pytest
import zipfile
import json
from pathlib import Path

# Define the directory containing test fixtures
FIXTURES_DIR = Path(__file__).parent / "fixtures"

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
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for inner_file_name in zip_ref.namelist():
            if inner_file_name.endswith('.tsv'):
                with zip_ref.open(inner_file_name) as file:
                    return pd.read_csv(file, sep='\t')
            elif inner_file_name.endswith('.json'):
                with zip_ref.open(inner_file_name) as file:
                    data = json.load(file)
                    return pd.DataFrame(data)
    raise ValueError("No supported file formats found inside the ZIP.")
