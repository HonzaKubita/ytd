import re
from pathlib import Path

path = f"{Path.home()}\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\pytube\\cipher.py"

with open(path, 'r') as file:
  filedata = file.read()

  filedata = filedata.replace('transform_plan_raw = find_object_from_startpoint(raw_code, match.span()[1] - 1)', 'transform_plan_raw = js')

with open(path, 'w') as file:
  file.write(filedata)
