# Ein Sensor liefert folgende Messwerte:

# values = [21, 22, 23, -999, 20, 19, -999, 18]

# Der Wert -999 kennzeichnet einen Messfehler.

# Schreiben Sie die Funktion

# getMaxValue(values)

# , die alle fehlerhaften Werte entfernt und eine neue Liste zurückgibt.

values = [21, 22, 23, -999, 20, 19, -999, 18]    # Messwerte

def getMaxValue(values):                         # Funktion GetMaxValue definieren
    valid = []                                   # leere Liste erstellen
    for v in values:                             # for Schleife
        if v > 0:                                # prüft auf negative Werte
            valid.append(v)                      # Werte in Liste schreiben
    return valid                                 # Rücksprung schließt die Liste
clean = getMaxValue(values)                      # neue Variablen
print(clean)                                     # Ausgabe neue Variablen