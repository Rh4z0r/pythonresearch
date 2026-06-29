# Erstellen Sie eine Klasse namens `Circle`, die durch einen Radius konstruiert werden kann. 
# Die Klasse Circle hat eine Methode names `area()`, mit der die Fläche des Kreises berechnet werden kann.

import math                                                                                 # Bibliothek math importieren

rad = int(input("Bitte geben sie den Radius des Kreises in cm ein: "))

class Circle:                                                                               # Erstellen der Klasse
    def __init__(self, radius):                                                             # Definition der Klasse
        self.radius = radius                                                                # Speichern des Wertes im Objekt

    def area(self):                                                                         # Definition der Area
        return math.pi * (self.radius ** 2)                                                 # Rechenoperation 

mein_kreis = Circle(rad)                                                                    # Eingegebener Kreisradius
print(f"Die Fläche des Kreises beträgt (qcm): {mein_kreis.area():.2f}")                     # Ausgabe der Fläche