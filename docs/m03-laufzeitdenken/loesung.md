# M3 — Musterlösungen

Diese Seite verrät die Lösung. Hast du es wirklich selbst versucht?

---

## Einstieg — Treppenlauf, Teilaufgabe 3

**Die Rechnung ist die ganze Aufgabe.** Deine Lösung aus M2 hat zwei Schleifen,
also O(N²):

| | N | pro Testfall | mal T = 100 | Grössenordnung | |
|---|---|---|---|---|---|
| ST3 | 1 000 | 10⁶ | 10⁸ | Sekunden | **läuft** |
| ST4 | 100 000 | 10¹⁰ | 10¹² | Tage | ausgeschlossen |

**Teilaufgabe 3 reichst du mit deiner alten Lösung ein.** Ein paar Sekunden sind
lang genug, dass du dich fragst, ob etwas hängt — und kurz genug, dass es
innerhalb der fünf Minuten völlig unproblematisch ist. 25 Punkte, ohne eine
Zeile neuen Code.

Das ist die praktische Seite des Moduls: Laufzeitdenken sagt dir nicht nur, wann
du aufhören musst, sondern auch, wann du **weitermachen darfst**. Wer bei 10⁸
Schritten reflexhaft nach einer besseren Lösung sucht, verschenkt Zeit.

Falls du die Lösung nicht mehr hast — sie steht bei den
[Musterlösungen zu M2](../m02-vollstaendige-suche/loesung.md).

---

## Kern — Ausdauer, Teilaufgabe 3

**Die Schätzung zuerst.** Die Lösung aus M2 hat zwei Schleifen, also O(N²). Mit
N = 100 000 sind das 10¹⁰ Schritte pro Testfall und mal T = 100 insgesamt 10¹².
Grössenordnung: Tage. Die alte Lösung scheidet aus, und das weisst du in zwei
Minuten auf Papier — ohne sie je gestartet zu haben.

**Der Durchgang.** Eine Schleife über die Strasse, zwei Zahlen im Gepäck:

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
    laenge = 0
    for i in range(n):
        if p[i] == 1:
            laenge = 0
        else:
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

Der Unterschied zu M2 ist eine einzige gestrichene Schleife. Statt für jeden
Startpunkt neu zu zählen, wird `laenge` weitergereicht und nur bei einem Loch
zurückgesetzt.

Der Vergleich `if laenge > bestes` steht **ausserhalb** des `else`. Sonst geht
nichts kaputt, aber es ist eine Falle weniger: So kann der Fall „die Strasse
endet ohne Loch" gar nicht erst schiefgehen.

**Dieses Programm löst Teilaufgabe 1, 2 und 3** — zusammen 60 Punkte. Wenn du in
M2 schon eingereicht hast, kommen jetzt 20 dazu.

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

Prüf zusätzlich `1 1 1` (Antwort 0) und eine Strasse ganz ohne Löcher.

??? tip "Wo die Zeit hingeht"
    Mit der grösstmöglichen Eingabe — 100 Testfälle zu je 100 000 Zahlen —
    stehen zehn Millionen Zahlen in der Datei. Zwei Teile kosten Zeit, und beide
    sind O(N · T), also 10⁷ Schritte:

    - die zehn Millionen Zahlen lesen und umwandeln
    - der Durchgang deines Algorithmus

    Der Algorithmus ist damit nicht mehr der teuerste Teil, sondern gleichauf —
    beim Messen liegt das Einlesen sogar vorn. Das ist ein gutes Zeichen: Wenn
    das Einlesen mithält, ist bei der Rechnung nichts mehr zu holen.

    Insgesamt bleibt es bei der Grössenordnung von Sekunden.

---

## Vertiefung — Treppenlauf, Teilaufgabe 4 diagnostizieren

**1. und 2.** 10⁵ · 10⁵ = 10¹⁰ Schritte pro Testfall, mal T = 100 sind das 10¹².
Grössenordnung: Tage. Ausgeschlossen.

**3.** Nötig wäre **O(N)** oder O(N log N). Bei O(N) und N = 10⁵ sind es
10⁵ · 100 = 10⁷ Schritte, also rund eine Sekunde.

**4. Die Umformung.** Gesucht ist das Maximum von

```
a[i] + |i − j| + b[j]
```

über alle Paare. Nimm an, der linke Wolkenkratzer steht links vom rechten, also
`i ≤ j`. Dann ist `|i − j| = j − i`, und die Summe wird zu

```
a[i] + (j − i) + b[j]   =   (a[i] − i)  +  (b[j] + j)
```

**Das ist der entscheidende Schritt.** Links steht nur noch etwas, das von `i`
abhängt, rechts nur noch etwas, das von `j` abhängt. Die beiden Wolkenkratzer
sind entkoppelt.

Damit brauchst du keine zwei Schleifen mehr: Geh einmal von links nach rechts,
führ das grösste bisher gesehene `a[i] − i` mit und kombinier es an jeder
Position `j` mit `b[j] + j`. Das ist ein Durchgang, also O(N).

