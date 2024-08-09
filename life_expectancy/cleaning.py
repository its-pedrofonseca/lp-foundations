"""
This module contains functions for loading, cleaning, and saving life expectancy data.
"""

import os
import glob
import argparse
import pandas as pd

def list_tsv_files():

    """List the first TSV file in the life_expectancy/data folder."""

    current_folder = os.getcwd()
    pattern = os.path.join(current_folder, "life_expectancy/data", "*.tsv")
    tsv_files = glob.glob(pattern)
    if not tsv_files:
        raise FileNotFoundError("No TSV files found in the data directory.")
    return tsv_files[0]

def clean_values(value):

    """Removes all non-numeric and non-decimal characters from a string."""

    return ''.join(c for c in value if c.isdigit() or c == '.') if isinstance(value, str) else value

def load_data():

    """Load data from the first TSV file found."""

    file = list_tsv_files()
    data_frame = pd.read_csv(file, sep="\t")
    return data_frame

def clean_data(data_frame, country="PT"):

    """
    Clean the data by unpivoting it, filtering country, and applying necesary transformations.
    
    Args:
        data_frame (pd.DataFrame): The raw data frame to clean.
        country (str): Country code to filter data by (default is 'PT').

    Returns:
        pd.DataFrame: data fra
        me.
    """

    # Unpivot data
    data_frame[['unit', 'sex', 'age', 'region']] = data_frame['unit,sex,age,geo\\time'].str.split(',', expand=True)
    data_frame = data_frame.drop(columns=['unit,sex,age,geo\\time'])
    data_frame = pd.melt(data_frame, id_vars=['unit', 'sex', 'age', 'region'], var_name='year', value_name='value')

    # Clean and convert data types
    data_frame['year'] = data_frame['year'].astype(int)
    data_frame['value'] = data_frame['value'].apply(clean_values)
    data_frame['value'] = pd.to_numeric(data_frame['value'], errors='coerce')

    # Remove NaN values and filter by country
    data_frame = data_frame.dropna(subset=['value'])
    data_frame = data_frame[data_frame['region'] == country]

    return data_frame

def save_data(data_frame, country="PT"):
    
    """
    Save the cleaned data to a CSV file.
    
    Args:
        data_frame (pd.DataFrame): The cleaned data frame to save.
        country (str): Country code used for naming the output file (default is 'PT').
    """

    current_folder = os.getcwd()
    output_file = f'{current_folder}/life_expectancy/data/{country.lower()}_life_expectancy.csv'
    data_frame.to_csv(output_file, index=False)

if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser(description="Process and clean life expectancy data.")
    parser.add_argument("--country", type=str, default="PT", help="Country code to filter data (default: PT)")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Load, clean, and save data functions being called
    raw_data = load_data()
    cleaned_data = clean_data(raw_data, country=args.country)
    save_data(cleaned_data, country=args.country)