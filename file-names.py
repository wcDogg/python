from os import listdir
from pathlib import Path

dir_start: Path = "D:\Media\Movies"
file_out: Path = "D:\Media\Movies/list.md"

# print(dir_start)
# print(file_out)

for f in listdir(dir_start):
  print(f)
