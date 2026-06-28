# Simulieren Sie mit einem Programm 50 Würfelwürfe.

# Bestimmen Sie anschließend:

# - wie oft jede Augenzahl vorkam
# - welche Augenzahl am häufigsten vorkam

# Verwenden Sie ein Dictionary.


import random                                                                                                           # Random Funktion initialisieren
ergebnisse = {                                                                                                          # Liste  für Ergebnisse erstellen
    1: 0, 
    2: 0, 
    3: 0, 
    4: 0, 
    5: 0, 
    6: 0, 
}

for x in range(50):                                                                                                      # for Schleife Würfe
    wurf = random.randint(1, 6)                                                                                          # random Funktion wür die Würfe (immer +1) 
    ergebnisse[wurf] +=1                                                                                                 # schreiben der Ergebnisse in die Liste           
    print("---Ergebnisse der 50 Würfelwürfe---")                                                                         # String Ausgabe

for augenzahl, anzahl in ergebnisse.items():                                                                             # Berechnen der Augenzahl 
     print (f"Augenzahl {augenzahl} kam {anzahl} mal vor.")                                                              # Ausgabe der Augenzahl und Anzahl

     haeufigste_zahl = max(ergebnisse, key=ergebnisse.get)                                                               # häufigste Zahl
anzahl_der_haeufigsten = ergebnisse[haeufigste_zahl]                                

print("-" * 37)                                                                                                          # 37 mal "-" als Trenner
print(f" Am häufigsten kam die {haeufigste_zahl}! Sie wurde {anzahl_der_haeufigsten} mal gewürfelt. ")                   # Ausgabe des Ergebnisses