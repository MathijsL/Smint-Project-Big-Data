#!/usr/local/bin/python

import csv
import cgitb

# set the errors to visible
cgitb.enable(display=1)

# function returns all supermarkets
def GetSupermarkten(): 
    with open('resources/supermarkten.csv', 'rb') as f:
        regel = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        csvinfo = []

        for row in regel:
            rij=(row[0], row [1], row[2], row[3], row[4])
            csvinfo.append(rij);
        return csvinfo