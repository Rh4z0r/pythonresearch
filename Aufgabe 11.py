# Schreiben Sie eine Funktion

# fak(number)


# die die Fakultät einer gegebenen Zahl berechnet und zurückgibt. 

def fak(number):                                                                                                    # Definition der Funktion fak(number)
    ergebnis = 1                                                                                                    # Ergebnisdefinition (kleinster Wert ist 1x1=1)
    for i in range(1, number + 1):                                                                                  # for-Schleife überprüft die Bandbreite von Zahl 1 bis Eingabe +1 
        ergebnis *= i                                                                                               # Berechnung des Ergebnisses mit der Variablen i
    return ergebnis                                                                                                 # Rückgabe des Ergebnissen

entry = int(input("Bitte geben Sie eine Zahl ein und ich erreichne daraus die Fakulät: "))                          # Nutzereingabe der Zahl erfragen

print(f"Die Fakultät von {entry} ist: {fak(entry)}")                                                                # Ausgabe des Ergebnisses