"""Python 3.11.2"""

import argparse
from life_expectancy.data import load_data, save_data
from life_expectancy.cleaning import clean_data
from life_expectancy.regions import Region


def main(**kwargs) -> None:
    """Main Function which call functions of the data pipeline"""
    file_name = kwargs.get("file_name", "data/eu_life_expectancy_raw.tsv")
    raw_df = load_data(file_name)
    regions_input = kwargs.get("regions", "PT")
    regions_list = []

    for region_str in regions_input.split(","):
        region_str = region_str.strip().upper()
        if region_str in [region.value for region in Region]:
            region = Region(region_str)
            regions_list.append(region)
        else:
            print(f"Warning, this '{region_str}' is not a valid region")

    cleaned_dataframes = []
    for region in regions_list:
        clean_df = clean_data(raw_df, region)
        save_data(clean_df, region.value)
        cleaned_dataframes.append(clean_df)
    if len(cleaned_dataframes) == 1:
        return cleaned_dataframes[0]
    if len(cleaned_dataframes) > 1:
        return {
            region.value: df
            for region, df in zip(regions_list, cleaned_dataframes)
        }
    return None


if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-R",
        "--regions",
        help=(
            "Choose the region you want to filter from here: "
            f"{[region.value for region in Region]}"
        ),
        default="PT",
    )
    parser.add_argument(
        "-fn",
        "--file_name",
        help=(
            "Specify data file name. "
            "Example: pipeline.py -fn data/eu_life_expectancy_raw.tsv"
        ),
        default="data/eu_life_expectancy_raw.tsv",
    )
    arguments = parser.parse_args()
    main(**vars(arguments))