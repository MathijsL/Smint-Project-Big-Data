#!/usr/local/bin/python

import csv
import cgitb

cgitb.enable(display=1)

def GetMarkten(week):
    with open('resources/markten.csv', 'rb') as f:
        regel = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        csvinfo = []

        for row in regel:
            rij=(row[0], row [1], row[2])
            csvinfo.append(rij);

    marktenlist = []

    for x in range(0,len(week)):
        if week[x] == 1:
            print csvinfo[x][0] +","+ csvinfo[x][1]  
            marktenlist.append(csvinfo[x])
        else:
            pass
    return marktenlist