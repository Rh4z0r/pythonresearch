# Der Benutzer gibt einen Satz (einzelner String) ein.

# Bestimmen Sie das Wort, das am häufigsten vorkommt.

# Groß- und Kleinschreibung sollen ignoriert werden.

import re                                                                                                                 # Bibliothek für regulären Ausdruck importieren
from collections import Counter                                                                                           # Modul collections importieren      

def haeufigstes_wort(satz):                                                                                               # Funktion haefigstes_wort definieren
    zaehler = Counter(re.findall(r'\w+', satz.lower()))                                                                   # Mehrfache finden und in Kleinbuchstaben umwandeln 
    return zaehler.most_common(1)[0][0] if zaehler else "Keine Wörter gefunden!"                                          # most_common(1) liefert eine Liste [(wort, anzahl)], wir nehmen das erste Element des ersten Tupels

eingabe = input("Bitte geben sie einen Satz ein und ich bestimme das Wort, dass am häufigsten vorkommt:")                 # Stringeingabe erbitten (Input)
ergebnis = haeufigstes_wort(eingabe)                                                                                      # häufigstes Wort in Liste schreiben

print(f"Das häufigste Wort ist: '{ergebnis}'")                                                                            # Ergebnis printen.