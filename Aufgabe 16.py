# Gegeben sind alle Filme in denen Georg Clooney mitspielt (Quelle Wikipedia):

#`["Title", "Grizzly II: Revenge", "Return to Horror High", "Return of the Ki#ller Tomatoes", "Red Surf, Unbecoming Age", "The Harvest", "From Dusk till Dawn", "One Fine Day, Batman & Robin", "The Peacemaker", "The Thin Red Line", "Out of Sight", "Waiting for Woody", "Three Kings", "The Book That Wrote Itself", "South Park: Bigger, Longer & Uncut", "The Perfect Storm"," O Brother", "Where Art Thou?", "Ocean's Eleven", "Spy Kids", "Confessions of a Dangerous Mind", "Solaris", "Welcome to Collinwood", "Spy Kids 3-D: Game Over", "Intolerable Cruelty", "Ocean's Twelve", "Good Night", "and Good Luck", "Syriana", "The Good German", "Michael Clayton", "Ocean's Thirteen", "Sand and Sorrow", "Darfur Now", "Leatherheads", "Burn After Reading", "Fantastic Mr. Fox", "The Men Who Stare at Goats", "Up in the Air", "The American", "The Ides of March", "The Descendants", "Gravity", "The Monuments Men", "Annie", "Tomorrowland", "Hail, Caesar!", "Money Monster", "The Midnight Sky", "Ticket to Paradise"]`

# Bearbeiten Sie folgende Teilaufgaben:
# - Geben Sie die ersten drei Filme der Liste aus.
# - Geben Sie die letzten drei Filme der Liste aus. 
# - Sortieren Sie Liste alphabetisch
# - Geben Sie den ersten Film der alphabetischen Liste aus
# - Geben Sie die letzten drei und ersten drei der Liste aus (eine Anweisung verwenden)
# - Geben Sie alle Filme aus, ausser den letzten drei und ersten drei der Liste (eine Anweisung verwenden)

liste = [                                                                                                                                   # Definieren der Liste
    "Title", "Grizzly II: Revenge", "Return to Horror High", 
    "Return of the Killer Tomatoes", "Red Surf, Unbecoming Age", 
    "The Harvest", "From Dusk till Dawn", "One Fine Day, Batman & Robin", 
    "The Peacemaker", "The Thin Red Line", "Out of Sight", "Waiting for Woody", 
    "Three Kings", "The Book That Wrote Itself", "South Park: Bigger, Longer & Uncut", 
    "The Perfect Storm"," O Brother", "Where Art Thou?", "Ocean's Eleven", "Spy Kids", 
    "Confessions of a Dangerous Mind", "Solaris", "Welcome to Collinwood", "Spy Kids 3-D: Game Over", 
    "Intolerable Cruelty", "Ocean's Twelve", "Good Night", "and Good Luck", "Syriana", "The Good German", 
    "Michael Clayton", "Ocean's Thirteen", "Sand and Sorrow", "Darfur Now", "Leatherheads", "Burn After Reading", 
    "Fantastic Mr. Fox", "The Men Who Stare at Goats", "Up in the Air", "The American", "The Ides of March", 
    "The Descendants", "Gravity", "The Monuments Men", "Annie", "Tomorrowland", "Hail, Caesar!", "Money Monster", 
    "The Midnight Sky", "Ticket to Paradise"]

def sort_names(liste):                                                                                                                      # Defintion der Funktion
    return sorted(liste)                                                                                                                    # Sprung zum Hauptprogramm

sorted_list = sort_names(liste)                                                                                                             # Sortierte Liste

print(f"Orginal-Liste: {liste}")                                                                                                            # Gibt die Orginal-Liste aus
print("-" * 37)                                                                                                                             # Trennzeichen
print(f"Alphabetisch sortiert: {sorted_list}")                                                                                              # Gibt die alphabetisch sortierte Liste aus
print("-" * 37)                                                                                                                             # Trennzeichen   
print(f"{liste[:3]} sind die ersten 3")                                                                                                     # Gibt die ersten 3 Werte der Liste aus
print("-" * 37)                                                                                                                             # Trennzeichen   
print(f"{liste[-3:]} sind die letzten 3")                                                                                                   # Gibt die letzten 3 Werte der Liste aus
print("-" * 37)                                                                                                                             # Trennzeichen   
print(f"Alphabetisch sortiert, der erste: {sorted_list[:1]}")                                                                               # Gibt den ersten Wert der sortierten Liste aus
print("-" * 37)                                                                                                                             # Trennzeichen   
print(f"Alphabetisch sortiert, die letzten 3: {sorted_list[-3:]} und Alphabetisch sortiert, die ersten 3: {sorted_list[:3]}")               # Gibt die ersten und letzten 3 Werte der sortierten Liste aus
print("-" * 37)                                                                                                                             # Trennzeichen   
print(f"Alphabetisch sortiert, ohne die ersten und letzten 3: {sorted_list[3:-3]}")                                                         # Gibt die sortierte Liste ohne die ersten und letzten 3 Werte aus