import csv
with open('markten.csv', 'rb') as f:
    regel = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
    for row in regel:
        print row