"""Hilfsfunktionen zum Schreiben und Pruefen der Ausgabedatei.

Diese Datei aenderst du nicht und startest du nicht. Sie wird von loesung.py
benutzt und muss nur im selben Ordner liegen.
"""


def schreibe(pfad, zeilen):
    """Schreibt die Ergebniszeilen in die Ausgabedatei."""
    # newline="\n" erzwingt einfache Zeilenumbrueche. Windows schreibt sonst
    # zwei Zeichen pro Zeilenende, und der Grader stolpert darueber.
    with open(pfad, "w", encoding="utf-8", newline="\n") as datei:
        for zeile in zeilen:
            datei.write(zeile + "\n")

    print(pfad + " geschrieben (" + str(len(zeilen)) + " Zeilen).")


def lies_zeilen(pfad):
    """Liest eine Datei als Liste von Zeilen, ohne Leerraum am Ende."""
    with open(pfad, encoding="utf-8") as datei:
        inhalt = datei.read()

    zeilen = []
    for zeile in inhalt.splitlines():
        zeilen.append(zeile.rstrip())

    # Leere Zeilen am Dateiende zaehlen nicht als Unterschied.
    while len(zeilen) > 0 and zeilen[-1] == "":
        zeilen.pop()

    return zeilen


def vergleiche(erwartet_pfad, meine_pfad):
    """Vergleicht die Ausgabe mit der erwarteten Ausgabe, Zeile fuer Zeile."""
    try:
        erwartet = lies_zeilen(erwartet_pfad)
    except FileNotFoundError:
        print("Die Datei " + erwartet_pfad + " fehlt - kein Vergleich moeglich.")
        return False

    meine = lies_zeilen(meine_pfad)

    fehler = 0
    anzahl = max(len(erwartet), len(meine))

    for i in range(anzahl):
        if i < len(erwartet):
            eine_erwartete = erwartet[i]
        else:
            eine_erwartete = "<fehlt>"

        if i < len(meine):
            eine_meine = meine[i]
        else:
            eine_meine = "<fehlt>"

        if eine_erwartete != eine_meine:
            fehler = fehler + 1
            if fehler <= 5:
                print("Zeile " + str(i + 1) + ":")
                print("  erwartet: " + eine_erwartete)
                print("  deine:    " + eine_meine)

    if fehler == 0:
        print("Alles richtig (" + str(len(erwartet)) + " Zeilen).")
        print("Du kannst jetzt die echte Eingabe herunterladen.")
        return True

    print("")
    print(str(fehler) + " Zeile(n) unterschiedlich.")

    if len(erwartet) != len(meine):
        print("Zeilenzahl: erwartet " + str(len(erwartet))
              + ", deine " + str(len(meine)) + ".")
        print("Tipp: Schreibst du fuer jeden Testfall genau eine Zeile?")

    return False
