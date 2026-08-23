# M5 — Musterlösungen

Diese Seite verrät die Lösung. Hast du es wirklich selbst versucht?

---

## Sushi, Teilaufgabe 2 und 4

Ein Programm für beide. Teilaufgabe 2 ist der Sonderfall S = 0.

### Der Gedankengang

Von jedem Paar zahlst du das teurere Stück. Die Gesamtrechnung ist also

```
Summe aller Preise  −  Summe der geschenkten Stücke  +  S pro gebildetem Paar
```

Du willst die geschenkten Stücke möglichst teuer machen. Sortierst du absteigend
und paarst die Nachbarn, ist das geschenkte Stück jedes Paars das
teuerstmögliche: Das zweitteuerste Stück überhaupt kann nirgends geschenkt
werden, wo es teurer wäre.

Bei S > 0 kommt eine Bedingung dazu. Ein Paar aus den Preisen a ≥ b kostet
`S + a` statt `a + b`. Es lohnt sich also genau dann, wenn `b > S` — wenn das
**billigere** Stück mehr kostet als die Flasche Sake.

Weil die Liste absteigend sortiert ist, gilt: Sobald sich ein Paar nicht mehr
lohnt, lohnt sich auch keines der folgenden. Alles danach kaufst du einzeln.

### Das Programm

```python
import pruefe

EINGABE = "bsp_ein.txt"
# EINGABE = "input.txt"
AUSGABE = "output.txt"
ERWARTET = "bsp_aus.txt"

with open(EINGABE, encoding="utf-8") as datei:
    tokens = datei.read().split()

position = 0


def zahl():
    global position
    position = position + 1
    return int(tokens[position - 1])


def loese(n, s, preise):
    preise.sort(reverse=True)
    gesamt = 0
    i = 0
    while i < n:
        # Paaren lohnt sich, wenn das billigere Stueck mehr kostet als der Sake.
        if i + 1 < n and preise[i + 1] > s:
            gesamt = gesamt + s + preise[i]
            i = i + 2
        else:
            gesamt = gesamt + preise[i]
            i = i + 1
    return gesamt


zeilen = []

T = zahl()
for fall in range(T):
    N = zahl()
    S = zahl()
    preise = []
    for k in range(N):
        preise.append(zahl())
    ergebnis = loese(N, S, preise)
    zeilen.append("Case #" + str(fall) + ": " + str(ergebnis))

pruefe.schreibe(AUSGABE, zeilen)

if EINGABE == "bsp_ein.txt":
    pruefe.vergleiche(ERWARTET, AUSGABE)
```

### Warum das Paaren von Nachbarn optimal ist

Die Frage ist berechtigt: Warum nicht das teuerste mit dem billigsten paaren?

Angenommen, in einer besten Lösung sind zwei Paare so gebildet, dass ein
teureres Stück mit einem billigeren zusammenliegt und umgekehrt — also die Preise
a ≥ b ≥ c ≥ d als Paare (a, d) und (b, c). Geschenkt sind dann d und c.

Tauschst du zu (a, b) und (c, d), sind b und d geschenkt. Da b ≥ c ist, ist die
Summe der geschenkten Stücke nicht kleiner geworden. Solche Tausche kann man
wiederholen, bis alle Paare aus Nachbarn bestehen — die Lösung wird dabei nie
schlechter.

Das ist ein **Vertauschungsargument** und die übliche Art, eine gierige Lösung zu
begründen.

### Laufzeit

Sortieren O(N log N), danach ein Durchgang O(N). Bei N = 10⁴ und T = 100 sind
das rund 10⁷ Schritte — Sekundenbruchteil.

Die naive Lösung, die N-mal das teuerste verbliebene Stück sucht, ist O(N²) und
landet bei 10¹⁰. Sie hätte bei Teilaufgabe 2 mit N ≤ 10³ noch gereicht (10⁸), bei
Teilaufgabe 4 nicht mehr.

!!! note "Die naive Lösung ist Selection Sort"
    „Suche das grösste Element, nimm es heraus, wiederhole" — das ist genau der
    Ablauf von Selection Sort, nur ohne dass man es Sortieren nennt. Wer
    Teilaufgabe 2 so gelöst hat, hat ein Sortierverfahren von Hand
    nachprogrammiert und dafür O(N²) bezahlt.

    Mehr dazu unter [Sortierverfahren](../hintergrund/sortierverfahren.md).

