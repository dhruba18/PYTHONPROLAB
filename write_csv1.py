import csv
# To create csv file
print('Ceting CSV file')
with open('sample.csv', 'w', newline='') as csvfile:
  writer=csv.writer(csvfile)
  writer.writerow(['She loves you', 'Sept 1963'])
  writer.writerow(['I want to hold your hand', 'Dec 1963'])
  writer.writerow(['Cant buy me love', 'Apr 1964'])
  writer.writerow(['A hard days night', 'July 1963'])
