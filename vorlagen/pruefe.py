"""Vergleicht deine Ausgabe mit der erwarteten Ausgabe.

Verwendung:
    python loesung.py < bsp_ein.txt > mein_aus.txt
    python pruefe.py bsp_aus.txt mein_aus.txt
"""

import sys


def zeilen(pfad):
    with open(pfad, encoding="utf-8") as f:
        # Leerzeichen am Zeilenende und leere Zeilen am Schluss ignorieren
        rohe = [z.rstrip() for z in f.read().splitlines()]
    while rohe and rohe[-1] == "":
        rohe.pop()
    return rohe


def main():
    if len(sys.argv) != 3:
        print("Aufruf: python pruefe.py erwartet.txt meine.txt")
        return 2

    erwartet = zeilen(sys.argv[1])
    meine = zeilen(sys.argv[2])

    fehler = 0
    for i in range(max(len(erwartet), len(meine))):
        e = erwartet[i] if i < len(erwartet) else "<fehlt>"
        m = meine[i] if i < len(meine) else "<fehlt>"
        if e != m:
            fehler += 1
            if fehler <= 5:
                print(f"Zeile {i + 1}:")
                print(f"  erwartet: {e}")
                print(f"  deine:    {m}")

    if fehler == 0:
        print(f"Alles richtig ({len(erwartet)} Zeilen).")
        print("Du kannst jetzt die echte Eingabe herunterladen.")
        return 0

    print(f"\n{fehler} Zeile(n) unterschiedlich.")
    if len(erwartet) != len(meine):
        print(f"Zeilenzahl: erwartet {len(erwartet)}, deine {len(meine)}.")
        print("Tipp: Gibst du fuer jeden Testfall genau eine Zeile aus?")
    return 1


if __name__ == "__main__":
    sys.exit(main())
