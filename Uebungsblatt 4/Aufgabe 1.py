# Betrachten Sie das Beispiel auf Folie 26 von Foliensatz 4 “Data Structures”. Hier wird demon-
# striert, dass das Suchen von 1000 zufälligen Zahlen in einer Liste von 100 000 Zahlen um mehrere
# Größenordnungen langsamer ist als in einem gleich großen Set. Erklärt werden kann dies mit der
# sogenannten Laufzeitkomplexität der darunterliegenden Suchalgorithmen. Während in einer Liste
# bei Verdopplung der Größe auch der Suchaufwand ca. doppelt so groß wird, steigt der Suchauf-
# wand in Sets nur in ca. log2-facher Beziehung an. In dieser Aufgabe sollen Sie den dazugehörigen
# Code selbst schreiben und Experimente damit durchführen.
#
# Dieses Skript erstellt zufällige Datenmengen als Liste und Set und misst jeweils die Suche von
# 1000 zufällig gezogenen Zahlen innerhalb des Intervalls [0, 10000000]. Danach werden die
# Messzeiten von Listen und Sets für verschiedene Containergrößen verglichen.

import random                                                          # Importiert das Modul für Zufallszahlen
import time                                                            # Importiert das Modul zum Messen der Zeit


def create_random_container(size: int, max_value: int) -> tuple[list[int], set[int]]:   # Deklariert eine Funktion, die Liste und Set erzeugt
    """Erstellt eine Liste und ein Set mit `size` eindeutigen Zufallszahlen."""         # Dokumentiert die Funktion
    values = random.sample(range(max_value + 1), size)                                  # Erzeugt `size` eindeutige Zufallszahlen
    return values, set(values)                                                          # Gibt Liste und Set zurück


def measure_search_time(container, queries: list[int]) -> float:                        # Deklariert eine Funktion zur Messung der Suchzeit
    """Misst die Zeit für `value in container` für alle Suchwerte."""                   # Dokumentiert die Funktion
    start = time.perf_counter()                                                         # Speichert den Startzeitpunkt
    for value in queries:                                                               # Iteriert über alle Suchwerte
        _ = value in container                                                          # Prüft das Vorhandensein des Wertes im Container
    return time.perf_counter() - start                                                  # Gibt die gemessene Dauer zurück


def run_experiment() -> None:                                                           # Deklariert die Hauptfunktion des Experiments
    random.seed(42)                                                                     # Setzt den Zufallszahlengenerator für reproduzierbare Ergebnisse
    max_value = 10_000_000                                                              # Legt das Suchintervall fest
    sample_sizes = [10_000, 100_000, 500_000, 1_000_000]                                # Definiert die Containergrößen
    queries = [random.randint(0, max_value) for _ in range(1000)]                       # Erzeugt 1000 zufällige Suchwerte

    print("Größe | Listensuche [s] | Setsuche [s] | Ratio List/Set")                    # Gibt die Tabellenüberschrift aus
    print("----- | ---------------- | ------------ | ---------------")                  # Gibt die Trennlinie aus

    for size in sample_sizes:                                                           # Schleife über die verschiedenen Containergrößen
        values_list, values_set = create_random_container(size, max_value)              # Erzeugt Liste und Set mit Zufallszahlen

        list_time = measure_search_time(values_list, queries)                           # Misst die Suchzeit in der Liste
        set_time = measure_search_time(values_set, queries)                             # Misst die Suchzeit im Set

        ratio = list_time / set_time if set_time > 0 else float("inf")                  # Berechnet das Verhältnis von Liste zu Set
        print(f"{size:>7} | {list_time:>14.6f} | {set_time:>12.6f} | {ratio:>15.2f}")   # Gibt die Ergebnisse formatiert aus

    print("\nErgebnis: Die Suche in Sets bleibt bei großen Datenmengen sehr schnell,\n"  
          "während das Durchsuchen von Listen deutlich langsamer wird.")                   # Ergebnisanzeige


if __name__ == "__main__":                                                              # Prüft, ob das Skript direkt ausgeführt wird
    run_experiment()                                                                    # Startet das Experiment