---

## Thermalquellen, Teilaufgabe 1

### Der Gedankengang

Die entscheidende Beobachtung steht in der Aufgabenstellung, man muss sie nur
umdrehen: Entlang einer gültigen Reihenfolge **steigt die Temperatur strikt**.

Eine Folge von Zahlen, die strikt steigt, ist aufsteigend sortiert. Es gibt
also höchstens **eine** Reihenfolge, die überhaupt in Frage kommt — nämlich die
nach Temperatur sortierte. Damit zerfällt die Aufgabe in zwei einfache Teile:

1. Sortiere die Quellen nach Temperatur. Das ist der einzige Kandidat.
2. Geh einmal durch und prüfe, ob auch die drei anderen Eigenschaften passen.

Wenn der Kandidat die Prüfung nicht besteht, gibt es keine Lösung — nicht etwa
eine andere Reihenfolge, die man noch suchen müsste.

Zwei Fallen:

- **Gleiche Temperaturen** bedeuten sofort `NO`. Die Bedingung heisst „strikt
  besser", zwei gleich warme Quellen können nicht aufeinanderfolgen. Die Prüfung
  in Schritt 2 fängt das ab, weil sie `>` verlangt und nicht `>=`.
- **Der Schwefelgeruch läuft andersherum.** Weniger ist besser, hier steht `<`.

### Das Programm

```python
import pruefe

EINGABE = "bsp_ein.txt"
# EINGABE = "input.txt"
AUSGABE = "output.txt"
ERWARTET = "bsp_aus.txt"

with open(EINGABE, encoding="utf-8") as datei:
    tokens = datei.read().split()

position = 0


def zahl():
    global position
    position = position + 1
    return int(tokens[position - 1])


def zahlen(anzahl):
    liste = []
    for i in range(anzahl):
        liste.append(zahl())
    return liste


zeilen = []

T = zahl()
for fall in range(T):
    N = zahl()
    temperatur = zahlen(N)
    mineralien = zahlen(N)
    schwefel = zahlen(N)
    panorama = zahlen(N)

    # Jede Quelle als ein Paket. Die urspruengliche Nummer kommt mit hinein,
    # sonst ist sie nach dem Sortieren verloren.
    quellen = []
    for i in range(N):
        quellen.append((temperatur[i], mineralien[i], schwefel[i],
                        panorama[i], i))

    quellen.sort()

    geht = True
    for i in range(1, N):
        vorher = quellen[i - 1]
        jetzt = quellen[i]
        if jetzt[0] <= vorher[0]:
            geht = False
        if jetzt[1] <= vorher[1]:
            geht = False
        if jetzt[2] >= vorher[2]:        # weniger Schwefel ist besser
            geht = False
        if jetzt[3] <= vorher[3]:
            geht = False

    if geht:
        zeilen.append("Case #" + str(fall) + ": YES")
        nummern = []
        for eintrag in quellen:
            nummern.append(str(eintrag[4]))
        # join setzt ein Leerzeichen zwischen alle Eintraege der Liste.
        zeilen.append(" ".join(nummern))
    else:
        zeilen.append("Case #" + str(fall) + ": NO")

pruefe.schreibe(AUSGABE, zeilen)

if EINGABE == "bsp_ein.txt":
    pruefe.vergleiche(ERWARTET, AUSGABE)
```

### Was hier neu ist

**Die Anzahl Ausgabezeilen ist nicht fest.** Bei `NO` schreibst du eine Zeile,
bei `YES` zwei. Das Muster „ein `append` pro Testfall" aus den früheren Modulen
trägt nicht mehr — deshalb sammelt die Lösung die Zeilen einzeln und schreibt
erst am Schluss.

**Das Tupel sortiert nach allen Feldern der Reihe nach.** `quellen.sort()`
ordnet nach Temperatur, bei Gleichstand nach Mineralien und so weiter. Für uns
zählt nur das erste Feld — bei Gleichstand in der Temperatur scheitert die
Prüfung ohnehin.

