import csv
from db import Cashball

records = Cashball.select()

with open('export.csv', 'w', newline= '') as csvfile:
    fieldnames = ['casino', 'datetime', 'dollar']
    writer = csv.DictWriter(csvfile, fieldnames= fieldnames)
    writer.writeheader()
    for record in records:
        writer.writerow({'casino': record.casino,
                         'datetime': record.datetime,
                         'dollar' : record.dollar})

