# M2 — Musterlösungen

Diese Seite verrät die Lösung. Hast du es wirklich selbst versucht?

---

## Endurance, Teilaufgabe 1 und 2

**Das Modell.** Eine Möglichkeit ist ein zusammenhängender Abschnitt. Wir halten
das linke Ende fest und wandern nach rechts, solange kein Loch kommt. Dabei
zählen wir die Länge mit und merken uns das beste Ergebnis.

Der Kopf mit dem Leser ist derselbe wie in M1. Hier der Teil darunter:

```python
T = zahl()

zeilen = []
for i in range(T):
    N = zahl()
    p = zahlen(N)

    bestes = 0
    for start in range(N):
        laenge = 0
        for ende in range(start, N):
            if p[ende] == 1:
                break
            laenge = laenge + 1
            if laenge > bestes:
                bestes = laenge

    zeilen.append("Case #" + str(i) + ": " + str(bestes))

pruefe.schreibe(AUSGABE, zeilen)
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
T = zahl()

zeilen = []
for i in range(T):
    N = zahl()
    a = zahlen(N)
    b = zahlen(N)

    bestes = 0
    for links in range(N):
        for rechts in range(N):
            strecke = a[links] + b[rechts] + abs(links - rechts)
            if strecke > bestes:
                bestes = strecke

    zeilen.append("Case #" + str(i) + ": " + str(bestes))

pruefe.schreibe(AUSGABE, zeilen)
```

`abs` liefert den Betrag, also den Abstand ohne Vorzeichen.

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

Mit nur zwei Wolkenkratzern pro Seite lässt sich das übrigens kaum zeigen: Dort
beträgt der Abstand höchstens 1, und die Abkürzung geht nur schief, wenn zwei
Höhen genau gleich sind. Das ist der Grund, warum eine Abkürzung „bei den
Beispielen funktioniert" und trotzdem falsch ist.

!!! warning "Eine Annahme, die du selbst prüfen solltest"
    Dass die Strecke entlang der Strasse genau dem Abstand der beiden Positionen
    entspricht, ist aus Teilaufgabe 1 erschlossen: Dort stehen sich die
    Wolkenkratzer gegenüber, der Abstand ist 0, und die Antwort ist `a + b`.

    Lies die Aufgabenstellung an dieser Stelle genau, bevor du hochlädst. Wenn
    dort ein anderer Zusammenhang steht, ändert sich nur die eine Zeile mit
    `strecke` — die Struktur der Suche bleibt gleich.

---

## Laufzeit-Schätzung

Beide Lösungen haben zwei ineinander liegende Schleifen, also **O(N²)** pro
Testfall. Bei T = 100 Testfällen kommt der Faktor 100 dazu.

| Aufgabe | Teilaufgabe | N | Schritte pro Fall | insgesamt | Urteil |
|---|---|---|---|---|---|
| Endurance | 3 | 10⁵ | 10¹⁰ | 10¹² | aussichtslos |
| Treppenlauf | 3 | 10³ | 10⁶ | 10⁸ | zu langsam |
| Treppenlauf | 4 | 10⁵ | 10¹⁰ | 10¹² | aussichtslos |

Python schafft 10⁶ bis 10⁷ Schritte pro Sekunde. Selbst die freundlichste Zeile
der Tabelle liegt um mindestens den Faktor 10 daneben, die anderen um das
Millionenfache.

**Das Ergebnis ist die eigentliche Botschaft:** Deine vollständige Suche endet in
beiden Aufgaben exakt nach Teilaufgabe 2. Nicht weil du sie schlecht
programmiert hättest — sondern weil mehr Möglichkeiten da sind, als man einzeln
anschauen kann.

Das ist kein Scheitern, sondern eine Diagnose. Man stellt sie in zwei Minuten auf
Papier, statt sie nach vierzig Minuten Programmieren zu erleben.

Bemerkenswert ist die mittlere Zeile: Treppenlauf Teilaufgabe 3 wäre in C++
knapp durchgelaufen. In Python nicht. Der Druck zur besseren Idee setzt bei uns
früher ein — und diese bessere Idee ist der Inhalt von M3.

---

## Verkleidung — die versteckte Suche

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

Der Unterschied zu Endurance ist die Frage, die gestellt wird. Bei Endurance
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

Zurück zu [den Übungen](uebungen.md) oder zum
[Lernbaustein](index.md).