Den Fall, bei dem der linke Wolkenkratzer rechts vom rechten steht (`i > j`),
rechnest du genauso — dort ist `|i − j| = i − j`, die Summe wird
`(a[i] + i) + (b[j] − j)`, und du läufst einmal von rechts nach links. Am Schluss
nimmst du das grössere der beiden Ergebnisse.

Diese Technik heisst **das Beste bisher mitführen** und ist eine Form von
„weitergeben statt neu berechnen". In
[M4](../m04-lineare-techniken/index.md) wird sie ausgeführt, dort löst du
Teilaufgabe 4 dann auch wirklich.

---

## Trockenübung 1 — die versteckte Bremse

**1. und 2. Die Messung.** Deine Sekundenwerte sind andere als die deiner
Nachbarin — darauf kommt es nicht an. Entscheidend ist der **Faktor** zwischen
den beiden Läufen.

Bei doppelt so vielen Zahlen wirst du ungefähr das **Vierfache** an Zeit sehen,
oft auch mehr. Doppelt so lange wäre O(N), viermal so lange ist O(N²). Also
verhält sich das Programm quadratisch, obwohl nur eine Schleife dasteht.

(Dass es oft mehr als das Vierfache wird, liegt an Speichereffekten bei grossen
Listen. Die Zählung sagt N²/2 Schritte voraus; die Wirklichkeit ist etwas
schlechter. Für das Urteil „quadratisch" spielt das keine Rolle.)

**3. Die versteckte Schleife** steht hier:

```python
    if zahl not in gesehen:
```

Python kennt den Inhalt der Liste nicht auswendig. Um `not in` zu beantworten,
geht es die Liste **von vorne bis hinten durch** und vergleicht jedes Element.
Ist die Antwort „nein, kommt nicht vor", wurde die ganze Liste angeschaut.

Diese eine Zeile ist also eine vollständige Schleife über `gesehen`. Da sie für
jede der N Zahlen ausgeführt wird und `gesehen` mitwächst, sind es insgesamt
rund N²/2 Vergleiche.

**4. Mit einem `set`:**

```python
import random
import time

zahlen = []
for i in range(20000):
    zahlen.append(random.randint(1, 1000000))

start = time.time()

gesehen = set()
for zahl in zahlen:
    gesehen.add(zahl)

print("Verschiedene:", len(gesehen))
print("Dauer:", time.time() - start)
```

Der Faktor beim Verdoppeln fällt von etwa vier auf etwa **zwei** — das ist die
Signatur von O(N). Und die absolute Dauer sinkt bei diesen Grössen um eine
Grössenordnung und mehr.

Die Abfrage `if zahl not in gesehen` kann ganz entfallen: Ein set speichert
jeden Wert ohnehin nur einmal.

---

## Trockenübung 2 — Schätzrunde

| | Schritte insgesamt | Grössenordnung | Urteil |
|---|---|---|---|
| a | 10³ · 10³ · 100 = 10⁸ | Sekunden | einreichen |
| b | 10⁵ · 10⁵ · 100 = 10¹² | Tage | ausgeschlossen |
| c | 10⁵ · 100 = 10⁷ | rund eine Sekunde | einreichen |
| d | 10⁶ · 100 = 10⁸ | Sekunden — **aber siehe unten** | prüfen! |
| e | 100³ · 100 = 10⁸ | Sekunden | einreichen |

**Zeile e ist die Überraschung.** Drei ineinander liegende Schleifen klingen nach
Katastrophe, aber bei N ≤ 100 sind es genau gleich viele Schritte wie in Zeile a.
Die Komplexität allein sagt nichts — erst zusammen mit der Schranke.

**Zeile d ist die Falle.** Die Komplexität ist in Ordnung: O(N) bei N = 10⁶ macht
10⁸ Schritte, also Sekunden. Das Problem steht woanders.

Bei N = 10⁶ und T = 100 stehen **hundert Millionen Zahlen** in der Eingabedatei.
Das sind mehrere hundert Megabyte. Deine Vorlage liest die ganze Datei ein und
zerlegt sie in Wörter — und diese Wortliste braucht ein Vielfaches der
Dateigrösse an Arbeitsspeicher. Zum Vergleich: Ausdauer Teilaufgabe 3 kommt auf
zehn Millionen Zahlen und rund 20 Megabyte, und das läuft problemlos.

Praktische Konsequenz, und sie kostet nichts: **Schau nach dem Download auf die
Dateigrösse.** Eine Eingabedatei von 200 MB ist ein Warnsignal, bevor du
überhaupt startest. Wenn die echten Testdaten kleiner ausfallen als der
schlimmste erlaubte Fall, ist alles gut — aber das siehst du erst an der Datei,
nicht an der Aufgabenstellung.

Die allgemeine Lehre aus dieser Zeile: **Die Grösse der Eingabe ist Teil der
Laufzeit.** Eine perfekte O(N)-Lösung hilft nicht, wenn N Zahlen einzulesen schon
zu lange dauert.

---

Zurück zu [den Übungen](uebungen.md) oder zum
[Lernbaustein](index.md).
