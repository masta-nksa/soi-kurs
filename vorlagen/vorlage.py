"""Vorlage fuer SOI-Aufgaben (Gerueststufe 1).

Verwendung:
    python vorlage.py < bsp_ein.txt > mein_aus.txt
"""

import sys

# ---------------------------------------------------------------
# Einlesen - das ist fertig, du musst hier nichts aendern.
# ---------------------------------------------------------------

_tokens = sys.stdin.read().split()
_pos = 0


def zahl():
    """Liest die naechste Zahl."""
    global _pos
    _pos += 1
    return int(_tokens[_pos - 1])


def zahlen(n):
    """Liest die naechsten n Zahlen als Liste."""
    return [zahl() for _ in range(n)]


def wort():
    """Liest das naechste Wort."""
    global _pos
    _pos += 1
    return _tokens[_pos - 1]


# ---------------------------------------------------------------
# Hier ist deine Aufgabe.
# ---------------------------------------------------------------

def loese(n, werte):
    # TODO: berechne das Ergebnis fuer einen Testfall
    return 0


# ---------------------------------------------------------------
# Hauptteil - Achtung: Case #i beginnt bei 0, nicht bei 1.
# ---------------------------------------------------------------

T = zahl()
for i in range(T):
    N = zahl()
    werte = zahlen(N)
    ergebnis = loese(N, werte)
    print(f"Case #{i}: {ergebnis}")
