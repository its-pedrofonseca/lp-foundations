import pandas as pd
from pathlib import Path

# Define the path to your TSV fixture
tsv_fixture_path = Path('life_expectancy/tests/fixtures/eu_life_expectancy_raw_fixture.tsv')

# Read the TSV fixture into a DataFrame
df = pd.read_csv(tsv_fixture_path, sep='\t')

# Define the path for the new JSON fixture
json_fixture_path = Path('life_expectancy/tests/fixtures/eu_life_expectancy_raw_fixture.json')

# Save the DataFrame as a JSON file
df.to_json(json_fixture_path, orient='records', lines=False)