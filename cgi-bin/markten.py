## markten.py
## wat doet deze script:
## Ontvangt van buiten een parameter voor de opgevraagde dagen, in de vorm van een lijst.
## Deze heeft een vaste volgorde voor de dagen, begint met maandag:
## als er nul staat, wordt dit gelezen als "info niet gevraagd", als er 1 staat dan is dat wel het geval.
## Deze parameter is input voor de functie GetMarkten.
## In deze functie wordt eerst het csv-bestand mbv een for-loop in een interne list bewaard, zie csvinfo[x]=(rij).
## Daarna wordt de adresinformatie, afh vd parameter, in een andere list gezet (marktadres) om deze terug te voeren
## naar de caller.
## Je kunt de hekjes bij de print-opdrachten weghalen om de werking van de code te zien.

import csv

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

            rij=(dagnr,row[0], row [1], row[2])
            csvinfo.append(rij)


    marktenlist = []

    for x in range(len(week)):
        if week[x] == 1:
            #print "dagnr is aan: ", x
            for i in range(0,len(csvinfo)):
                if csvinfo[i][0] == x:
                    print str(csvinfo[i][0]) + "," + csvinfo[i][1] + "," + csvinfo[i][2]
                    marktenlist.append(csvinfo[i])
    #print marktenlist
    return marktenlist

#test:
#GetMarkten([0,0,0,1,0,0,0])