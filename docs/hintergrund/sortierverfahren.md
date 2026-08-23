# Sortierverfahren

!!! warning "Zuerst das Wichtigste"
    **In der SOI schreibst du nie selbst eine Sortierung.** Du rufst `sort()`
    auf. Wer nach dieser Seite Bubble Sort von Hand einbaut, tauscht O(N log N)
    gegen O(N²) und verliert damit unter Umständen genau die Teilaufgabe, für die
    er sortieren wollte.

    Diese Seite erklärt, was innen passiert. Sie ist kein Bauplan.

Warum sie trotzdem dasteht — drei Gründe:

- Sortierverfahren sind das **sauberste Beispiel für Komplexität überhaupt**.
  Dieselbe Aufgabe, dieselbe Ausgabe, und trotzdem liegen zwischen den Verfahren
  Faktoren von tausend. Das lässt sich an keinem anderen Problem so gut zeigen.
- In der **Ersten Runde** können sie als Quizfrage vorkommen. Dort wird nicht
  programmiert, sondern verglichen und geschätzt.
- Eines davon hast du wahrscheinlich schon geschrieben, ohne es zu merken. Wer
  bei [Sushi](../m05-sortieren-und-suchen/uebungen.md) Teilaufgabe 2 in einer
  Schleife jedes Mal das teuerste Stück gesucht hat, hat Selection Sort gebaut.

---

## Die zwei Klassen

Alle Verfahren hier vergleichen Elemente paarweise. Für solche Verfahren gilt
eine bewiesene Untergrenze: **Schneller als O(N log N) geht es nicht.** Die
Verfahren zerfallen damit in zwei Gruppen.

| | Verfahren | Komplexität | bei N = 10 000 |
|---|---|---|---|
| einfach | Selection, Bubble, Insertion | O(N²) | 10⁸ Schritte |
| effizient | Merge, Quick, Timsort | O(N log N) | 1,4 · 10⁵ Schritte |

Der Unterschied ist Faktor 700 — bei N = 10⁶ schon Faktor 50 000. Das ist der
Grund, warum niemand die einfachen Verfahren produktiv einsetzt.

---

## Selection Sort — such das Kleinste, wiederhole

Der naheliegendste Weg. Such das kleinste Element, stell es nach vorne, wiederhol
das mit dem Rest.

```
5  3  8  1  9        kleinstes ist 1  ->  tausche mit Position 0
1  3  8  5  9        kleinstes im Rest ist 3  ->  steht schon richtig
1  3  8  5  9        kleinstes im Rest ist 5  ->  tausche mit Position 2
1  3  5  8  9        kleinstes im Rest ist 8  ->  steht schon richtig
1  3  5  8  9        fertig
```

```python
def selection_sort(liste):
    n = len(liste)
    for i in range(n):
        kleinstes = i
        for j in range(i + 1, n):
            if liste[j] < liste[kleinstes]:
                kleinstes = j
        merker = liste[i]
        liste[i] = liste[kleinstes]
        liste[kleinstes] = merker
```

**Komplexität O(N²), immer.** Die innere Schleife läuft N + (N−1) + ... + 1 mal,
das sind N·(N+1)/2 Schritte. Selection Sort ist auch dann nicht schneller, wenn
die Liste schon sortiert ist — er schaut trotzdem jedes Mal alles an.

---

## Bubble Sort — tausche Nachbarn, bis nichts mehr passiert

Geh durch die Liste und tausche jedes Nachbarpaar, das in falscher Reihenfolge
steht. Wiederhol das, bis ein ganzer Durchgang ohne Tausch bleibt.

```
5  3  8  1  9        5>3 tauschen
3  5  8  1  9        5<8 lassen, 8>1 tauschen
3  5  1  8  9        8<9 lassen        -> ein Durchgang fertig
3  5  1  8  9        5>1 tauschen
3  1  5  8  9                          -> ein Durchgang fertig
1  3  5  8  9        kein Tausch mehr  -> fertig
```

Bei jedem Durchgang wandert das grösste noch unsortierte Element ganz nach
rechts — daher der Name.

```python
def bubble_sort(liste):
    n = len(liste)
    getauscht = True
    while getauscht:
        getauscht = False
        for i in range(n - 1):
            if liste[i] > liste[i + 1]:
                merker = liste[i]
                liste[i] = liste[i + 1]
                liste[i + 1] = merker
                getauscht = True
```

**Komplexität O(N²)** im Normal- und Schlechtfall, O(N) wenn die Liste bereits
sortiert ist (ein Durchgang ohne Tausch). Bubble Sort ist in der Praxis
bedeutungslos und steht hier nur, weil er in jedem Lehrbuch vorkommt und in Quiz
gerne abgefragt wird.

---

## Insertion Sort — einsortieren wie Spielkarten

Nimm ein Element nach dem anderen und schieb es an die richtige Stelle im bereits
sortierten Anfangsstück — genau so, wie man Karten auf der Hand einsortiert.

