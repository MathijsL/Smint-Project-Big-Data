#!/usr/local/bin/python

import csv
import cgitb

# set the errors to visible
cgitb.enable(display=1)

def GetMarkten(week):
    with open('resources/markten.csv', 'rb') as f:
        regel = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        # zorg er eerst voor dat de csv in een list wordt gelezen
        csvinfo = []
        for row in regel:
            if   row[0] == "Maandag": dagnr = 0
            elif row[0] == "Dinsdag": dagnr = 1
            elif row[0] == "Woensdag": dagnr = 2
            elif row[0] == "Donderdag": dagnr = 3
            elif row[0] == "Vrijdag": dagnr = 4
            elif row[0] == "Zaterdag": dagnr = 5
            elif row[0] == "Zondag": dagnr = 6
            else: dagnr = 9

            rij=(dagnr,row[0], row[1], row[2])
            csvinfo.append(rij)

    marktenlist = []
    for x in range(len(week)):
        if week[x] == 1:
            for i in range(0,len(csvinfo)):
                if csvinfo[i][0] == x:
                    marktenlist.append(csvinfo[i])

    return marktenlist