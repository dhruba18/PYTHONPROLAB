## Reading a csv file

import csv
print('Starting to read csv file')
with open('sample.csv','r', newline='') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    print(*row, sep=', ')
print('done reading')
