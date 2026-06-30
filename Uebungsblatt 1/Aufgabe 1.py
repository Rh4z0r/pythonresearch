#    a) Nehmen wir an, wir haben ein Rechteck mit einer Länge von 4 m und einer Breite von 3 m.
#       Berechnen Sie die Fläche dieses Rechtecks auf möglichst naive Weise in Python.
#    b) Verwenden Sie Variablen mit aussagekräftigen Namen, um Ihre Berechnung verständlicher
#       zu machen.
#    c) Stellen Sie sich das Rechteck als ein Grundstück vor, das Sie kaufen möchten. Die Stadtver-
#       waltung hat den Preis pro Quadratmeter auf 50 festgelegt. Auf diese Käufe ist eine Steuer
#       von 3,5% zu entrichten. Berechnen Sie den Netto- und Bruttopreis, den Sie zahlen müssten,
#       und informieren Sie den Nutzer über die Zusammensetzung des Bruttopreises.

length = 4                                                                              # länge festlegen
width = 3                                                                               # breite festlegen
price = 50                                                                              # 50 Euro Quadratmeterpreis
tax = 0.035                                                                             # Steuersatz


flaeche = length * width                                                                # Flächenberechnung durchführen
netto = flaeche * price                                                                 # Preisberechnung durchführen
brutto = netto * (1+tax)                                                                # Brutto berechnen

print(f"Die Fläche beträgt {flaeche} cm²")                                              # Ausgabe des Ergebnisses der Flächenberechnung
print(f"Der Nettopreis beträgt {netto:,.2f} EUR".replace(".", ","))                     # Ausgabe des Nettopreises (erzwingen von 2 Nachkomma-Stellen und ersetzen des Punktes durch ,)
print(f"Der bruttopreis beträgt {brutto:,.2f} EUR".replace(".", ","))                   # Ausgabe des Bruttopreises (erzwingen von 2 Nachkomma-Stellen und ersetzen des Punktes durch ,)