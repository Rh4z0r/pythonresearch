# Kinder und Hundeliebhaber stellen sich häufig die Frage, wie alt ihr Hund wohl waere, wenn er
# kein Hund, sondern ein Mensch wäre. Landläufig rechnet man Hundejahre in Menschenjahre um,
# indem man das Alter des Hundes mit 7 multipliziert. Je nach Hundegröße und Rasse sieht die
# Umrechnung jedoch etwas komplizierter aus, z.B.:
# Ein einjähriger Hund entspricht in etwa einem 14-jährigen Menschen.
# 2 Jahre eines Hundes entsprechen 22 Jahre eines Menschen.
# Ab dann entspricht ein Hundejahr jeweils 5 Menschenjahren.
# Schreiben Sie ein Programm, das das Alter eines Hundes erfragt und dann nach obiger Methode
# berechnet, welchem Alter in Menschenjahren dies entspricht.

try:                                                                                                                                      # Eingabevalidierung
    human = int(input("Bitte geben sie die gewünschte Anzahl an Menschenjahren ein. Ich werde sie dann in Hundejahre umrechnen: "))       # Abfrage Menschenjahre

    if human < 0:                                                                                                                         # Fehlermeldung bei negativer Zahl
        print("Bitte geben Sie eine gültige Zahl ein.")                                                                                   # Ausgabe der Fehlermeldung bei negativer Zahl 
    if human == 0:                                                                                                                        # Bei Eingabe 0 
        print("0 Menschenjahre entsprechen 0 Hundejahren")                                                                                # Ausgabe bei Zahl 0 
    elif human == 1:                                                                                                                      # Vergleich für 1 Menschenjahr
        print("1 Jahr entspricht genau 14 Hundejahren")                                                                                   # Ausgabe für 1 Menschenjahr
    elif human == 2:                                                                                                                      # Vergleich für 2 Menschenjahre
        print("2 Jahre entsprechen exakt 22 Hundejahren")                                                                                 # Ausgabe für 2 Menschenjahre
    else:                                                                                                                                 
        dogyears = ((human -2) * 5) + 22                                                                                                  # Vergleich für mehr als 2 Menschenjahre
        print(f"{human} Menschenjahre entsprechen ganz genau {dogyears} Hundejahren.")                                                    # Berechnung der Hundejahre
except:                                                                                                                                   # Eingabevalidierung
    print("Das war leider keine gültige Zahl. Bitte versuche es nochmal.")                                                                # Fehlermeldung bei Falscheingaben