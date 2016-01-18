## ret.py
## geeft 5 kolommen in deze volgorde terug:
## (0) naam vd halte,
## (1) type halte,
## (2) detailoms halte,
## (3) latitude,
## (4) longitude
## verwachte parameter: B voor bus, T voor tram, M voor metro en leeg voor alles


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
    with open('ret_met_type.csv', 'rb') as f:
        regel = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        csvinfo = []
        for row in regel:
            if x in ("B","T","M"):
                if row[1] == type:
                    row[3] = row[3].replace(",", ".")
                    row[4] = row[4].replace(",", ".")
                    rij=(row[0], row [1], row[2], row[3], row[4])
                    #print rij
                    csvinfo.append(rij)
            else:
                row[3] = row[3].replace(",", ".")
                row[4] = row[4].replace(",", ".")
                rij=(row[0], row [1], row[2], row[3], row[4])
                #print rij
                csvinfo.append(rij)
        return csvinfo

#tabhalte = GetHalte("")
#print tabhalte.item
#count = 0
#for i in tabhalte:
    #count += 1
#print count