# M1 — Musterlösungen

Diese Seite verrät die Lösung. Hast du es wirklich selbst versucht?

---

## Cheeseparty, Teilaufgabe 1

**Das Modell.** An der Party sind N Familien mit je K + 2 Mäusen, dazu Stofl:

```
Mäuse = N · (K + 2) + 1
Käse  = Mäuse · S
```

Probe bei N = 0: eine Maus, S Stück Käse. Stimmt.

Das ganze Programm, so wie es aus der Vorlage entsteht:

```python
import pruefe

EINGABE = "bsp_ein.txt"
AUSGABE = "output.txt"
ERWARTET = "bsp_aus.txt"

with open(EINGABE, encoding="utf-8") as datei:
    tokens = datei.read().split()

position = 0


def zahl():
    global position
    position = position + 1
    return int(tokens[position - 1])


N = zahl()
K = zahl()
S = zahl()

maeuse = N * (K + 2) + 1
kaese = maeuse * S

zeilen = []
zeilen.append(str(kaese))

pruefe.schreibe(AUSGABE, zeilen)

if EINGABE == "bsp_ein.txt":
    pruefe.vergleiche(ERWARTET, AUSGABE)
```

Beachte die Ausgabe: nur die Zahl, kein `Case #0:`. Cheeseparty hat keine
Testfälle.

Zum Testen brauchst du `bsp_ein.txt` mit `4 3 6` und `bsp_aus.txt` mit `126`.

---

## Cheeseparty, Teilaufgabe 2

Der Kopf mit dem Leser bleibt unverändert. Nur der untere Teil ändert sich:

```python
N = zahl()
K = zahl()
S = zahl()
R = zahl()

maeuse = N * (K + 2) + 1
richtig = maeuse * S

if R == richtig:
    antwort = "YES"
else:
    antwort = "NO"

zeilen = []
zeilen.append(antwort)

pruefe.schreibe(AUSGABE, zeilen)
```

Das ist der ganze Unterschied: eine Zahl mehr einlesen, einmal vergleichen, statt
der Zahl ein Wort ausgeben. Die Rechnung selbst ist identisch.

Wer hier lange gesucht hat, hat vermutlich versucht, aus R auf N, K und S
zurückzurechnen. Das geht nicht eindeutig und wäre auch gar nicht gefragt.

---

## Directions, Teilaufgaben 1 bis 3

**Das Modell.** Gesucht ist: Ist Stofls Zeichenkette `s` der Anfang von Binnas
Zeichenkette `b`?

Dafür gibt es in Python eine fertige Funktion. `b.startswith(s)` ist genau dann
wahr, wenn `b` mit `s` beginnt.

```python
def wort():
    global position
    position = position + 1
    return tokens[position - 1]


T = zahl()

zeilen = []
for i in range(T):
    b = wort()
    s = wort()

    if b.startswith(s):
        antwort = "YES"
    else:
        antwort = "NO"

    zeilen.append("Case #" + str(i) + ": " + antwort)

pruefe.schreibe(AUSGABE, zeilen)
```

**Dieses eine Programm löst alle drei Teilaufgaben.** Teilaufgabe 1 (gleich lang)
und Teilaufgabe 2 (nur ein Zeichen) sind Spezialfälle des allgemeinen Falls. Wer
zuerst den allgemeinen Fall modelliert, bekommt die 100 Punkte in einem Zug.

Der Fall, den viele übersehen: Wenn `s` länger ist als `b`, kann `b` nicht mit
`s` beginnen. `startswith` gibt dann korrekt `False` zurück — von Hand
programmiert vergisst man diese Prüfung leicht und liest über das Ende der
Zeichenkette hinaus.

Achte hier auf `Case #` mit nullbasierter Nummer.

Zum Testen `bsp_ein.txt`:

```
3
rrlr
rrrr
lrrrl
lrrrl
rrll
llrr
```

