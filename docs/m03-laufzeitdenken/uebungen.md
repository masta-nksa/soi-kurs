# M3 — Übungen

Drei SOI-Teilaufgaben, eine Messübung am eigenen Rechner und eine Schätzrunde
auf Papier. Zusammen sind das 45 Punkte, und für 25 davon musst du nichts Neues
können.

!!! note "Du musst nichts nachschlagen"
    Alles zum Lösen steht auf dieser Seite. Auf soi.ch gehst du erst, wenn deine
    Lösung am Beispiel läuft — dort holst du die Eingabedaten, und dann läuft die
    Uhr.

!!! tip "Neu: Gerüststufe 2"
    `vorlage-stufe2.py` aus dem Ordner `vorlagen/`. Die Werkzeuge zum Einlesen
    bekommst du weiterhin fertig, aber das Muster für einen Testfall trägst du
    selbst ein. Bei der Ausdauer ist es dasselbe wie in M2 — ein guter Moment,
    um es einmal ohne Vorlage hinzuschreiben.

!!! warning "Erst schätzen, dann programmieren"
    Bei **jeder** Aufgabe dieser Seite gilt dieselbe Reihenfolge: Schreib zuerst
    auf ein Blatt, wie viele Schritte deine Idee braucht und wie lange das
    dauert. Eine Zahl, kein Gefühl. Erst danach VS Code öffnen.

    Wer zuerst programmiert und dann merkt, dass es zu lange dauert, hat die
    halbe Lektion verschenkt.

---

## Einstieg — Treppenlauf, Teilaufgabe 3

Aus der Runde 2020/2021. Teilaufgabe 1 kennst du aus
[M0](../m00-werkzeugkasten/index.md), Teilaufgabe 2 aus
[M2](../m02-vollstaendige-suche/uebungen.md).

Binnas Laufstrecke geht vom Dach eines Wolkenkratzers links über die Strasse auf
ein Dach rechts. Gesucht ist die längstmögliche Gesamtdistanz:

```
Höhe links  +  Abstand entlang der Strasse  +  Höhe rechts
```

| Teilaufgabe | Schranke | Punkte | |
|---|---|---|---|
| 1 | N = 1 | 25 | erledigt in M0 |
| 2 | N = 2 | 25 | erledigt in M2 |
| 3 | 1 ≤ N ≤ 1000 | 25 | **dieses Modul** |
| 4 | 1 ≤ N ≤ 100 000 | 25 | M4 |

T = 100, Höhen zwischen 1 und 10⁶.

**Eingabe.** Erste Zeile T. Pro Testfall: eine Zeile mit N, eine Zeile mit den N
Höhen links, eine Zeile mit den N Höhen rechts.

```
Eingabe:              Ausgabe:

1                     Case #0: 11
5
1 5 5 1 1
1 2 3 4 1
```

Die beste Strecke nimmt links die 5 an Position 1 und rechts die 4 an
Position 3: 5 + 2 + 4 = 11. Nicht die beiden höchsten — der Abstand zählt mit.

**Hier musst du nichts Neues programmieren.** Deine allgemeine Lösung aus M2 hat
zwei ineinander liegende Schleifen. Die Frage ist nur, ob sie bei dieser Schranke
durchläuft. Nimm dir **10 Minuten**, und die meisten davon für die Rechnung.

??? tip "Hinweis 1 — erst selbst versuchen"
    Zwei Schleifen über je N Wolkenkratzer. Wie viele Schritte sind das pro
    Testfall bei N = 1000?

    Und dann die Frage, die man am häufigsten vergisst: Wie viele Testfälle gibt
    es?

??? tip "Hinweis 2 — erst selbst versuchen"
    10⁶ Schritte pro Testfall, mal 100 Testfälle sind 10⁸.

    Schlag in der Tabelle nach, welche Grössenordnung das ist, und vergleich sie
    mit deinem Budget von fünf Minuten.

