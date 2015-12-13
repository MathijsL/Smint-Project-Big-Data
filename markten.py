import csv
with open('markten.csv', 'rb') as f:
    regel = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
    for row in regel:
        print row[0], row [1], row[2]

#vragen aan Mathijs:
#(1) op welke manier wil je de marktgegevens uitvragen? krijgen we een parameter door,
# bijv 0 voor alles, 1 voor maandag, 2 voor dinsdag etc en wat geven we dan terug? een tabel? een bestandje?

#(2) bovenstaande moet waarsch in een functie. Geldt dat ook voor de import-functie? hoe zorgen we ervoor dat
#het csv maar 1 wordt ingelezen en niet bij elke verandering van een vinkje. 



