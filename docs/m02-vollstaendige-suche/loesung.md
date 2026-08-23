# M2 — Musterlösungen

Diese Seite verrät die Lösung. Hast du es wirklich selbst versucht?

---

## Ausdauer, Teilaufgabe 1 und 2

**Das Modell.** Eine Möglichkeit ist ein zusammenhängender Abschnitt. Wir halten
das linke Ende fest und wandern nach rechts, solange kein Loch kommt. Dabei
zählen wir die Länge mit und merken uns das beste Ergebnis.

Das ganze Programm. Mit `vorlage.py` schreibst du davon nur die Funktion
`loese` — der Rest steht schon dort.

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


def loese(n, p):
    bestes = 0
    for start in range(n):
        laenge = 0
        for ende in range(start, n):
            if p[ende] == 1:
                break
            laenge = laenge + 1
            if laenge > bestes:
                bestes = laenge
    return bestes


zeilen = []

T = zahl()
for i in range(T):
    N = zahl()
    p = zahlen(N)
    ergebnis = loese(N, p)
    zeilen.append("Case #" + str(i) + ": " + str(ergebnis))

pruefe.schreibe(AUSGABE, zeilen)

if EINGABE == "bsp_ein.txt":
    pruefe.vergleiche(ERWARTET, AUSGABE)
