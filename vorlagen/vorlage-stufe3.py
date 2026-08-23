"""Vorlage fuer SOI-Aufgaben (Gerueststufe 3, ab M5).

Starten: der Play-Knopf oben rechts in VS Code.

Neu gegenueber M3 und M4: Du bekommst keine Leser-Funktionen mehr und keinen
fertigen Hauptteil. Was bleibt, ist das Geruest - die Dateinamen, das Einlesen
der ganzen Datei in eine Wortliste und der Vergleich am Schluss.

Das ist Absicht. Im Wettbewerb ist das Einlesen Teil der Aufgabe, und das
Ausgabeformat ist die haeufigste Fehlerquelle ueberhaupt. Ab hier uebst du das
mit.
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
# Die ganze Datei als Liste von Woertern. Mehr bekommst du nicht.
# ---------------------------------------------------------------

with open(EINGABE, encoding="utf-8") as datei:
    tokens = datei.read().split()


# ---------------------------------------------------------------
# Ab hier schreibst du alles selbst.
# ---------------------------------------------------------------
#
# Eine Merkliste, damit nichts vergessen geht:
#
#   1. Ein Weg, das naechste Wort oder die naechste Zahl zu holen. Die
#      Leser-Funktionen aus vorlage-stufe2.py darfst du abschreiben - du
#      sollst sie kennen, nicht auswendig lernen.
#   2. Die Anzahl Testfaelle T steht als Erstes in der Datei.
#   3. Pro Testfall eine Ausgabezeile "Case #i: ..." - und "Case #i" ist
#      NULLBASIERT. Der erste Testfall ist Case #0.
#      Manche Aufgaben verlangen mehr als eine Zeile pro Testfall. Lies das
#      Ausgabeformat genau.
#   4. Alle Zeilen sammeln und am Schluss in einem Zug schreiben:
#          pruefe.schreibe(AUSGABE, zeilen)
#   5. Beim Testen mit dem Beispiel vergleichen:
#          if EINGABE == "bsp_ein.txt":
#              pruefe.vergleiche(ERWARTET, AUSGABE)
#
# print() bleibt frei fuer Debug-Ausgaben - es schreibt nichts in die
# Ausgabedatei.
