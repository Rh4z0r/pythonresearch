#Was macht folgendes Programm?
#
#    data = [4, 7, 11, 1, 3,  15]
#
#    i, j = 0,0
#    while i < len(data):
#        if data[i] > 10:
#            j += 1
#        i += 1

#    print("Anzahl Werte größer 10: {}".format(j))

# Ersetze Sie die `while`-Schleife durch eine `for`-Schleife.

data = [4, 7, 11, 1, 3,  15]                                    # Werteliste

j = 0                                                           # Definition von j
for wert in data:                                               # for Schleife
    if wert > 10:                                               # Kondition für den 10er-Übergang
        j += 1                                                  # j um eins erhöhen
    print("Anzahl Werte größer 10: {}".format(j))               # Ausgabe