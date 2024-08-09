import pandas as pd
from life_expectancy.cleaning import load_data, clean_data, save_data
from . import OUTPUT_DIR

def test_clean_data(pt_life_expectancy_expected):
    """Run the `clean_data` function and compare the output to the expected output"""
    
    # Load the raw data
    raw_data = load_data()
    
    # Clean the data
    cleaned_data = clean_data(raw_data, country="PT")
    
    # Save the cleaned data to a file
    save_data(cleaned_data, country="PT")
    
    # Load the saved file
    pt_life_expectancy_actual = pd.read_csv(
        OUTPUT_DIR / "pt_life_expectancy.csv"
    )
    
    # Compare the actual and expected dataframes
    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )