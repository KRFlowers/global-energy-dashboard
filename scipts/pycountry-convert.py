import pandas as pd
import pycountry_convert as pc

# add path to your csv file located in parent directory /data/processed

csv_file_path = '../data/processed/owid_energy_dashboard_subset.csv'

df = pd.read_csv(csv_file_path)

def iso_to_continent(iso3):
    if pd.isna(iso3) or iso3 == '':
        return 'Unknown'
    try:
        iso2 = pc.country_alpha3_to_country_alpha2(iso3)
        continent_code = pc.country_alpha2_to_continent_code(iso2)
        continent_name = pc.convert_continent_code_to_continent_name(continent_code)
        return continent_name
    except KeyError:
        return 'Unknown'

df['continent'] = df['iso_code'].apply(iso_to_continent)
df.to_csv('../data/processed/owid_energy_dashboard_subset_with_continent.csv', index=False)