import pandas as pd
import os
import glob

def list_tsv_files():
    """List TSV files in the given folder."""

    current_folder = os.getcwd()
    pattern = os.path.join(current_folder, "life_expectancy/data", "*.tsv")
    tsv_files = glob.glob(pattern)
    print(tsv_files)
    if not tsv_files:
        raise FileNotFoundError("No TSV files found in the data directory.")
    return tsv_files[0]

def clean_data():
    """
    
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

    # Filter data for PT
    df = df[df['region'] == 'PT']

    # Save the df into CSV file 
    df.to_csv('life_expectancy/data/pt_life_expectancy.csv', index=False)

    return df

# Run the function
if __name__ == "__main__":
    list_tsv_files()
