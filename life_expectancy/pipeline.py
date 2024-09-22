
"""Python 3.11.2"""

import argparse
from life_expectancy.data import load_data, save_data
from life_expectancy.cleaning import clean_data
from life_expectancy.regions import Region 


def main(*args, **kwargs) -> None:
    """Main Function which call functions of the data pipeline"""
    raw_df = load_data(kwargs.get('file_name', 'data/eu_life_expectancy_raw.tsv'))
    regions_input = kwargs.get('regions', 'PT')
    regions_list = []

    for region_str in regions_input.split(','):
        region_str = region_str.strip().upper()
        if region_str in Region._value2member_map_:
            region = Region(region_str)
            regions_list.append(region)
        else:
            print(f"Warning, this '{region_str}' is not a valid region")

    for region in regions_list:
        clean_df = clean_data(raw_df, region)
        save_data(clean_df, region.value)



if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-R",
        "--regions",
        help=f"Choose the region you want to filter from here: {[region.value for region in Region]}",
        default="PT",
    )
    parser.add_argument(
        "-fn",
        "--file_name",
        help="Specify data file name. Example: pipeline.py -fn data/eu_life_expectancy_raw.tsv",
        default="data/eu_life_expectancy_raw.tsv",
    )
    arguments = parser.parse_args()
    main(**vars(arguments))