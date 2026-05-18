"""
01_data_preparation.py
Add continent column to OWID energy dataset using ISO-3 country codes.
"""

import pandas as pd
import pycountry_convert as pc

from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
INPUT_PATH = PROJECT_ROOT / 'data' / 'processed' / 'owid_energy_dashboard_subset.csv'
OUTPUT_PATH = PROJECT_ROOT / 'data' / 'processed' / 'owid_energy_dashboard_subset_with_continent.csv'


def iso_to_continent(iso3: str) -> str:
    """
    Map an ISO-3 country code to a continent name.
    Returns 'Unknown' for codes that cannot be mapped (e.g., regional
    aggregates like OWID_WRL, OWID_EUR, or politically ambiguous entities).
    """
    if pd.isna(iso3) or iso3 == '':
        return 'Unknown'
    try:
        iso2 = pc.country_alpha3_to_country_alpha2(iso3)
        continent_code = pc.country_alpha2_to_continent_code(iso2)
        return pc.convert_continent_code_to_continent_name(continent_code)
    except KeyError:
        return 'Unknown'


def main():
    df = pd.read_csv(INPUT_PATH)
    print(f"Loaded {len(df):,} rows from {INPUT_PATH}")

    df['continent'] = df['iso_code'].apply(iso_to_continent)

    # Diagnostic: see what got mapped and what didn't
    print("\nContinent distribution:")
    print(df['continent'].value_counts(dropna=False))

    # Show which iso_codes failed to map — these are your edge cases
    unknown_codes = df[df['continent'] == 'Unknown']['iso_code'].unique()
    print(f"\nIso codes mapped to 'Unknown' ({len(unknown_codes)} unique):")
    print(sorted([c for c in unknown_codes if pd.notna(c) and c != '']))

    df.to_csv(OUTPUT_PATH, index=False)
    print(f"\nSaved to {OUTPUT_PATH}")


if __name__ == '__main__':
    main()