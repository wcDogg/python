import json
import csv
from pathlib import Path
import configure


def json_records_to_csv(input, output):
  '''Converts a JSON file in records format
  (list of dictionaries) to a CSV file.
  * `input` - File path string
  * `output` - File path string
  '''
  data = None
  headers = None
  print(f'File in: %s' % input)

  try: 
    with Path(input).open('r', encoding='utf-8') as source:
      data = json.load(source)

    headers = list(data[0].keys())  

    with Path(output).open('w', encoding='utf-8', newline='') as save:
        
        write = csv.writer(save)
        write.writerow(headers)

        for k in data:
            write.writerow(k.values())

    print(f'File out: %s' % output)

  except Exception as e:
    print(f'File error: %s' % input)
    print(e)
    return


def json_keyed_to_csv(input, output, firstcol):
  '''Converts a JSON file with simple nesting to a CSV file.
  * `input` - File path string
  * `output` - File path string
  * `firstcol` - First column's heading string
  '''
  data = None
  headers = [firstcol]
  print(f'File in: %s' % input)

  try: 
    with Path(input).open('r', encoding='utf-8') as source:
      data = json.load(source)

    # The first key's nested keys become headers.
    first_key = next(iter(data))
    for k in data[first_key]:
      headers.append(k)

    with Path(output).open('w', encoding='utf-8', newline='') as save:
      write = csv.writer(save)
      write.writerow(headers)
      
      for key in data.keys():
        row = [key]
        for nested in data[key].keys():
          row.append(data[key][nested])

        write.writerow(row)

    print(f'File out: %s' % output)

  except Exception as e:
    print(f'File error: %s' % input)
    print(e)
    return


# --------------------------------------
# Tasks
# --------------------------------------
json_records_to_csv(configure.JSON_COUNTRY_SELECT, configure.JSON_CSV)
json_keyed_to_csv(configure.JSON_COUNTRY_KEYED, configure.JSON_KEYED_CSV, 'ISO2')
