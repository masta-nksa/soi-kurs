# M4 — Musterlösungen

Diese Seite verrät die Lösung. Hast du es wirklich selbst versucht?

---

## Einstieg und Kern — Ausdauer, Teilaufgabe 4 und 5

**Das Modell.** Ein Abschnitt ist brauchbar, wenn er höchstens K Löcher enthält.
Gesucht ist der längste solche Abschnitt. Welche Löcher repariert werden, ist
keine Entscheidung — es sind alle im gewählten Abschnitt.

**Der Zweizeiger.** Ein Fenster wandert über die Strasse. Das rechte Ende geht in
jedem Schritt eins weiter; wenn zu viele Löcher im Fenster sind, wird das linke
Ende nachgezogen.

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


def loese(n, k, p):
    bestes = 0
    links = 0
    loecher = 0
    for rechts in range(n):
        if p[rechts] == 1:
            loecher = loecher + 1
        while loecher > k:
            if p[links] == 1:
                loecher = loecher - 1
            links = links + 1
        laenge = rechts - links + 1
        if laenge > bestes:
            bestes = laenge
    return bestes


zeilen = []

T = zahl()
for i in range(T):
    N = zahl()
    K = zahl()
    p = zahlen(N)
    ergebnis = loese(N, K, p)
    zeilen.append("Case #" + str(i) + ": " + str(ergebnis))

pruefe.schreibe(AUSGABE, zeilen)

if EINGABE == "bsp_ein.txt":
    pruefe.vergleiche(ERWARTET, AUSGABE)
```

**Dieses Programm löst Teilaufgabe 4 und 5** — zusammen 40 Punkte. Und mit K = 0
liefert es auch das Ergebnis von Teilaufgabe 3.

Achte auf die Reihenfolge im Schleifenrumpf: erst das neue Element aufnehmen,
dann verkleinern, dann messen. Wer zuerst misst, misst ein ungültiges Fenster.

Und `while`, nicht `if`: Bei K = 0 und mehreren Löchern hintereinander muss das
linke Ende in einem Schritt mehrfach vorrücken.

Zum Testen das Beispiel aus der Aufgabenstellung, `bsp_ein.txt`:

```
2
10 3
0 0 0 1 1 1 0 0 0 0
12 3
0 1 0 0 1 1 0 1 0 0 1 0
```

und `bsp_aus.txt`:

```
Case #0: 10
Case #1: 8
```

Bau dir zusätzlich einen Testfall mit K = 0 und vergleich mit deiner Lösung aus
M3. Beide müssen dasselbe liefern.

??? tip "Wenn du Teilaufgabe 4 mit Brute Force gelöst hast"
    Dann war das richtig, und du solltest sie eingereicht haben.

    Bei N ≤ 100 und T = 100 landen sogar drei geschachtelte Schleifen bei 10⁸
    Schritten, also in der Grössenordnung von Sekunden. 20 Punkte, ohne den
    Zweizeiger zu kennen.

    Der Zweizeiger ist trotzdem kein Umweg: Er ist dieselbe Lösung für
    Teilaufgabe 5, wo Brute Force bei 10¹² Schritten liegt.

---

## Vertiefung — Treppenlauf, Teilaufgabe 4

**Die Umformung.** Gesucht ist das Maximum von

```
a[i] + |i − j| + b[j]
```

Der Betrag ist das Problem: Solange er drinsteht, hängen `i` und `j` aneinander.
Also spaltet man die zwei Fälle auf.

**Fall 1: der Wolkenkratzer links steht bei der kleineren Position**, also
i ≤ j. Dann ist `|i − j| = j − i`, und man kann sortieren:

```
a[i] + (j − i) + b[j]  =  (a[i] − i)  +  (b[j] + j)
```

Jetzt steht links nur noch etwas mit `i`, rechts nur noch etwas mit `j`. Für ein
festes `j` brauchst du also nur den **grössten Wert von `a[i] − i` unter allen
i ≤ j** — und den kannst du mitführen, statt ihn jedes Mal zu suchen. Das ist
dieselbe Idee wie bei den Präfixsummen, nur mit Maximum statt Summe.

**Fall 2: der Wolkenkratzer links steht rechts**, also i ≥ j. Dann ist
`|i − j| = i − j`, und dieselbe Umformung ergibt `(a[i] + i) + (b[j] − j)`.

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


def loese(n, a, b):
    bestes = 0

    # Fall 1: (a[k] - k) + (b[j] + j) fuer k <= j
    bestes_a = a[0]
    for j in range(n):
        wert = a[j] - j
        if wert > bestes_a:
            bestes_a = wert
        strecke = bestes_a + b[j] + j
        if strecke > bestes:
            bestes = strecke

    # Fall 2: (b[k] - k) + (a[j] + j) fuer k <= j
    bestes_b = b[0]
    for j in range(n):
        wert = b[j] - j
        if wert > bestes_b:
            bestes_b = wert
        strecke = bestes_b + a[j] + j
        if strecke > bestes:
            bestes = strecke

    return bestes


zeilen = []

T = zahl()
for i in range(T):
    N = zahl()
    a = zahlen(N)
    b = zahlen(N)
    ergebnis = loese(N, a, b)
    zeilen.append("Case #" + str(i) + ": " + str(ergebnis))

pruefe.schreibe(AUSGABE, zeilen)

if EINGABE == "bsp_ein.txt":
    pruefe.vergleiche(ERWARTET, AUSGABE)
```