```
5 | 3  8  1  9       nimm 3, schieb links an 5 vorbei
3  5 | 8  1  9       nimm 8, bleibt stehen
3  5  8 | 1  9       nimm 1, schieb an 8, 5 und 3 vorbei
1  3  5  8 | 9       nimm 9, bleibt stehen
1  3  5  8  9        fertig
```

```python
def insertion_sort(liste):
    for i in range(1, len(liste)):
        aktuell = liste[i]
        j = i - 1
        while j >= 0 and liste[j] > aktuell:
            liste[j + 1] = liste[j]
            j = j - 1
        liste[j + 1] = aktuell
```

**Komplexität O(N²) im Schlechtfall, aber O(N) bei fast sortierten Daten.** Das
ist der interessante Punkt: Wenn jedes Element nur ein paar Positionen wandern
muss, bricht die innere Schleife sofort ab. Genau deshalb steckt Insertion Sort
bis heute in den effizienten Verfahren drin.

---

## Mergesort — teile, sortiere, füge zusammen

Der erste Sprung in die andere Komplexitätsklasse. Die Idee heisst **Teile und
herrsche**:

1. Teile die Liste in der Mitte.
2. Sortiere beide Hälften — nach demselben Verfahren.
3. Füge die beiden sortierten Hälften zusammen.

Schritt 3 ist der eigentliche Trick. Zwei sortierte Listen zusammenzufügen geht
in einem Durchgang: Man schaut nur die beiden vordersten Elemente an und nimmt
das kleinere.

```
Teilen:      5  3  8  1  9  2
             5  3  8   |   1  9  2
             5 | 3  8  |   1 | 9  2
             5 | 3 | 8 |   1 | 9 | 2

Zusammen:    3  5 | 8  |   1 | 2  9
             3  5  8   |   1  2  9
             1  2  3  5  8  9
```

Der letzte Schritt im Detail — zwei sortierte Hälften `3 5 8` und `1 2 9`:

```
vorne stehen 3 und 1  ->  nimm 1        Ergebnis: 1
vorne stehen 3 und 2  ->  nimm 2        Ergebnis: 1 2
vorne stehen 3 und 9  ->  nimm 3        Ergebnis: 1 2 3
vorne stehen 5 und 9  ->  nimm 5        Ergebnis: 1 2 3 5
vorne stehen 8 und 9  ->  nimm 8        Ergebnis: 1 2 3 5 8
nur noch 9 uebrig                       Ergebnis: 1 2 3 5 8 9
```

**Warum O(N log N):** Die Liste lässt sich log₂ N mal halbieren, bis Stücke der
Länge 1 übrig sind. Auf jeder dieser Ebenen wird insgesamt jedes Element genau
einmal angefasst, also N Schritte pro Ebene. Zusammen N · log₂ N.

**Eigenschaften:** immer O(N log N), auch im Schlechtfall. Braucht zusätzlichen
Speicher für die Zwischenlisten. Und er ist **stabil** — dazu unten mehr.

Mergesort ruft sich selbst auf, ist also rekursiv. Rekursion ist in diesem Kurs
kein Thema; für das Verständnis dieser Seite reicht das Bild vom Halbieren.

---

## Quicksort — wähl einen Trennwert und teile auf

Auch Teile und herrsche, aber andersherum. Statt stumpf in der Mitte zu teilen
und beim Zusammenfügen zu arbeiten, wird beim Teilen gearbeitet und das
Zusammenfügen ist gratis.

1. Wähl ein Element als **Trennwert** (Pivot).
2. Sortier die Liste so um, dass links alles Kleinere und rechts alles Grössere
   steht.
3. Verfahr mit beiden Seiten genauso.

```
5  3  8  1  9  2        Trennwert 5

kleiner: 3  1  2   |  5  |   groesser: 8  9
         Trennwert 3               Trennwert 8

         1 | 3 | 2      5      -      8  |  9
         1  2  3        5           8  9

Ergebnis:  1  2  3  5  8  9
```

Nach dem Aufteilen steht der Trennwert bereits an seiner endgültigen Stelle. Am
Schluss muss nichts mehr zusammengefügt werden.

**Komplexität O(N log N) im Mittel, aber O(N²) im Schlechtfall.** Der
Schlechtfall tritt ein, wenn der Trennwert immer der kleinste oder grösste Wert
ist — dann wird die Liste nicht halbiert, sondern nur um eins verkürzt. Bei einer
bereits sortierten Liste und dem ersten Element als Trennwert passiert genau das.

In der Praxis wird der Trennwert deshalb zufällig oder als Median dreier Werte
gewählt. Quicksort ist trotz des Schlechtfalls oft der schnellste, weil er ohne
zusätzlichen Speicher auskommt.

---

## Was Python tatsächlich tut

