import csv
from pathlib import Path
import configure

def csv_to_md_table(input, output, align='center', brow='true', bcol='false'): 
  '''Converts a CSV file to a Markdown table.
  * `input` - File path string
  * `output` - File path string
  * `align` - `'left'`, `'right'`, `'center'` (default)
  * `brow` - Bold the first row `'true'` (default), `'false'`
  * `bcol` - Bold the first column `'true'`, `'false'` (default)
  '''
  data = None
  headers = None
  hdiv = None
  first_key = None
  pipe = '|'
  nl = '\n'
  bold = '**'
  space = ' '
  left =    ':-----|'
  right =   '-----:|'
  center =  ':----:|'

  try: 
    # Set header row alingment div.
    if align == 'center':
      hdiv = center
    elif align == 'left':
      hdiv = left
    elif align == 'right':
      hdiv = right
    else:
      raise Exception("The `align` argument must be 'left', 'right', or 'center'.")

    print(f'File in: %s' % input)

    # Create a list of dictionaries.
    with Path(input).open('r', encoding='utf-8') as source:

      reader = csv.DictReader(source)
      data = [rows for rows in reader]

    # Get the header row column names. 
    headers = list(data[0].keys())

    # Get the dict key for the first column. 
    first_key = headers[0]
    print(first_key)

    # Write to MD file.
    with Path(output).open('w', encoding='utf-8') as save:

      save.write(pipe)
      for h in headers:
        if brow == 'true':
          save.write(space + bold + h + bold + space + pipe)
        else: 
          save.write(space + h + space + pipe)
      
      save.write(nl)
      save.write(pipe)
      for _i in range(len(headers)): 
        save.write(hdiv)

      save.write(nl)
      for d in data:
        save.write(pipe)
        for h in headers:
          if bcol == 'true' and h == first_key:
            save.write(space + bold + d[h] + bold + space + pipe)
          else: 
            save.write(space + d[h] + space + pipe)
        save.write(nl)

    print(f'File out: %s' % output)

  except Exception as e:
    print(f'Error: %s' % input)
    print(e)
    return
  

# -----------------------------------
# Tasks
# -----------------------------------  
csv_to_md_table(configure.CSV_NATO, configure.MD_NATO, 'left', 'true', 'true')
csv_to_md_table(configure.CSV_COUNTRY, configure.MD_COUNTRY, 'center', 'true', 'false')

