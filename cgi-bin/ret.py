#!/usr/local/bin/python

import csv
import cgitb

# set the errors to visible
cgitb.enable(display=1)

def GetHalte(x):  #type weglaten levert geeft alle haltes terug
    if   x == "B":
        type = "bus"
    elif x == "T":
        type = "tram"
    elif x == "M":
        type = "metro"
    else:
        pass

    import csv
    with open('resources/ret_met_type.csv', 'rb') as f:
        regel = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        csvinfo = []
        for row in regel:
            if x in ("B","T","M"):
                if row[1] == type:
                    row[3] = row[3].replace(",", ".")
                    row[4] = row[4].replace(",", ".")
                    rij=(row[0], row [1], row[2], row[3], row[4])
                    csvinfo.append(rij)
            else:
                row[3] = row[3].replace(",", ".")
                row[4] = row[4].replace(",", ".")
                rij=(row[0], row [1], row[2], row[3], row[4])
                csvinfo.append(rij)
        return csvinfo