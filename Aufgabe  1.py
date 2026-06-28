# Schreiben Sie ein Programm, das den Benutzer so lange nach einer Zahl fragt, bis eine ungerade Zahl eingegeben wird.

# Nach jeder gültigen Eingabe soll die Zahl ausgegeben werden.

# Falls die Eingabe keine Zahl ist, soll die Meldung: "Bitte geben Sie eine Zahl ein" erscheinen und die Eingabe wiederholt werden.

zahl = int(input("bitte gib eine Zahl ein, ich prüfe ob sie gerade oder ungerade ist:"))       # Variable für die erste Zahlenabfrage 
print(f"Die Zahl ist {zahl}.")                                                                 # Ausgabe der ersten Zahl 

while zahl % 2 == 0:                                                                           # while Schleife. Condition % 2 wird geprüft
    zahl = int(input("Die Zahl ist gerade. Bitte eine weitere Zahl eingeben:"))                # Überschreiben der Variablen durch durch einen neuen Input
    print(f"Die Zahl ist {zahl}.")                                                             # Ausgabe jeder weiteren Eingabe

print("Die eingegebene Zahl ist ungerade. Programm wird verlassen")                            # Ausgabe zum Programmende für ungerade Zahlen
       