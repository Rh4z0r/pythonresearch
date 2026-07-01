# Berechnen Sie einfache Statistiken auf einer Liste von Ganzzahlen. Schreiben Sie dazu ein Pro-
# gramm, das den User so lange Ganzzahlen eingeben lässt, bis dieser ”stop” eingibt. Die eingegebe-
# nen Zahlen sollen dabei in einer Liste gespeichert werden. Berechnen Sie dann unter Verwendung
# einer for-Schleife die folgenden Statistiken auf dieser Liste:
# Minimum
# Maximum
# Mittelwert
# Beispiel: Die Ergebnisse für die eingegebene Sequenz 3, 7, 2, ’stop’ sollten wie folgt sein:
# Minimum → 2, Maximum → 7, Mittelwert → 4

numbers = []                                                                                                # Liste numbers anlegen
while True:                                                                                                 # while Schleife starten
    user_input = input("Geben Sie eine Ganzzahl ein (oder 'stop' zum Beenden): ")                           # Eingabeaufforderung für den Benutzer
    if user_input.lower() == 'stop':                                                                        # Abbruchbedingung für die Schleife
        break                                                                                               # Schleife beenden  
    try:                                                                                                    # Eingabe in Ganzzahl umwandeln und zur Liste hinzufügen
        number = int(user_input)                                                                            # Eingabe in Ganzzahl umwandeln
        numbers.append(number)                                                                              # Liste numbers um die eingegebene Zahl erweitern
    except ValueError:                                                                                      # Fehlerbehandlung für ungültige Eingaben
        print("Bitte geben Sie eine gültige Ganzzahl ein.")                                                 # Ausgabe einer Fehlermeldung bei ungültiger Eingabe
        
minimum = min(numbers)                                                                                      # Minimum der Liste berechnen
maximum = max(numbers)                                                                                      # Maximum der Liste berechnen
mean = sum(numbers) / len(numbers)                                                                          # Mittelwert der Liste berechnen
mean = int(mean)                                                                                            # Mittelwert in Ganzzahl umwandeln

print(f"Minimum: {minimum}, Maximum: {maximum}, Mittelwert: {mean}")                                        # Ausgabe der berechneten Statistiken
