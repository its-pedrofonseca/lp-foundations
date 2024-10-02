"""Python 3.11.2"""

from abc import ABC, abstractmethod
from pathlib import Path
import pandas as pd
import zipfile
import json
from typing import Union

DIR_PATH = Path(__file__).parent

class DataLoader(ABC):
    """Abstract base class for data loaders."""

    @abstractmethod
    def load_data(self, file_name: Union[str, Path]) -> pd.DataFrame:
        """Load data from a file and return a DataFrame."""
        pass

class TSVDataLoader(DataLoader):
    """Data loader for TSV files."""

    def load_data(self, file_name: Union[str, Path]) -> pd.DataFrame:
        file_path = DIR_PATH.joinpath(file_name)
        return pd.read_csv(file_path, sep="\t")

class JSONDataLoader(DataLoader):
    """Data loader for JSON files."""

    def load_data(self, file_name: Union[str, Path]) -> pd.DataFrame:
        file_path = DIR_PATH.joinpath(file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        # Adjust this if the JSON structure is nested or complex
        return pd.DataFrame(data)

class ZIPDataLoader(DataLoader):
    """Data loader for ZIP files."""

    def load_data(self, file_name: Union[str, Path]) -> pd.DataFrame:
        zip_path = DIR_PATH.joinpath(file_name)
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Look for supported file types inside the zip
            for inner_file_name in zip_ref.namelist():
                if inner_file_name.endswith('.tsv'):
                    with zip_ref.open(inner_file_name) as file:
                        return pd.read_csv(file, sep='\t')
                elif inner_file_name.endswith('.json'):
                    with zip_ref.open(inner_file_name) as file:
                        data = json.load(file)
                        return pd.DataFrame(data)
            raise ValueError("No supported file formats found inside the ZIP.")

def get_data_loader(file_name: Union[str, Path]) -> DataLoader:
    """Factory function to get the appropriate data loader based on file extension."""
    if isinstance(file_name, Path):
        suffix = file_name.suffix.lower()
    else:
        suffix = Path(file_name).suffix.lower()

    if suffix == '.tsv':
        return TSVDataLoader()
    elif suffix == '.json':
        return JSONDataLoader()
    elif suffix == '.zip':
        return ZIPDataLoader()
    else:
        raise ValueError(f"Unsupported file format: {file_name}")

def load_data(file_name: Union[str, Path] = "data/eu_life_expectancy_raw.tsv") -> pd.DataFrame:
    """Load data using the appropriate data loader."""
    data_loader = get_data_loader(file_name)
    return data_loader.load_data(file_name)

def save_data(data_frame: pd.DataFrame, country: str = "pt") -> None:
    """Function that saves the data into a local CSV file."""
    output_path = DIR_PATH.joinpath(f"data/{country.lower()}_life_expectancy.csv")
    data_frame.to_csv(output_path, index=False)