`liste.sort()` verwendet **Timsort**, benannt nach Tim Peters. Timsort ist ein
Hybrid aus Mergesort und Insertion Sort und nutzt aus, dass echte Daten selten
völlig zufällig sind:

- Er sucht in der Liste nach bereits sortierten Abschnitten und verwendet sie als
  fertige Bausteine.
- Kurze Abschnitte sortiert er mit Insertion Sort — bei wenigen Elementen ist das
  schneller als jedes raffinierte Verfahren.
- Die Bausteine fügt er wie Mergesort zusammen.

**O(N log N) im Schlechtfall, O(N) bei bereits sortierten Daten, stabil.** Für
den Kurs heisst das schlicht: `sort()` ist besser als alles, was du in der
verfügbaren Zeit selbst schreiben könntest.

---

## Stabilität — und warum sie dich betrifft

Ein Sortierverfahren heisst **stabil**, wenn Elemente mit gleichem Sortierwert
ihre ursprüngliche Reihenfolge behalten.

```
Vorher:   (Anna, 3)  (Beat, 1)  (Cem, 3)  (Dina, 1)

stabil nach Zahl:     (Beat, 1)  (Dina, 1)  (Anna, 3)  (Cem, 3)
instabil koennte:     (Dina, 1)  (Beat, 1)  (Cem, 3)  (Anna, 3)
```

Das klingt nach einer Feinheit, ist aber praktisch: Weil Pythons `sort()` stabil
ist, kannst du **nacheinander nach mehreren Kriterien sortieren**. Sortier zuerst
nach dem unwichtigeren, dann nach dem wichtigeren — die Reihenfolge aus dem
ersten Durchgang bleibt innerhalb gleicher Werte erhalten.

Selection Sort und Quicksort sind in ihrer einfachen Form **nicht** stabil,
Insertion Sort, Bubble Sort, Mergesort und Timsort schon.

---

## Übersicht

| Verfahren | Mittel | Schlechtfall | Bestfall | stabil | Speicher |
|---|---|---|---|---|---|
| Selection Sort | O(N²) | O(N²) | O(N²) | nein | O(1) |
| Bubble Sort | O(N²) | O(N²) | O(N) | ja | O(1) |
| Insertion Sort | O(N²) | O(N²) | O(N) | ja | O(1) |
| Mergesort | O(N log N) | O(N log N) | O(N log N) | ja | O(N) |
| Quicksort | O(N log N) | O(N²) | O(N log N) | nein | O(log N) |
| **Timsort** (Python) | O(N log N) | O(N log N) | O(N) | ja | O(N) |

---

## Prüfe dich selbst

??? success "Vergleiche deine Antwort — Frage 1"
    **Eine Liste ist bereits sortiert. Welches der einfachen Verfahren merkt das,
    und welches nicht?**

    Insertion Sort und Bubble Sort merken es und sind dann O(N) — bei Insertion
    Sort bricht die innere Schleife sofort ab, bei Bubble Sort bleibt der erste
    Durchgang ohne Tausch.

    Selection Sort merkt es nicht. Er sucht in jedem Durchgang das Minimum des
    Rests und schaut dafür immer alles an, egal wie die Daten aussehen. O(N²)
    auch bei perfekt sortierter Eingabe.

??? success "Vergleiche deine Antwort — Frage 2"
    **Quicksort ist im Mittel O(N log N), im Schlechtfall O(N²). Wann tritt der
    Schlechtfall ein, und warum ist ausgerechnet eine sortierte Liste gefährlich?**

    Wenn der Trennwert immer das kleinste oder grösste Element ist. Dann landet
    auf einer Seite nichts und auf der anderen alles ausser dem Trennwert — die
    Liste wird um eins kürzer statt halbiert, und das N-mal.

    Bei einer sortierten Liste ist das erste Element immer das kleinste. Wer es
    naiv als Trennwert nimmt, bekommt genau diesen Fall — die scheinbar
    einfachste Eingabe ist die schlechteste.

??? success "Vergleiche deine Antwort — Frage 3"
    **Du hast eine Liste von Tupeln `(nachname, vorname)` und willst nach
    Nachname sortieren, bei gleichem Nachnamen nach Vorname. Warum genügt es,
    zweimal zu sortieren, und in welcher Reihenfolge?**

    Erst nach Vorname, dann nach Nachname.

    Weil Pythons `sort()` stabil ist, bleibt die Vornamen-Reihenfolge innerhalb
    gleicher Nachnamen beim zweiten Sortieren erhalten. Umgekehrt würde der zweite
    Durchgang die Nachnamen-Ordnung zerstören.

    Beim Sortieren von Tupeln braucht man diesen Umweg gar nicht — `sort()`
    vergleicht ohnehin erst das erste, dann das zweite Feld. Nützlich wird die
    Regel, sobald die Kriterien nicht in dieser Reihenfolge im Tupel stehen.

---

Zurück zu [M5 — Sortieren und Suchen](../m05-sortieren-und-suchen/index.md).