```

`break` verlässt die innere Schleife sofort. Sobald ein Loch kommt, ist dieser
Startpunkt erledigt — jeder längere Abschnitt von hier aus enthält dasselbe Loch.

**Dieses eine Programm löst beide Teilaufgaben.** Für Teilaufgabe 1 mit N = 3
hättest du auch von Hand unterscheiden können; das allgemeine Programm ist
kürzer und trägt gleich 20 Punkte weiter.

Zum Testen `bsp_ein.txt`:

```
2
3
1 0 0
3
0 1 0
```

und `bsp_aus.txt`:

```
Case #0: 2
Case #1: 1
```

Bau dir zusätzlich einen eigenen Testfall mit `1 1 1` — die Antwort ist 0. Das
mitgelieferte Beispiel prüft diesen Fall nicht.

??? tip "Warum ist das O(N²) und nicht O(N³)?"
    Weil die Länge mitgezählt wird, statt jeden Abschnitt noch einmal
    nachzuprüfen.

    Die dritte Schleife entsteht, wenn man erst beide Enden festlegt und dann
    fragt: „Ist zwischen diesen Enden ein Loch?" Diese Frage wurde für den
    kürzeren Abschnitt schon beantwortet — die Antwort muss man nur weiterreichen,
    und genau das tut `laenge`.

---

## Treppenlauf, Teilaufgabe 2

**Das Modell.** Eine Möglichkeit ist ein Paar: ein Wolkenkratzer links, einer
rechts. Die Strecke setzt sich zusammen aus

```
Höhe links + Höhe rechts + Abstand entlang der Strasse
```

Der Abstand ist der Unterschied der beiden Positionen. Stehen sich die beiden
direkt gegenüber, ist er 0 — genau der Fall aus Teilaufgabe 1, bei dem die
Antwort `a + b` lautet.

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
    for links in range(n):
        for rechts in range(n):
            strecke = a[links] + b[rechts] + abs(links - rechts)
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

`abs` liefert den Betrag, also den Abstand ohne Vorzeichen.

!!! note "Hier musst du den Hauptteil anpassen"
    `vorlage.py` liest pro Testfall **eine** Zahlenliste. Der Treppenlauf hat
    **zwei** — die Höhen links und die Höhen rechts. Zwei Aufrufe von `zahlen(N)`
    statt einem, und `loese` bekommt entsprechend ein Argument mehr.

    Das ist der erste Vorgeschmack auf Gerüststufe 2: Ab M3 ist das Einlesen
    eines Testfalls generell deine Aufgabe.

Das Programm ist allgemein geschrieben und damit gleich die Lösung der
Verschärfung. Prüf es mit dem Beispiel der Aufgabenstellung: Dort ist N = 1, es
gibt nur eine Kombination, und der Abstand ist 0 — es müssen 5 und 1337
herauskommen.

**Warum die Abkürzung nicht funktioniert.** „Höchster links plus höchster
rechts" vergisst, dass der Abstand mitzählt. Ein Gegenbeispiel mit drei
Wolkenkratzern pro Seite:

```
Seite a:  10   1   1
Seite b:   9   1   8
```

Die Abkürzung nimmt links die 10 (Position 0) und rechts die 9 (Position 0).
Die stehen sich gegenüber, der Abstand ist 0:

```
10 + 9 + 0 = 19
```

Besser ist aber die 10 links mit der 8 rechts (Position 2):

```
10 + 8 + 2 = 20
```

Der eine Meter weniger Höhe wird durch zwei Meter Abstand mehr als
ausgeglichen. Genau solche Fälle findet die vollständige Suche und die Abkürzung
nicht.

Bei nur zwei Wolkenkratzern pro Seite geht die Abkürzung **nur bei Gleichständen**
schief — der Abstand beträgt dort höchstens 1, und den kann eine niedrigere Höhe
nur ausgleichen, wenn sie gar nicht niedriger ist. Genau so ein Fall ist
Testfall 0 der Aufgabenstellung: `1 1 / 1 1` mit der Antwort 3.

Wer dagegen bei N = 2 mit lauter verschiedenen Höhen testet, findet nie ein
Gegenbeispiel. Das ist der Grund, warum eine Abkürzung „bei den Beispielen
funktioniert" und trotzdem falsch ist — Trockenübung 3 rechnet das durch.

!!! note "Die Distanz ist wirklich der Positionsabstand"
    Das bestätigt die Aufgabenstellung an ihrem eigenen Beispiel: Bei
    `1 1 / 1 1` ist die beste Strecke die von Position 0 nach Position 1, und
    sie ist 1 + 1 + 1 = 3 lang. Die 1 in der Mitte ist der Abstand.

    Der Grenzfall steht gleich daneben: Bei `1 1336 / 1 1336` liegen die beiden
    hohen Türme einander gegenüber, der Abstand ist 0, und es kommen
    1336 + 1336 = 2672 heraus.

---

## Trockenübung 1 — wo hört das auf?

Beide Lösungen haben zwei ineinander liegende Schleifen, also **O(N²)** pro
Testfall. Bei T = 100 Testfällen kommt der Faktor 100 dazu.

| Aufgabe | Teilaufgabe | N | Schritte pro Fall | insgesamt | Grössenordnung | Urteil |
|---|---|---|---|---|---|---|
| Treppenlauf | 3 | 10³ | 10⁶ | 10⁸ | Sekunden | **läuft** |
| Ausdauer | 3 | 10⁵ | 10¹⁰ | 10¹² | Tage | aussichtslos |
| Treppenlauf | 4 | 10⁵ | 10¹⁰ | 10¹² | Tage | aussichtslos |

Gerechnet mit der Faustregel 10⁷ Schritte pro Sekunde. Die Spalte „Grössenordnung"
ist bewusst grob — ob es sieben oder dreissig Sekunden werden, hängt vom Gerät ab
und ändert am Urteil nichts.

**Die erste Zeile ist die Überraschung.** Treppenlauf Teilaufgabe 3 läuft mit
deiner vollständigen Suche durch — ein paar Sekunden, volle 25 Punkte. Du musst
nichts Besseres können. Probier es aus.

Der Grund ist unser Einreichungsweg: Wir laden eine Ausgabedatei hoch, kein
Programm. **Niemand misst die Laufzeit.** Die einzige Uhr sind die fünf Minuten
zwischen Download und Upload, und ein paar Sekunden passen dort bequem hinein. In
einem Wettbewerb mit Sekundenlimit wäre dieselbe Lösung durchgefallen.

Faustregel für den Rest des Kurses:

| Schritte insgesamt | Grössenordnung | Urteil |
|---|---|---|
| bis 10⁸ | Sekunden | unproblematisch |
| 10⁹ | Minuten | ohne Reserve für einen zweiten Versuch |
| ab 10¹⁰ | halbe Stunde und mehr | ausgeschlossen |

**Die beiden anderen Zeilen sind die eigentliche Botschaft.** Dort hilft kein
Warten: 10¹² Schritte sind Tage. Zwischen „unbequem" und „unmöglich" liegen bei
uns keine Zwischentöne — kleine Unterschiede sind egal, grosse sind tödlich.

Deine vollständige Suche trägt also weiter, als du vielleicht dachtest, und
endet dann schlagartig. Wo genau, sagt dir eine Schätzung in zwei Minuten auf
Papier — statt vierzig Minuten Programmieren und einem Programm, das nie fertig
wird.

Wie man den Sprung nach 10⁵ trotzdem schafft, ist der Inhalt von M3.

---

## Trockenübung 2 — wo steckt hier eine Suche?

**1. Was ist eine Möglichkeit?**

Ein Paar aus zwei verschiedenen Käsestücken. Die Reihenfolge spielt keine Rolle:
Stück 3 mit Stück 7 ist dieselbe Möglichkeit wie Stück 7 mit Stück 3.

**2. Wie viele gibt es?**

```
N · (N - 1) / 2
```

Bei N = 100 sind das 4950. Für jedes Stück gäbe es N − 1 Partner, das wären
N · (N − 1) — aber so hätte man jedes Paar zweimal gezählt, deshalb durch 2.

**3. Die Invariante**

> **Solange `gefunden` noch falsch ist, hatte keines der bisher geprüften Paare
> zusammen genau W Gramm.**

Der Unterschied zu Ausdauer ist die Frage, die gestellt wird. Bei Ausdauer
suchst du das Beste und musst deshalb bis zum Ende schauen. Hier suchst du nur,
ob es überhaupt eines gibt — sobald du eines findest, darfst du sofort aufhören.

**4. Wenn dasselbe Stück zweimal zählen dürfte**

Dann kommen die N Möglichkeiten dazu, bei denen ein Stück mit sich selbst
kombiniert wird:

```
N · (N - 1) / 2 + N  =  N · (N + 1) / 2
```

Bei N = 100 also 5050.

Diese Formel kennst du bereits — es ist die Anzahl der Abschnitte einer Strasse
der Länge N aus dem Konzept. Kein Zufall: Beide zählen dasselbe, nämlich alle
Paare `(i, j)` mit `i ≤ j`. Zwei Aufgaben, die nichts miteinander zu tun haben,
und dieselbe Anzahl Möglichkeiten.

---

## Trockenübung 3 — eine Abkürzung widerlegen

**1. Das offizielle Beispiel widerlegt die Abkürzung sofort.**

`1 1` links, `1 1` rechts. Alle vier Türme sind gleich hoch. „Der höchste links"
ist also nicht eindeutig — nimmt man beide Male den ersten, kommt heraus:

```
1 + 1 + 0 = 2
```

Die richtige Antwort ist 3: ein Turm an Position 0, einer an Position 1, dazu
1 für den Abstand. Die Abkürzung liegt daneben, weil sie nur auf die Höhen
schaut und die Positionen dem Zufall überlässt.

**2. Ein Gegenbeispiel mit lauter verschiedenen Höhen.**

Bei N = 3 genügen schon die Zahlen 1 bis 3:

```
Seite a:  1  2  3
Seite b:  2  1  3
```

Die Abkürzung nimmt links die 3 (Position 2) und rechts die 3 (Position 2). Die
stehen sich gegenüber:

```
3 + 3 + 0 = 6
```

Besser ist die 3 links mit der 2 rechts an Position 0:

```
3 + 2 + 2 = 7
```

Ein Meter weniger Höhe, zwei Meter mehr Abstand. Etwas grosszügiger geht es
auch so:

```
Seite a:  10   1   1
Seite b:   9   1   8
```

Abkürzung 10 + 9 + 0 = 19, tatsächlich bestes Paar 10 + 8 + 2 = 20.

**3. Die reparierte Fassung.**

*„Bei Gleichstand nehme ich unter allen höchsten Türmen die Kombination mit dem
grössten Abstand."*

Bei **N = 2 hält sie**. Wir haben alle Höhenkombinationen aus den Werten 1 bis 4
durchprobiert — 256 Fälle — und die reparierte Abkürzung war in keinem
schlechter als die vollständige Suche. Testfall 0 von oben fängt sie ab: Unter
den vier gleich hohen Türmen wählt sie zwei mit Abstand 1 und kommt auf 3.

Bei **N = 3 hält sie nicht mehr**:

```
Seite a:  1  1  2
Seite b:  1  1  2
```

Das Maximum ist auf beiden Seiten die 2 an Position 2, es gibt also gar keinen
Gleichstand zu nutzen: 2 + 2 + 0 = 4. Am besten ist aber die 2 links mit der 1
rechts an Position 0: 2 + 1 + 2 = 5.

**4. Was das über Testbeispiele sagt.**

Das ist der eigentliche Punkt, und die Zahlen sind unangenehm deutlich. Von allen
Höhenkombinationen aus 1 bis 4:

| | N = 2 | N = 3 |
|---|---|---|
| naive Abkürzung falsch | 64 von 256 | 1532 von 4096 |
| davon mit lauter verschiedenen Höhen | **0** | 78 |
| reparierte Abkürzung falsch | **0** | 264 |

Lies die mittlere Zeile noch einmal. Wer bei N = 2 mit lauter verschiedenen
Höhen testet, findet **kein einziges** Gegenbeispiel — die Abkürzung besteht
jeden solchen Test. Sie ist trotzdem falsch.

Daraus folgen zwei Gewohnheiten:

- **Bau Testfälle mit Gleichständen.** Gleiche Werte, Nullen, leere Eingaben,
  alles-gleich — dort brechen Ideen zuerst. Die mitgelieferten Beispiele sind
  zum Erklären gebaut, nicht zum Fallenstellen; dass Testfall 0 hier trotzdem
  eine Falle enthält, ist Glück.
- **Ein Test kann eine Idee widerlegen, nie beweisen.** Wenn du kein
  Gegenbeispiel findest, heisst das nicht, dass es keines gibt — es heisst, dass
  du jetzt begründen musst, warum es keines geben kann. Findest du diese
  Begründung nicht, nimm die vollständige Suche.

---

Zurück zu [den Übungen](uebungen.md) oder zum
[Lernbaustein](index.md).
