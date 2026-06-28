# Der Benutzer gibt einen Satz (einzelner String) ein.

# Bestimmen Sie das Wort, das am häufigsten vorkommt.

# Groß- und Kleinschreibung sollen ignoriert werden.

import re
from collections import Counter

def haeufigstes_wort(satz):                                                              # Alles in einem Schritt: Finden, in Lowercase umwandeln und direkt zählen
    zaehler = Counter(re.findall(r'\w+', satz.lower()))
       return zaehler.most_common(1)[0][0] if zaehler else "Keine Wörter gefunden!"         # most_common(1) liefert eine Liste [(wort, anzahl)], wir nehmen das erste Element des ersten Tupels

# Testlauf
print(f"Das häufigste Wort ist: '{haeufigstes_wort('Das ist ein Test. Ein richtig guter Test ist das!')}'")