### Laufzeit

Sortieren O(N log N), prüfen O(N). Bei N = 300 und T = 100 sind das etwa 2 · 10⁵
Schritte. Selbst eine O(N²)-Lösung wäre hier durchgekommen — die Aufgabe belohnt
nicht die Geschwindigkeit, sondern die Einsicht, dass es nur einen Kandidaten
gibt.

---

## Trockenübung 1 — wann lohnt sich Sortieren?

**1.** Lineare Suche für jede Frage: **Q · N** Schritte.

**2.** Sortieren und binär suchen: **N log N + Q log N** Schritte.

**3.** N = 10⁵, Q = 10⁵. Mit log₂(10⁵) ≈ 17:

| | Rechnung | Schritte |
|---|---|---|
| linear | 10⁵ · 10⁵ | 10¹⁰ |
| sortiert | 10⁵ · 17 + 10⁵ · 17 | 3,4 · 10⁶ |

Faktor rund 3000 zugunsten des Sortierens. In Grössenordnungen: eine halbe
Stunde gegen einen Sekundenbruchteil.

**4.** N = 10⁵, Q = 1:

| | Rechnung | Schritte |
|---|---|---|
| linear | 1 · 10⁵ | 10⁵ |
| sortiert | 10⁵ · 17 + 17 | 1,7 · 10⁶ |

Jetzt gewinnt die lineare Suche, und zwar um Faktor 17. Bei einer einzigen Frage
zahlst du das Sortieren umsonst.

**5.** Gleichsetzen: `Q · N = N log N + Q log N`, also
`Q · (N − log N) = N log N` und damit `Q ≈ log N`, sobald N deutlich grösser ist
als log N.

Die Faustregel lautet also: **Sortieren lohnt sich ab ungefähr log N Anfragen**,
hier ab etwa zwanzig. Das ist erstaunlich wenig — und der Grund, warum Sortieren
in der Praxis fast immer die richtige Wahl ist.

---

## Trockenübung 2 — binär suchen ohne Liste

**1.** Prüfen, ob G reicht: Geh die Bücher in ihrer festen Reihenfolge durch und
füll das aktuelle Regal, solange sein Gewicht dabei G nicht überschreitet. Passt
das nächste Buch nicht mehr, fang ein neues Regal an. Zähl die Regale. G reicht
genau dann, wenn du mit höchstens K Regalen auskommst — und wenn kein einzelnes
Buch schwerer als G ist.

Das ist **ein** Durchgang durch die Bücher, also O(N).

**2.** Ja und nein. Wenn es mit G geht, geht es auch mit G + 1: Dieselbe
Verteilung ist weiterhin erlaubt, denn jedes Regal wiegt immer noch höchstens
G + 1. Und wenn es mit G nicht geht, kann es mit G − 1 erst recht nicht gehen.

**3.** Die Eigenschaft aus Frage 2 heisst **Monotonie**: Es gibt eine Schwelle,
unterhalb derer die Antwort immer „nein" ist und ab der sie immer „ja" ist.
Genau diese Schwelle ist die gesuchte Zahl.

Die binäre Suche läuft also nicht über eine Liste, sondern **über den Wertebereich
der Antwort** — über alle denkbaren Werte für „Gewicht des schwersten Regals".

**4.** Untere Schranke: das **Gewicht des schwersten einzelnen Buchs**. Darunter
geht es nie, weil dieses Buch irgendwo stehen muss.

Obere Schranke: die **Summe aller Buchgewichte**. Damit geht es immer, denn dann
passen alle Bücher auf ein einziges Regal.

!!! note "Suche auf der Antwort"
    Dieses Muster — raten, prüfen, halbieren — heisst „binäre Suche auf der
    Antwort" und ist eine der meistgebrauchten Techniken überhaupt. Voraussetzung
    ist immer dieselbe: Die Prüffrage muss monoton sein.

    In den zugänglichen SOI-Runden kommt sie nicht vor, deshalb gibt es dazu hier
    keine Grader-Aufgabe. In der Zweiten Runde begegnet sie dir sicher.

---

Zurück zu den [Übungen](uebungen.md) oder zum
[Lernbaustein](index.md).
