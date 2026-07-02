# Erweitern Sie den Code zu geometrischen Formen des ersten
# Ubungsblattes. In dieser Aufgabe
# sollten Sie die Fläche von Grundstücken berechnen und auf dieser Basis den Brutto- und Netto-     
# preis ausgeben. Stellen Sie sich nun vor, dass dieses Programm in einer Stadtverwaltung für viele
# verschiedene Grundstücke eingesetzt werden soll. Erweitern Sie also Ihr Programm dahingehend,
# dass die Länge und Breite von einzelnen Grundstücken in einer Liste verwaltet werden. Lagern Sie
# außerdem die Berechnung der Netto- und Bruttopreise in Funktionen aus. Achten Sie hierbei auf
# sinnvolle Funktionssignaturen mit eventuellen Standardwerten der Parameter. Geben Sie dann mit
# Hilfe einer for-Schleife und den geschriebenen Funktionen den Brutto- und Nettopreis f¨ ur jedes
# Grundst¨ uck aus.
# Beispiel: Für die Liste properties = [(10, 10)], 1 Quadratmeterpreis und 10% Steuersatz
# soll das Ergbenis 110 herauskommen.

properties = [                                                                       # Liste der Grundstücksgrößen (Länge, Breite)
    (4, 3),                                                                           # Breite und Länge des ersten Grundstücks
    (10, 10),                                                                         # Breite und Länge des zweiten Grundstücks
    (8, 12)                                                                           # Breite und Länge des dritten Grundstücks
]
price_per_sqm = 50                                                                   # 50 Euro pro Quadratmeter
standard_tax = 0.035                                                                 # 3,5 % Steuersatz


def calculate_area(length: float, width: float) -> float:                            # Berechnung der Grundstücksfläche
    return length * width


def calculate_net_price(area: float, price: float = price_per_sqm) -> float:         # Berechnung des Nettopreises
    return area * price


def calculate_gross_price(net_price: float, tax_rate: float = standard_tax) -> float:  # Berechnung des Bruttopreises
    return net_price * (1 + tax_rate)


for idx, (length, width) in enumerate(properties, start=1):                             # Schleife über alle Grundstücke
    flaeche = calculate_area(length, width)
    netto = calculate_net_price(flaeche)
    brutto = calculate_gross_price(netto)

    print(f"Grundstück {idx}: Länge={length} m, Breite={width} m")
    print(f"  Fläche: {flaeche} m²")
    print(f"  Nettopreis: {netto:,.2f} EUR".replace('.', ','))
    print(f"  Bruttopreis: {brutto:,.2f} EUR".replace('.', ','))
