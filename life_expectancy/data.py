"""Life expectancy"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Union
import json
import zipfile

import pandas as pd

DIR_PATH = Path(__file__).parent


class DataLoader(ABC): # pylint: disable=too-few-public-methods
    """Abstract base class for data loaders."""

    @abstractmethod
    def load_data(self, file_name: Union[str, Path]) -> pd.DataFrame:
        """Load data from a file and return a DataFrame."""


class TSVDataLoader(DataLoader):  # pylint: disable=too-few-public-methods
    """Data loader for TSV files."""

    def load_data(self, file_name: Union[str, Path]) -> pd.DataFrame:
        file_path = DIR_PATH.joinpath(file_name)
        return pd.read_csv(file_path, sep="\t")


class JSONDataLoader(DataLoader):  # pylint: disable=too-few-public-methods
    """Data loader for JSON files."""

    def load_data(self, file_name: Union[str, Path]) -> pd.DataFrame:
        file_path = DIR_PATH.joinpath(file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return pd.DataFrame(data)


class ZIPDataLoader(DataLoader):  # pylint: disable=too-few-public-methods
    """Data loader for ZIP files."""

    def load_data(self, file_name: Union[str, Path]) -> pd.DataFrame:
        zip_path = DIR_PATH.joinpath(file_name)
        return load_data_from_zip(zip_path)


def get_data_loader(file_name: Union[str, Path]) -> DataLoader:
    """Factory function to get the appropriate data loader based on file extension."""
    if isinstance(file_name, Path):
        suffix = file_name.suffix.lower()
    else:
        suffix = Path(file_name).suffix.lower()

    if suffix == '.tsv':
        return TSVDataLoader()
    if suffix == '.json':
        return JSONDataLoader()
    if suffix == '.zip':
        return ZIPDataLoader()
    raise ValueError(f"Unsupported file format: {file_name}")


def load_data(file_name: Union[str, Path] = "data/eu_life_expectancy_raw.tsv") -> pd.DataFrame:
    """Load data using the appropriate data loader."""
    data_loader = get_data_loader(file_name)
    return data_loader.load_data(file_name)


def save_data(data_frame: pd.DataFrame, country: str = "pt") -> None:
    """Function that saves the data into a local CSV file."""
    output_path = DIR_PATH.joinpath(f"data/{country.lower()}_life_expectancy.csv")
    data_frame.to_csv(output_path, index=False)


def load_data_from_zip(zip_path: Path) -> pd.DataFrame:
    """Utility function to load data from a ZIP file."""
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for inner_file_name in zip_ref.namelist():
            if inner_file_name.endswith('.tsv'):
                with zip_ref.open(inner_file_name) as file:
                    return pd.read_csv(file, sep='\t')
            if inner_file_name.endswith('.json'):
                with zip_ref.open(inner_file_name) as file:
                    data = json.load(file)
                    return pd.DataFrame(data)
    raise ValueError("No supported file formats found inside the ZIP.")
