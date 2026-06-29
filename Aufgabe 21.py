# Erstellen Sie eine Klasse `Person` und ihre beiden Unterklassen: `Male` und `Female`. Alle Klassen haben eine Methode `getGender()`, die "Male" (String) für die Klasse `Male` und "Female" (String) für die Klasse `Female` ausgeben kann. 

# Verwenden Sie für die Polymorphie

class Person:                                         # Die Basisklasse anlegen
    def getGender(self):                              # Defintion der Funktion getGender für Unknown
        return "Unknown"                                
    
class Male(Person):                                   # Unterklasse Male anlegen
    def getGender(self):                              # Defintion der Funktion getGender für Male
        return "Male"

class Female(Person):                                 # Unterklasse Female anlegen
    def getGender(self):                              # Defintion der Funktion getGender für Female
        return "Female"

personen_liste = [Male(), Female(), Male(), Female()] # Liste mit Objekten erstellen


for p in personen_liste:                               # Aufrufen jedes Objektes ohne das Geschlecht zu wissen
    print(f"Diese Person ist: {p.getGender()}")        # Ausgabe der Personen und Geschlechter