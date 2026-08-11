# M3 — Übungen

Eine Aufgabe mit Grader, eine Messübung am eigenen Rechner und eine Schätzrunde
auf Papier.

---

## Variation — Treppenlauf, Teilaufgabe 3 und 4

**[Treppenlauf](https://soi.ch/contests/2021/round1/stairracing/)** aus der Runde
2021, Teilaufgaben 3 und 4. Teilaufgabe 1 kennst du aus M0, Teilaufgabe 2 aus
M2.

Jetzt stehen beliebig viele Wolkenkratzer auf jeder Seite:

| Teilaufgabe | Schranke | Punkte |
|---|---|---|
| 3 | 1 ≤ N ≤ 1000 | 25 |
| 4 | 1 ≤ N ≤ 100 000 | 25 |

T = 100 in beiden.

**Schätze zuerst, für beide Teilaufgaben getrennt.** Deine allgemeine Lösung aus
M2 hat zwei ineinander liegende Schleifen, ist also O(N²). Rechne aus, wie viele
Schritte das insgesamt gibt, und schlag die Grössenordnung nach. Schreib beides
auf, bevor du irgendetwas startest.

Eine der beiden Teilaufgaben kannst du mit deiner alten Lösung einreichen. Finde
heraus, welche — und lade sie dann auch wirklich hoch. Es sind 25 Punkte, für die
du nichts Neues können musst.

Für die andere Teilaufgabe reicht in diesem Modul die **Diagnose**: Wie viele
Schritte wären es, wie lange würde das dauern, und welche Komplexität bräuchtest
du stattdessen? Die Technik dazu kommt in M4.

!!! tip "Nicht raten, messen"
    Wenn du unsicher bist, ob deine Schätzung stimmt: Bau dir eine eigene
    Eingabedatei mit einem einzigen grossen Testfall und stopp die Zeit. Dann
    rechnest du auf 100 Testfälle hoch. Das ist genauer als jedes Bauchgefühl und
    dauert zwei Minuten.

---

## Verkleidung — die versteckte Bremse

Am Rechner, ohne Grader. Tipp die beiden Programme ab und miss selbst.

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
4. Beschreibe in einem Satz, was das Programm bei jeder einzelnen Zahl tut.

!!! tip "Was du beim Messen erwarten kannst"
    Bei O(N²) brauchen doppelt so viele Elemente rund **viermal** so lange, bei
    O(N) doppelt so lange. Genau messen wirst du das nicht: Bei so grossen
    Listen kommen Speichereffekte dazu, und dein Gerät ist nebenbei mit anderem
    beschäftigt.

    Achte deshalb nicht auf die Sekunden, sondern auf den **Faktor**. Etwa vier
    statt etwa zwei — das ist die Aussage.

Das ist die gefährlichste Sorte Laufzeitproblem: Die teure Stelle sieht aus wie
eine einfache Frage.

??? tip "Wenn du bei Frage 3 feststeckst"
    Überleg, wie Python herausfindet, ob eine Zahl in einer Liste vorkommt. Es
    kennt die Liste nicht auswendig. Was muss es tun?

    Und wie oft muss es das tun, wenn die Antwort „nein" lautet?

---

## Schätzrunde

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
| c | Endurance ST3 | N ≤ 100 000 | ein Durchgang, O(N) |
| d | Gipfel ST3 (2022) | N ≤ 1 000 000 | ein Durchgang, O(N) |
| e | irgendeine Aufgabe | N ≤ 100 | drei Schleifen, O(N³) |

Zeile **d** hat einen Haken, der nicht in der Komplexität steckt. Wenn deine
Antwort dort „O(N) ist immer gut" lautet, lies den Abschnitt über das Einlesen im
Konzept noch einmal.

---

## Lösungen

Erst wenn du es wirklich versucht hast: [Musterlösungen zu M3](loesung.md).
