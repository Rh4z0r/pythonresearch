# Schreiben Sie eine Funktion

# is_palindrome(text)

# die überprüft, ob ein Wort vorwärts und rückwärts identisch ist.

# Beispiele:

# otto -> True

# lagerregal -> True

# python -> False

def is_palindrome(text):                                                                                        # Definition der Funktion is_palindrome
    text = text.lower()                                                                                         # Wort in Kleinbuchstaben formatieren
    return text == text[::-1]                                                                                   # Wort Rückwärts = Wort Vorwärts

wort = input("Bitte geben Sie ein Wort ein und ich überprüfe ob es ein Palindrom ist: ")                        # Nutzereingabe erfragen

ist_palindrom = is_palindrome(wort)                                                                             # Variable für positives Ergebnis definieren

if ist_palindrom:                                                                                               # Wenn die Bedingung gegeben ist
    print(f"Das Wort {wort} ist ein Palindrom")                                                                 # Ausgabe
else:                                                                                                           # Wenn die Bedingung nicht gegeben ist
    print(f"Das Wort {wort} ist kein Palindrom.")                                                               # Ausgabe
    
    
