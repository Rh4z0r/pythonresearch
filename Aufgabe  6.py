# Gegeben ist:

# passwords = [
#     "abc",
#     "Passwort1",
#     "Hallo",
#     "Python2025",
#     "Test"
# ]

# Erstellen Sie mit einer List Comprehension eine neue Liste, die nur Passwörter mit mindestens 8 Zeichen enthält.

passwords = [                                                                                       # Definition der Passwortliste
    "abc",
    "Passwort1",
    "Hallo",
    "Python2025",
    "Test"
]
neue_passwoerter = [x for x in passwords if len(x) >= 8]                                             # Condition für die Mindestzeichen

print(neue_passwoerter)                                                                              # Ausgabe der gültigen Passwörter
