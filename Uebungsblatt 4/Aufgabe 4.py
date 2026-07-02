# a) Erweitern Sie den Code am Ende des Foliensatzes 5 “Funktionen”. Bisher ist diese Funktion
# zur Erkennung von Palindromen abhängig von der Groß- und Kleinschreibung.
# 
# Ändern Sie
# Ihre Lösung soweit ab, dass Worte nun unabhängig von ihrer Groß- und Kleinschreibung als
# Palindrom erkannt werden.
# Beispiel: Sowohl “anna” als auch “Anna” sollen als Palindrom erkannt werden.
# b) Neben Ein-Wort-Palindromen gibt es auch Satzpalindrome. Bei diesen gilt jedoch die Be-
# sonderheit, dass Leerzeichen und Sonderzeichen ignoriert werden können. Erweitern Sie Ihre
# Funktion um die Funktionalität, auch Satzpalindrome erkennen zu können.
# Beispiel: “Ein Esel lese nie.” und “Oh, Cello voll Echo!” sind Satzpalindrome.

import string                                                                                                                   # Bibliothek String importieren


def normalize_text(text: str, ignore_non_alphanumeric: bool = False) -> str:                                                    # Funktion zum Normalisieren von Text
    """Bereitet Text für den Palindrom-Test vor."""                                                                             # Dokumentiert die Normalisierungsfunktion
    cleaned = text.lower()                                                                                                      # Wandelt den Text in Kleinbuchstaben um
    if ignore_non_alphanumeric:                                                                                                 # Prüft, ob Sonderzeichen entfernt werden sollen
        cleaned = ''.join(ch for ch in cleaned if ch.isalnum())                                                                   # Entfernt Nicht-Alphanumerische Zeichen
    return cleaned                                                                                                              # Gibt den bereinigten Text zurück


def is_palindrome(text: str, ignore_non_alphanumeric: bool = False) -> bool:                                                    # Funktion zur Palindromprüfung
    """Prüft, ob ein Text ein Palindrom ist."""                                                                                 # Dokumentiert die Palindromprüfung
    normalized = normalize_text(text, ignore_non_alphanumeric)                                                                  # Normalisiert den Eingabetext
    return normalized == normalized[::-1]                                                                                       # Vergleicht Text mit seiner Umkehrung


if __name__ == "__main__":                                                                                                      # Prüft, ob das Skript direkt ausgeführt wird
    tests = [                                                                                                                   # Liste der Testtexte
        "anna",                                                                                                                 # Ein einfaches Palindromwort
        "Anna",                                                                                                                 # Palindrom unabhängig von Groß-/Kleinschreibung
        "Ein Esel lese nie.",                                                                                                   # Satzpalindrom mit Leerzeichen und Punkt
        "Oh, Cello voll Echo!",                                                                                                 # Satzpalindrom mit Sonderzeichen
        "Test"                                                                                                                  # Nicht-Palindrom als Negativtest
    ]                                                                                                                           # Ende der Testliste

    for text in tests:                                                                                                          # Schleife über alle Testtexte
        result_word = is_palindrome(text, ignore_non_alphanumeric=False)                                                        # Prüft das Wortpalindrom
        result_sentence = is_palindrome(text, ignore_non_alphanumeric=True)                                                     # Prüft das Satzpalindrom
        print(f'Original: {text}')                                                                                              # Gibt das Original aus
        print(f'  Wortpalindrom (case-insensitive): {result_word}')                                                             # Gibt das Wortpalindrom-Ergebnis aus
        print(f'  Satzpalindrom (ignoriere Leer- und Sonderzeichen): {result_sentence}')                                        # Gibt das Satzpalindrom-Ergebnis aus
        print()                                                                                                                 # Fügt eine Leerzeile zur Ausgabeformatierung hinzu
