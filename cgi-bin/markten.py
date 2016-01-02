## markten.py
## wat doet deze script:
## Ontvangt van buiten een parameter voor de opgevraagde dagen, in de vorm van een tuple.
## Deze heeft een vaste volgorde voor de dagen, begint met maandag:
## als er nul staat, wordt dit gelezen als "info niet gevraagd", als er 1 staat dan is dat wel het geval.
## Deze parameter is input voor de functie markten.
## In deze functie wordt eerst het csv-bestand mbv een for-loop in een interne list bewaard, zie csvinfo[x]=(rij).
## Daarna wordt de adresinformatie, afh vd parameter, in een andere list gezet (marktadres) om deze terug te voeren
## naar de caller.
## Je kunt de hekjes bij de print-opdrachten weghalen om de werking van de code te zien.

import csv

def GetMarkten(week):
    with open('markten.csv', 'rb') as f:
        regel = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        # zorg er eerst voor dat de csv in een list wordt gelezen
        csvinfo = []
        #csvinfo = [ [ None for i in range(3) ] for j in range(20) ]  
		#hier 20 rijen geinitialiseerd, is dit per se nodig, wat als je het aantal rijen niet weet?
		# MATHIJS: hoeft niet perse je kan zonder 20 rijen te initialiseren ook een item toevoegen aan een array met 'append' (zie hieronder)
		
        for row in regel:
            rij=(row[0], row [1], row[2])
            csvinfo.append(rij);

    #print
    #print csvinfo[0]
    #print csvinfo


    #daarna info uit tuple in een list of tuple zetten om deze als return waarde terug te geven

    marktenlist = []

    for x in range(0,len(week)):
        if week[x] == 1:
            print csvinfo[x][0] +","+ csvinfo[x][1]  #kolom3 = openingstijden weglatenop de website? niet interessant
            marktenlist.append(csvinfo[x])
        else:
            #print "indexnummer is: " , x , " hier dus niets printen of appenden"
            pass
    return marktenlist

## hieronder het deel waar de functie markten zal worden aangeroepen vanuit de caller
## week is een tuple die 7 dagen bevat, begint bij maandag: indien nul dan staat het vinkje kennelijk uit, anders aan.
#week = (0,1,0,0,0,1,1)      #hiermee wordt dus dinsdag, zaterdag en zondag opgevraagd
#print week
#marktadres = markten(week)
#print marktadres