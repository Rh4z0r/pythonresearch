# Betrachten Sie nochmals die Stückliste aus Aufgabe 1b) von
# Übungsblatt 3. Erweitern Sie die
# beispielhafte Stückliste um weitere Produkte. Schreiben Sie ein Programm, das Ihnen auf Basis
# der erweiterten Stückliste jede Artikelnummer auf die Menge und Einheit des jeweiligen Produktes
# abbildet.
# Beispiel: Aus der Liste parts = [(1, '500-1', 'Hammer', 2, 'Pieces'), (2, '503', 'Screw-
# driver', 3, 'Pieces'), (3, '555', 'Nail', 10, 'Pieces')] soll das Dictionary invento-
# ry = {'500-1': (2, 'Pieces'), '503': (3, 'Pieces'), '555': (10, 'Pieces')} erzeugt wer-
# den.

parts = [(1, '500-1', 'Hammer', 2, 'Pieces'), (2, '503', 'Screwdriver', 3, 'Pieces')]                     # Liste Parts definieren
inventory = {part[1]: (part[3], part[4]) for part in parts}                                               # Dictionary mit Artikelnummer als Schlüssel und Menge/Einheit als Wert erstellen
print(f"Inventory: {inventory}")                                                                          # Ausgabe des Inventars    

