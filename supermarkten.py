## supermarkten.py
## geeft 5 kolommen in deze volgorde terug:
## (0) naam vd supermarkt,
## (1) straat incl huisnr,
## (2) poko,
## (3) latitude,
## (4) longitude


def GetSupermarkten():  #ontvangt geen parameter
    import csv
    with open('supermarkten.csv', 'rb') as f:
        regel = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        csvinfo = []
        csvinfo = [ [ None for i in range(5) ] for j in range(200) ]
        #print len(csvinfo)
        x = 0
        for row in regel:
            rij=(row[0], row [1], row[2], row[3], row[4])
            #print rij
            csvinfo[x]=(rij);
            x += 1
        return csvinfo