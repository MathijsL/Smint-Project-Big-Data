
def markten(week):
    import csv
    with open('markten.csv', 'rb') as f:
        regel = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        # zorg er eerst voor dat de csv in een list wordt gelezen
        csvinfo = []
        csvinfo = [ [ None for i in range(3) ] for j in range(20) ]
        print len(csvinfo)
        x = 0
        for row in regel:
            rij=(row[0], row [1], row[2])
            #print rij
            csvinfo[x]=(rij);
            x += 1

    print
    print csvinfo[0]
    print csvinfo


    #daarna info uit tuple in een list of tuple zetten om deze als return waarde terug te geven
    for x in range(0,len(week)):
        if week[x] == 1:
            print csvinfo[x]
        else:
            print "indexnummer is: " , x , " hier dus niets printen of appenden"

#week is een tuple die 7 dagen bevat, begint bij maandag: indien nul dan staat het vinkje kennelijk uit, anders aan.
week = (0,1,0,0,0,0,0)      #hiermee wordt dus alleen dinsdag opgevraagd
print week
markten(week)