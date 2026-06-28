# Schreiben Sie ein Programm, das bei einer gegebenen ganzzahligen Zahl $n$ ein Dictionary erzeugt, das (i, i*i) so enthält, dass es eine ganzzahlige Zahl zwischen 1 und $n$ ist (beide eingeschlossen). Anschließend soll das Programm das Dictionary ausgeben. 

# Angenommen, das Programm erhält die folgende Eingabe: `8`, dann sollte die Ausgabe lauten: `{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}`

number = int(input("Bitte geben Sie eine Zahl ein. Ich erstelle daraus ein Dictionary mit der Anzahl an x² Multiplikationen und den zugehörigen Ergebnissen. Als Beispiel 8 führt zu einer Range von 1² bis 8²: "))             #User-Input erfragen

quadrat_dict = {}                                               # Erzeugen des Dictionaries

for i in range(1, number + 1):                                  # for-Schleife mit der Range von 1 bis Eingabe + 1
    quadrat_dict[i] = i * i                                     # Quadrieren 
print(quadrat_dict)                                             # Ausgabe der Ergebnisse