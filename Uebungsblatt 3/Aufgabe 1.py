# a) Betrachten Sie die Liste [’H’, ’P’, ’E’, ’E’, ’L’, ’T’, ’L’, ’E’, ’O’, ’R’]. Diese
# Liste enthält die Worte ’Hello’ und ’Peter’ in vermischter Form. Speichern Sie die ursprüng-
# lichen Worte unter Verwendung von List comprehension in zwei Listen ([’H’, ’E’, ’L’, ’L’,
# ’O’] und [’P’, ’E’, ’T’, ’E’, ’R’]) ab.
# Tipp: Verwenden Sie die enumerate()-Funktion
# b) Stellen Sie sich eine Stückliste vor, die zu jedem Produkt die folgenden Informationen auf-
# listet: Position, Teilenummer, Bezeichnung, Menge und Einheit. Extrahieren Sie aus einer
# Liste von Tupeln mit allen aufgelisteten Informationen die Bezeichnungen aller Produkte.
# Verwenden Sie hierzu List comprehension.
# Beispiel: Aus der Liste parts = [(1, ’500-1’, ’Hammer’, 2, ’Pieces’), (2, ’503’,
# ’Screwdriver’, 3, ’Pieces’)] soll die Liste [’Hammer’, ’Screwdriver’] extrahiert wer-
# den.

list = ['H', 'P', 'E', 'E', 'L', 'T', 'L', 'E', 'O', 'R']                                           # Liste definieren

hello = [char for i, char in enumerate(list) if i in [0, 2, 4, 6, 8]]                               # hello als list-comprehension definieren, indexieren und Hello definieren
peter = [char for i, char in enumerate(list) if i in [1, 3, 5, 7, 9]]                               # peter als list-comprehension definieren, indexieren und Peter definieren


for i, char in enumerate(list):                                                                     # Index und zugehörigen Char ausgeben
    print(f"Index: {i} Char: {char}")                                                               # Ausgabe

print(f"Hello: {hello}")                                                                            # Ausgabe des Wortes Hello  
print(f"Peter: {peter}")                                                                            # Ausgabe des Wortes Peter

parts = [(1, '500-1', 'Hammer', 2, 'Pieces'), (2, '503', 'Screwdriver', 3, 'Pieces')]               # Liste Parts definieren
bezeichnungen = [bezeichnung for _, _, bezeichnung, _, _ in parts]                                  # Namen extrahieren   _, _, bezeichnung, _, _    

print(f"Bezeichnungen: {bezeichnungen}")                                                            # Ausgabe der Bezeichnung