Der zweite Durchgang sieht aus wie der erste mit vertauschten Rollen, und genau
das ist er auch: Dort ist der Turm auf der **b**-Seite der weiter links stehende.
Ein Durchgang von rechts nach links wäre gleichwertig.

Zwei Durchgänge, jeder O(N) — insgesamt O(N) statt O(N²). Bei N ≤ 100 000 und
T = 100 sind das 2 · 10⁷ Schritte statt 10¹².

**Dieses Programm löst alle vier Teilaufgaben des Treppenlaufs**, also 100
Punkte. Prüf es am Beispiel von Teilaufgabe 3 — dort muss `Case #0: 11`
herauskommen.

??? tip "Die zuverlässigste Fehlersuche"
    Lass deine neue Lösung und die alte aus M2 auf denselben zufälligen kleinen
    Eingaben laufen — etwa N = 5 mit Höhen zwischen 1 und 20 — und vergleich die
    Ausgaben.

    Bei einer Umformung wie dieser ist ein Vorzeichenfehler schnell passiert und
    von Hand kaum zu finden. Zwei Programme, die sich widersprechen, zeigen ihn
    sofort.

---

## Trockenübung 1 — die Frage, die hundertmal gestellt wird

**1. Die naive Lösung.** Pro Frage werden bis zu N Tage durchgezählt, bei Q
Fragen also `N · Q` Schritte:

```
10⁵ · 10⁵ = 10¹⁰
```

**2. Die Dauer.** 10¹⁰ Schritte sind die Grössenordnung einer halben Stunde —
ausserhalb jedes Budgets.

**3. Die Lösung.** Einmal vorher eine Präfixsummen-Liste bauen: `praefix[i]` ist
die Summe der Tickets der ersten i Tage. Dann ist die Antwort auf „Tag a bis Tag
b" eine einzige Subtraktion:

```
praefix[b + 1] - praefix[a]
```

Die Vorbereitung kostet N Schritte — ein Durchgang, bei dem jeder Wert zur Summe
der vorherigen addiert wird.

**4. Insgesamt.** N für die Vorbereitung plus Q für die Fragen:

```
10⁵ + 10⁵ = 2 · 10⁵
```

Ein Sekundenbruchteil statt einer halben Stunde. Aus `N · Q` ist `N + Q`
geworden, und das ist der ganze Trick.

**5. Ab wann es sich lohnt.** Gleichsetzen: `Q · N = N + Q` ergibt
`Q · (N − 1) = N`, also `Q ≈ 1`.

Die Antwort ist überraschend: **schon ab der zweiten Frage.** Die Vorbereitung
kostet genauso viel wie eine einzige naive Frage im schlimmsten Fall — ab der
zweiten ist sie geschenkt.

Das ist ein guter Vergleichspunkt für später: Beim Sortieren in
[M5](../m05-sortieren-und-suchen/index.md) liegt dieselbe Schwelle bei etwa
log N, also rund zwanzig Fragen. Präfixsummen sind billiger vorzubereiten und
lohnen sich deshalb fast immer.

Merk dir die Form: **Wenn dieselbe Art Frage mehr als einmal gestellt wird, lohnt
sich eine Vorbereitung, die jede einzelne Frage billig macht.**

---

## Trockenübung 2 — warum zwei Schleifen nicht immer O(N²) sind

**1. Eine teure Eingabe.** Nimm K = 0 und eine Strasse aus lauter Nullen, an
deren Ende ein einziges Loch steht:

```
0 0 0 0 0 0 0 0 0 1
```

Solange das rechte Ende über die Nullen wandert, tut die innere Schleife nichts.
Im letzten Schritt kommt das Loch, und das linke Ende muss auf einen Schlag über
die ganze Strasse nachziehen — fast N Schritte in einem einzigen Durchgang.

**2. Trotzdem höchstens 2N Schritte insgesamt.**

Argumentiere über die beiden Enden statt über die Schleifen:

- `rechts` beginnt bei 0, wird in jedem Durchgang der äusseren Schleife um eins
  erhöht und endet bei N. Das sind genau N Bewegungen.
- `links` beginnt bei 0 und wird ausschliesslich **erhöht**, nie verringert. Es
  wird nie grösser als N. Also sind es über den ganzen Durchlauf höchstens N
  Bewegungen.

Jeder Schritt der inneren Schleife bewegt `links` um eins. Die innere Schleife
kann deshalb über den ganzen Durchlauf höchstens N mal ausgeführt werden — egal,
wie sich diese Schritte auf die Durchgänge verteilen.

Zusammen also höchstens 2N Bewegungen, und das ist O(N).

**3. Warum das kein Widerspruch ist.**

Weil `links` ein festes Gesamtbudget von N Bewegungen hat: Was in einem
Durchgang viel verbraucht wird, fehlt in allen anderen. Ein einzelner teurer
Durchgang **erzwingt**, dass die übrigen billig sind.

Das ist der Kern der amortisierten Analyse. Die Frage lautet nie „wie teuer ist
der schlimmste einzelne Schritt", sondern „wie teuer sind alle zusammen".

---

Zurück zu [den Übungen](uebungen.md) oder zum
[Lernbaustein](index.md).
