"""Vorlage fuer SOI-Aufgaben (Gerueststufe 1).

Starten: der Play-Knopf oben rechts in VS Code.

Das Programm liest die Eingabedatei, rechnet und schreibt das Ergebnis in die
Ausgabedatei. Beim Testen vergleicht es die Ausgabe gleich mit der erwarteten.
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
# Einlesen - das ist fertig, du musst hier nichts aendern.
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

def loese(n, werte):
    # TODO: berechne das Ergebnis fuer einen Testfall
    return 0


# ---------------------------------------------------------------
# Hauptteil - Achtung: Case #i beginnt bei 0, nicht bei 1.
# ---------------------------------------------------------------

zeilen = []

T = zahl()
for i in range(T):
    N = zahl()
    werte = zahlen(N)
    ergebnis = loese(N, werte)
    zeilen.append("Case #" + str(i) + ": " + str(ergebnis))

pruefe.schreibe(AUSGABE, zeilen)

# Beim Testen wissen wir, was herauskommen soll. In der echten Runde nicht -
# dann faellt der Vergleich weg.
if EINGABE == "bsp_ein.txt":
    pruefe.vergleiche(ERWARTET, AUSGABE)
