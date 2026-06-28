# Gegeben ist folgende Liste:

# names = [
#    "Liam", "Olivia", "Noah", "Charlotte",
#    "Oliver", "Emma", "Theodore", "Amelia",
#    "Henry", "Sophia", "James", "Mia",
#    "Elijah", "Isabella", "Mateo", "Evelyn",
#    "William", "Sofia", "Lucas", "Eliana"
# ]

# Schreiben Sie eine Funktion

# sort_names(names)

# die die Liste alphabetisch sortiert zurückgibt.

names = [                                                                               # Deklaration der Liste
    "Liam", "Olivia", "Noah", "Charlotte",
    "Oliver", "Emma", "Theodore", "Amelia",
    "Henry", "Sophia", "James", "Mia",
    "Elijah", "Isabella", "Mateo", "Evelyn",
    "William", "Sofia", "Lucas", "Eliana"
]

def sort_names(names):                                                                  # Erstellen der Funktion sort_names zur Namenssortierung 
    return sorted(names)                                                                # Return zum Hauptprogramm

sorted_list = sort_names(names)                                                         # Deklarierung der sortierten Liste

print(f"Orginal: {names}")                                                              # Ausgabe der Orginalliste
print(f"Sortierte Liste: {sorted_list}")                                                # Ausgabe der sortierten Liste
