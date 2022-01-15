# -*- coding: utf-8 -*-
import sys, csv

# Set output filepath
OUTPATH = "test.csv"

# Set wavelength range
BEGIN = 200.0
END = 1000.0
STEP = 0.5

# Get input filepaths
filepaths = sys.argv[1:]

# Prepare output x and y data
titles = ['wavelength (nm)']
wavelengths = ['{:.2f}'.format(x * STEP + BEGIN) for x in range(int((END - BEGIN) / STEP) + 1)]
write_rows = [[wl] for wl in wavelengths]

# Loop for files
for path in filepaths:
  print(f'Reading {path}')

  # Read CSV file
  with open(path, 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    rows = list(reader)

  # Append title to titles
  title = rows[0][0]
  titles.append(title)

  # Get xy datasets
  xys = rows[2:]
  xs = [xy[0] for xy in xys]
  ys = [xy[1] for xy in xys]
  
  # Append y value to write_rows
  for row in write_rows:
    try:
      i = xs.index(row[0])
      row.append(ys[i])
    except:
      row.append('')

# Export CSV file
print(f'Exporting {OUTPATH}')
with open(OUTPATH, 'w', newline='') as f:
  writer = csv.writer(f)
  writer.writerow(titles)
  writer.writerows(write_rows)
