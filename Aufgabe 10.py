# Schreiben Sie ein Programm, das alle Zahlen zwischen 2000 und 3200 (beide eingeschlossen) findet, die durch 7 teilbar sind, aber kein Vielfaches von 5 sind. Die gefundenen Zahlen sollen in einer durch Komma getrennten Sequenz in einer einzigen Zeile ausgegeben werden.

# Hinweise: Erwägen Sie die Verwendung der Methode `range(#begin, #end)`

list = []                                                           # leere Liste erstellen

for number in range(2000, 3201):                                    # Nummer 2000-3200 (bei 2000-3200 als Werte würde die Range nur bis 3199 gehen)
    if number % 7 == 0 and number % 5 != 0 :                        # Konditionen: Durch 7 teilbar aber kein vielfaches von fünf
        list.append(number)                                         # Nummer in Liste einfügern

print(", ".join(map(str, list)))                                    # Liste ausgeben


# Alternativcode zur direkten Ausgabe der Werte (ohne Liste)
#for number in range(2000, 3201): 
#   if number % 7 == 0 and number % 5 != 0 : 
#        print(number)