und `bsp_aus.txt`:

```
Case #0: NO
Case #1: YES
Case #2: NO
```

Beachte, dass die beiden Zeichenketten eines Testfalls auf zwei getrennten
Zeilen stehen. Für den Leser aus der Vorlage macht das keinen Unterschied — er
zerlegt die ganze Datei in Wörter und gibt sie eines nach dem anderen heraus.

---

## Sushi, Teilaufgaben 1 und 3

**Das Modell.** Bei zwei Sushi gibt es genau zwei Arten zu bestellen:

```
ohne Angebot:  p₀ + p₁
mit Angebot:   max(p₀, p₁) + S
```

Gesucht ist der kleinere der beiden Beträge. Mehr steckt nicht dahinter — kein
Ausprobieren, keine Fallunterscheidung über die Preise.

```python
def zahlen(anzahl):
    liste = []
    for i in range(anzahl):
        liste.append(zahl())
    return liste


T = zahl()

zeilen = []
for i in range(T):
    N = zahl()
    S = zahl()
    preise = zahlen(N)

    ohne_angebot = preise[0] + preise[1]
    mit_angebot = max(preise[0], preise[1]) + S
    guenstiger = min(ohne_angebot, mit_angebot)

    zeilen.append("Case #" + str(i) + ": " + str(guenstiger))

pruefe.schreibe(AUSGABE, zeilen)
```

Rechne die beiden Beispiele nach:

| Eingabe | ohne Angebot | mit Angebot | Antwort |
|---|---|---|---|
| `2 0` / `16 42` | 58 | 42 + 0 = 42 | 42 |
| `2 32` / `16 42` | 58 | 42 + 32 = 74 | 58 |

Bei Teilaufgabe 1 gewinnt immer das Angebot, weil die Flasche nichts kostet. Bei
Teilaufgabe 3 kommt es darauf an — und genau deshalb reicht es nicht, nur eine
der beiden Möglichkeiten hinzuschreiben.

Beachte: `N` wird eingelesen, obwohl es in diesen beiden Teilaufgaben immer 2
ist. Das Format schreibt die Zahl vor, also muss sie gelesen werden — sonst
verrutscht alles Weitere.

---

## Widerlegung

**1. Wen vergisst welche Formel?**

| Formel | vergisst |
|---|---|
| Anna: `(N · K + 1) · S` | die beiden Elterntiere jeder Familie |
| Bea: `(N · (K + 2)) · S` | Stofl selbst |

**2. Wann stimmen sie trotzdem?**

Annas Formel stimmt, wenn `N · K + 1 = N · (K + 2) + 1`, also wenn `2 · N = 0` —
das heisst **N = 0**. Sind keine Familien eingeladen, gibt es auch keine Eltern
zu vergessen.

Beas Formel stimmt, wenn `N · (K + 2) = N · (K + 2) + 1`, und das geht nie. Aber:
Ist **S = 0**, kommt bei jeder Formel 0 heraus. Dann stimmen beide.

Zusammengefasst: Bei `N = 0` fällt Anna nicht auf, bei `S = 0` fällt keine von
beiden auf.

**3. Was heisst das fürs Testen?**

Ein Beispiel, das durchläuft, beweist gar nichts.

Das mitgelieferte Beispiel `4 3 6` hätte hier beide Fehler gefunden — Glück
gehabt. Ein Beispiel mit `N = 0` oder `S = 0` hätte Anna oder beide
durchgewinkt, und die Aufgabe wäre mit 0 Punkten zurückgekommen.

Deshalb die Probe am Extremfall aus dem Konzept: Setz selbst die kleinsten
erlaubten Werte ein und rechne von Hand nach. Das mitgelieferte Beispiel ist
dafür gemacht, das Format zu zeigen, nicht dein Denken zu prüfen.

---

Zurück zu [den Übungen](uebungen.md) oder zum
[Lernbaustein](index.md).
