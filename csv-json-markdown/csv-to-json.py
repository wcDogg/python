import csv
import json
from pathlib import Path
import configure


def csv_to_json_records(input, output):
  '''Converts CSV to JSON list of dictionaries (records format).
  * `input` - File path string
  * `output` - File path string
  '''
  data = None
  print(f'File in: %s' % input)

  try: 
    with Path(input).open('r', encoding='utf-8') as source:
      reader = csv.DictReader(source)
      data = [rows for rows in reader]

    with Path(output).open('w', encoding='utf-8') as save:
      save.write(json.dumps(data, indent=4))

    print(f'File out: %s' % output)

  except Exception as e:
    print(f'File error: %s' % input)
    print(e)
    return


def csv_to_json_records_select(input, output, headers):
  '''Converts selected columns of a CSV to JSON
  list of dictionaries (records format). 
  * `input` - File path string
  * `output` - File path string
  * `headers` - A [list] of column headings to include 
  '''
  data = None
  print(f'File in: %s' % input)

  try: 
    with Path(input).open('r', encoding='utf-8') as source:
      reader = csv.DictReader(source)
      data = [rows for rows in reader]

    for d in data:
      for k in list(d.keys()):
        if k not in headers:
          del d[k]

    with Path(output).open('w', encoding='utf-8') as save:
      save.write(json.dumps(data, indent=4))

    print(f'File out: %s' % output)

  except Exception as e:
    print(f'File error: %s' % input)
    print(e)
    return


def csv_to_json_keyed(input, output, keyname):
  '''Converts CSV to JSON nested dictionaries where each
  dictionary is identified by the given CSV column name.
  * `input` - File path string
  * `output` - File path string
  * `keyname` - The column heading to use as main dict key. 
  '''
  data = {}
  print(f'File in: %s' % input)

  try: 
    with Path(input).open('r', encoding='utf-8') as source:
      reader = csv.DictReader(source)

      for rows in reader:
        key = rows[keyname]
        data[key] = rows

    with Path(output).open('w', encoding='utf-8') as save:
      save.write(json.dumps(data, indent=4))

    print(f'File out: %s' % output)

  except Exception as e:
    print(f'File error: %s' % input)
    print(e)
    return


# --------------------------------------
# Tasks
# --------------------------------------
# Unique Record ID column
ID = 'ISO2'
# Select Column Names
COLUMNS = ['ISO2','Country Name', 'Continent', 'Capital']

csv_to_json_records(configure.CSV_NATO, configure.JSON_NATO)
csv_to_json_records(configure.CSV_COUNTRY, configure.JSON_COUNTRY)
csv_to_json_keyed(configure.CSV_COUNTRY, configure.JSON_COUNTRY_KEYED, ID)
csv_to_json_records_select(configure.CSV_COUNTRY, configure.JSON_COUNTRY_SELECT, COLUMNS)

