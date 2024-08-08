"""
This module contains functions for cleaning and processing life expectancy data.
"""

import os
import glob
import argparse
import pandas as pd

def list_tsv_files():
    """List TSV files in the given folder."""

    current_folder = os.getcwd()
    pattern = os.path.join(current_folder, "life_expectancy/data", "*.tsv")
    tsv_files = glob.glob(pattern)
    if not tsv_files:
        raise FileNotFoundError("No TSV files found in the data directory.")
    return tsv_files[0]


def clean_values(value):
    """Removes all non-numeric and non-decimal characters from a string."""
    return ''.join(c for c in value if c.isdigit() or c == '.') if isinstance(value, str) else value


def clean_data(country = "PT"):
    """
    This function read input file and applies data transformations to output csv file
    """

    # i) Read data from file
    file = list_tsv_files()
    data_frame = pd.read_csv(file, sep="\t")

    # ii) Correct data_frame and unpivot data
    data_frame[['unit', 'sex', 'age', 'region']] = data_frame['unit,sex,age,geo\\time'].str.split(',', expand=True)
    data_frame = data_frame.drop(columns=['unit,sex,age,geo\\time'])
    data_frame = pd.melt(data_frame, id_vars=['unit', 'sex', 'age', 'region'], var_name='year', value_name='value')

    # iii) Cast year to int and value to float
    data_frame['year'] = data_frame['year'].astype(int)
    data_frame['value'] = data_frame['value'].apply(clean_values)
    data_frame['value'] = pd.to_numeric(data_frame['value'].str.replace(':', ''), errors='coerce')

    # iv) Remove nan
    data_frame = data_frame.dropna(subset=['value'])

    # v) Filter data for country
    data_frame = data_frame[data_frame['region'] == country]

    # vi) Save the data_frame into CSV file 
    current_folder = os.getcwd()
    output_file = f'{current_folder}/life_expectancy/data/{country.lower()}_life_expectancy.csv'
    data_frame.to_csv(output_file, index=False)

    return data_frame

# Run the function
if __name__ == "__main__": # pragma: no cover

    #init parser
    parser = argparse.ArgumentParser()
    parser.add_argument("--country", type=str, default="PT", help="Country code to filter data (default: PT)")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Pass the country argument clean_data
    clean_data(country=args.country)
