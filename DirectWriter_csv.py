import csv
with open('names.csv', 'w', newline='') as csvfile:
  fieldnames = ['First Name', 'Last Name', 'Result']
  writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
  writer.writeheader()
  writer.writerow({'First Name':'John',
                  'Last Name': 'Smith',
                  'Result': 54})
  writer.writerow({'First Name':'Dhruba',
                  'Last Name': 'Kalita',
                  'Result': 100})
  writer.writerow({'First Name':'Prabhat',
                  'Last Name': 'Kumar',
                  'Result': 200})
