"""Vorlage fuer SOI-Aufgaben (Gerueststufe 2, ab M3).

Starten: der Play-Knopf oben rechts in VS Code.

Neu gegenueber M0 bis M2: Das Einlesen eines Testfalls ist nicht mehr
vorgegeben. Die Werkzeuge dafuer bekommst du weiterhin fertig - das Muster
musst du selbst auf das Eingabeformat deiner Aufgabe uebertragen.
"""

import pruefe

# ---------------------------------------------------------------
# Dateien - hier stellst du um.
# ---------------------------------------------------------------

# Zum Testen mit dem Beispiel aus der Aufgabenstellung:
EINGABE = "bsp_ein.txt"
# Fuer die echte Runde diese Zeile verwenden:
# EINGABE = "input.txt"

AUSGABE = "output.txt"
ERWARTET = "bsp_aus.txt"


# ---------------------------------------------------------------
# Werkzeuge zum Einlesen - fertig, hier aenderst du nichts.
# ---------------------------------------------------------------

with open(EINGABE, encoding="utf-8") as datei:
    tokens = datei.read().split()

position = 0


def zahl():
    """Liest die naechste Zahl."""
    global position
    position = position + 1
    return int(tokens[position - 1])


def zahlen(anzahl):
    """Liest die naechsten Zahlen als Liste."""
    liste = []
    for i in range(anzahl):
        liste.append(zahl())
    return liste


def wort():
    """Liest das naechste Wort."""
    global position
    position = position + 1
    return tokens[position - 1]


# ---------------------------------------------------------------
# Hier ist deine Aufgabe.
# ---------------------------------------------------------------

def loese():
    # TODO: berechne das Ergebnis fuer einen Testfall
    return 0


# ---------------------------------------------------------------
# Hauptteil - hier ist die Luecke.
# ---------------------------------------------------------------
#
# Die Aufrufe muessen in derselben Reihenfolge stehen wie die Werte im
# Eingabeformat der Aufgabe. Fuer das Format
#
#     T
#     N                    <- erste Zeile eines Testfalls
#     p_0 p_1 ... p_N-1    <- zweite Zeile
#
# sieht der Rumpf so aus:
#
#     N = zahl()
#     p = zahlen(N)
#     ergebnis = loese(N, p)
#
# Stehen zwei Werte auf einer Zeile, etwa "N K", dann sind das einfach
# zwei Aufrufe von zahl() nacheinander. Ob Werte auf derselben Zeile oder
# auf verschiedenen stehen, spielt keine Rolle - die Werkzeuge oben
# zerlegen die ganze Datei in Woerter.

T = zahl()

zeilen = []
for i in range(T):
    # TODO: lies die Werte dieses Testfalls ein und ruf loese damit auf
    ergebnis = loese()
    zeilen.append("Case #" + str(i) + ": " + str(ergebnis))

pruefe.schreibe(AUSGABE, zeilen)

# Beim Testen vergleichen wir gleich mit der erwarteten Ausgabe.
if EINGABE == "bsp_ein.txt":
    pruefe.vergleiche(ERWARTET, AUSGABE)