??? tip "Hinweis 3 — erst selbst versuchen"
    Es reicht. 10⁸ Schritte sind die Grössenordnung von Sekunden — unangenehm,
    aber weit innerhalb der fünf Minuten.

    Lad deine alte Lösung hoch. 25 Punkte, ohne eine Zeile Code zu ändern. Genau
    dafür ist das Rechnen da: Es sagt dir nicht nur, wann etwas *nicht* geht,
    sondern auch, wann du dir Arbeit sparen kannst.

!!! success "Erst wenn deine Lösung am Beispiel läuft"
    [Treppenlauf Teilaufgabe 3 einreichen](https://soi.ch/contests/2021/round1/stairracing/#teilaufgabe-3-eine-langere-strasse-25-punkte)

    Ab dem Klick auf „Eingabedaten herunterladen" hast du fünf Minuten.

---

## Kern — Ausdauer, Teilaufgabe 3

Die Ankeraufgabe des Moduls. Dieselbe Strasse, dieselben Löcher, dieselbe Frage
wie in M2 — nur eine andere Zahl in den Limits.

| Teilaufgabe | Schranke | Punkte | |
|---|---|---|---|
| 1 | N = 3 | 20 | erledigt in M2 |
| 2 | 1 ≤ N ≤ 100 | 20 | erledigt in M2 |
| 3 | 1 ≤ N ≤ **100 000** | 20 | **dieses Modul** |
| 4 | mit einer zusätzlichen Regel | 20 | M4 |
| 5 | mit einer zusätzlichen Regel | 20 | M4 |

T = 100. Eingabe- und Ausgabeformat sind unverändert: erste Zeile T, pro
Testfall eine Zeile mit N und eine Zeile mit N Zahlen (`1` = Loch, `0` = heil).
Ausgabe `Case #i: l`, nullbasiert.

```
Eingabe:              Ausgabe:

2                     Case #0: 2
3                     Case #1: 1
1 0 0
3
0 1 0
```

Nimm dir **30 Minuten**. Erst die Rechnung für deine M2-Lösung, dann die neue
Idee.

??? tip "Hinweis 1 — erst selbst versuchen"
    Nimm eine ganz kurze Strasse ohne ein einziges Loch, etwa fünf Abschnitte.

    Wie oft schaut deine M2-Lösung die **letzte** Position an? Zähl es auf
    Papier durch, indem du die Startpunkte der Reihe nach durchgehst.

??? tip "Hinweis 2 — erst selbst versuchen"
    Geh ein einziges Mal von links nach rechts.

    Was musst du dir unterwegs merken, damit du am Ende die Antwort hast? Es
    sind zwei Zahlen. Überleg, welche das sind, bevor du weiterliest.

??? tip "Hinweis 3 — erst selbst versuchen"
    Die eine Zahl ist die Länge des lochfreien Stücks, das an der aktuellen
    Position endet. Die andere ist das beste Ergebnis bisher.

    Wenn ein Loch kommt, beginnt die erste wieder bei null. Was du vorher gezählt
    hast, ist nicht verloren — es steckt schon in der zweiten.

    Achte darauf, dass du auch nach dem letzten Abschnitt noch verglichen hast.
    Am einfachsten ist es, bei **jedem** Schritt zu vergleichen.

!!! success "Erst wenn deine Lösung am Beispiel läuft"
    [Ausdauer Teilaufgabe 3 einreichen](https://soi.ch/contests/2025/preround/endurance/#teilaufgabe-3-ein-sehr-langer-weg-20-punkte)

    Prüf vorher gegen deine alte Lösung: Auf kleinen Eingaben müssen beide
    dasselbe liefern. Zwei Lösungen gegeneinander laufen zu lassen ist die
    zuverlässigste Fehlersuche überhaupt — und du hast hier beide.

---

## Vertiefung — Treppenlauf, Teilaufgabe 4 diagnostizieren

Dieselbe Aufgabe wie im Einstieg, aber mit 1 ≤ N ≤ 100 000.

**Diese Teilaufgabe löst du in diesem Modul nicht.** Die Technik dafür kommt in
[M4](../m04-lineare-techniken/index.md). Was du hier machst, ist die Diagnose —
und die ist der eigentliche Inhalt von M3.

Beantworte schriftlich:

1. Wie viele Schritte bräuchte deine O(N²)-Lösung hier insgesamt? Rechne mit dem
   Faktor T.
2. Welche Grössenordnung ist das?
3. Welche Komplexität bräuchtest du stattdessen, damit es in Sekunden durchläuft?
4. Die Strecke ist `a[i] + |i − j| + b[j]`. Nimm an, der linke Wolkenkratzer
   steht **links vom** rechten, also `i ≤ j`. Löse den Betrag auf und sortier die
   Summe so um, dass alles mit `i` auf der einen und alles mit `j` auf der
   anderen Seite steht. Was fällt dir auf?

Frage 4 ist der Vorgriff auf M4. Wenn du sie beantwortest, hast du die Lösung
schon fast — mehr dazu dort.

---

## Trockenübung 1 — die versteckte Bremse

Am Rechner, ohne Grader. Tipp das Programm ab und miss selbst.

Dieses Programm zählt, wie viele **verschiedene** Zahlen in einer Liste
vorkommen:

```python
import random
import time

zahlen = []
for i in range(20000):
    zahlen.append(random.randint(1, 1000000))

start = time.time()

gesehen = []
for zahl in zahlen:
    if zahl not in gesehen:
        gesehen.append(zahl)

print("Verschiedene:", len(gesehen))
print("Dauer:", time.time() - start)
```

1. Starte es. Notiere die Dauer.
2. Ändere die 20 000 auf 40 000 und starte erneut. **Ist es doppelt so langsam
   oder deutlich mehr?** Was sagt dir das über die Komplexität?
3. **In diesem Programm steht keine zweite Schleife.** Trotzdem verhält es sich
   wie O(N²). Welche Zeile ist die versteckte Schleife, und warum?
4. Schreib das Programm mit einem `set` um und miss noch einmal. Wie ändert sich
   der Faktor beim Verdoppeln?

!!! tip "Was du beim Messen erwarten kannst"
    Bei O(N²) brauchen doppelt so viele Elemente rund **viermal** so lange, bei
    O(N) doppelt so lange. Genau messen wirst du das nicht: Bei so grossen Listen
    kommen Speichereffekte dazu, und dein Gerät ist nebenbei mit anderem
    beschäftigt.

    Achte deshalb nicht auf die Sekunden, sondern auf den **Faktor**. Etwa vier
    statt etwa zwei — das ist die Aussage.

Das ist die gefährlichste Sorte Laufzeitproblem: Die teure Stelle sieht aus wie
eine einfache Frage.

## Trockenübung 2 — Schätzrunde

Papier und Bleistift. Kein Rechner, keine Programme.

Für jede Zeile: Wie viele Schritte insgesamt, welche Grössenordnung ist das, und
kannst du damit einreichen? **T = 100 in allen Fällen**, und wir rechnen mit rund
10⁷ Schritten pro Sekunde.

Antworte in Grössenordnungen — „Sekunden", „Minuten", „Tage". Eine Antwort wie
„17,4 Sekunden" wäre eine Genauigkeit, die die Rechnung nicht hergibt.

| | Aufgabe | Schranke | deine Lösung |
|---|---|---|---|
| a | Treppenlauf ST3 | N ≤ 1 000 | zwei Schleifen, O(N²) |
| b | Treppenlauf ST4 | N ≤ 100 000 | zwei Schleifen, O(N²) |
| c | Ausdauer ST3 | N ≤ 100 000 | ein Durchgang, O(N) |
| d | Gipfel ST3 (2022) | N ≤ 1 000 000 | ein Durchgang, O(N) |
| e | irgendeine Aufgabe | N ≤ 100 | drei Schleifen, O(N³) |

Zeile **d** hat einen Haken, der nicht in der Komplexität steckt. Wenn deine
Antwort dort „O(N) ist immer gut" lautet, lies den Abschnitt über das Einlesen
im Konzept noch einmal.

---

Wenn du eine Aufgabe wirklich versucht hast, findest du die
[Musterlösungen zu M3](loesung.md).
