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

def clean_data(country = "PT"):
    """
    This function read input file and applies data transformations to output csv file
    """

    # Read data from file
    file = list_tsv_files()
    df = pd.read_csv(file, sep="\t")

    # Correct df and unpivot data
    df[['unit', 'sex', 'age', 'region']] = df['unit,sex,age,geo\\time'].str.split(',', expand=True)
    df = df.drop(columns=['unit,sex,age,geo\\time'])
    df = pd.melt(df, id_vars=['unit', 'sex', 'age', 'region'], var_name='year', value_name='value')

    # Cast year to int and value to float
    df['year'] = df['year'].astype(int)
    df['value'] = pd.to_numeric(df['value'].str.replace(':', ''), errors='coerce')

    # Remove nan
    df = df.dropna(subset=['value'])

    # Filter data for country
    df = df[df['region'] == country]

    # Save the df into CSV file 
    current_folder = os.getcwd()
    output_file = f'{current_folder}/life_expectancy/data/{country.lower()}_life_expectancy.csv'
    df.to_csv(output_file, index=False)

    return df

# Run the function
if __name__ == "__main__": # pragma: no cover

    #init parser
    parser = argparse.ArgumentParser()
    parser.add_argument("--country", type=str, default="PT", help="Country code to filter data (default: PT)")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Pass the country argument clean_data
    clean_data(country=args.country)
