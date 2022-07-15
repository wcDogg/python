from pathlib import Path

# -----------------------------------
# Project Directories
# -----------------------------------
DIR_PROJECT = Path(__file__).parent
DIR_CSV = Path(DIR_PROJECT / 'csv')
DIR_JSON = Path(DIR_PROJECT / 'json')
DIR_MD = Path(DIR_PROJECT / 'md')

# -----------------------------------
# I/O File Paths
# Listed here for convienece. 
# -----------------------------------
CSV_NATO = Path(DIR_CSV / 'nato.csv')
MD_NATO = Path(DIR_MD / 'nato.md')
JSON_NATO = Path(DIR_JSON / 'nato.json')

CSV_COUNTRY = Path(DIR_CSV / 'country.csv')
MD_COUNTRY = Path(DIR_MD / 'country.md')

JSON_COUNTRY = Path(DIR_JSON / 'country.json')
JSON_COUNTRY_KEYED = Path(DIR_JSON / 'country-keyed.json')
JSON_COUNTRY_SELECT = Path(DIR_JSON / 'country-select.json')

JSON_CSV = Path(DIR_CSV / 'country-json-to-csv.csv')
JSON_KEYED_CSV = Path(DIR_CSV / 'country-json-keyed-to-csv.csv')


# -----------------------------------
# Test
# -----------------------------------
def print_dirs():

  print(DIR_PROJECT)
  print(DIR_CSV)
  print(DIR_JSON)
  print(DIR_MD)


# print_dirs()