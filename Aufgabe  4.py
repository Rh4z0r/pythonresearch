# Gegeben ist:

# temps = [18, 21, 22, 18, 20, 21, 18, 19]

# Bestimmen Sie:

#- Minimum
#- Maximum
#- Durchschnitt

# ohne Verwendung von min(), max() oder statistics.


temps = [18, 21, 22, 18, 20, 21, 18, 19] #Temperaturliste


mintemp = temps[0]                          # Anlegen der Liste mintemp mit dem Startwert 0
maxtemp = temps[0]                          # Anlegen der Liste maxtemp mit dem Startwert 0
anzahl = 0                                  # Anlegen der Variablen anzahl
summe = 0                                   # Anlegen der Vasriablen summe

for t in temps:                             # for Schleife  
    if t < mintemp:                         # Vergleiche t mit mintemp
        mintemp = t                         # ersetze minimum falls Bedingung erfüllt

    elif t > maxtemp:                       # else if 2.Kondition vergleichen
        maxtemp = t                         # ersetze maximum falls Bedingung erfüllt

    summe += t                              # Summe aus allen geprüften t
    anzahl += 1                             # zählt bei jeder anzahl eins hoch 

durchschnitt = summe / anzahl               # Berechnung des Durchschnittswert

print(f"Minimum: {mintemp}")                # Ausgabe Minimaltemperatur
print(f"Maximum: {maxtemp}")                # Ausgabe Maximaltempertur
print(f"Durchschnitt: {durchschnitt}")      # Ausgabe Durschnittstemperatur