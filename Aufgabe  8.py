# Gegeben ist eine Einkaufsliste:

# shopping = {
#     "Milch": 2,
#     "Brot": 1,
#     "Äpfel": 6
# }

# Schreiben Sie ein Programm, dass den Benutzer bittet einen Produktnamen einzugeben.

# Falls das Produkt bereits existiert, soll die Menge um 1 erhöht werden.

# Andernfalls soll das Produkt neu angelegt werden.

shopping = {                                                                                                                # Anlegen des Dictionaries
    "Milch": 2, 
    "Brot": 1,
    "Äpfel": 6
}

produkt = input("Bitte geben Sie das entsprechende Produkt ein: ")                                                          # Produkteingabe erfragen    

if produkt in shopping:                                                                                                     # Prüfen ob Produkt in der Shopping Liste ist
    shopping[produkt] += 1                                                                                                  # Produktanzahl erhöhen
    print(f"Das Produkt '{produkt}' existiert bereits. Die Menge wurde erhöht auf {shopping[produkt]}.")                    # Ausgabe
else:   
    shopping[produkt] = 1                                                                                                   # Produkt vorhanden
    print(f"Das Produkt '{produkt}' wurde neu hinzugefügt.")                                                                # Ausgabe

print(f"Aktuelle Einkaufsliste: {shopping}")                                                                                # Ausgabe Gesamtliste    

