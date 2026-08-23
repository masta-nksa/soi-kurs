# M5 — Sortieren und Suchen

!!! note "Du kannst hier einsteigen, wenn ..."
    ... du zu einer unbekannten Teilaufgabe aus Schranke, Komplexität und
    Anzahl Testfällen die Grössenordnung der Schritte ausrechnen kannst, und
    zwar bevor du programmierst. Das ist der Inhalt von
    [M3](../m03-laufzeitdenken/index.md).

    **M4 brauchst du hier nicht.** Präfixsummen und Zweizeiger kommen in diesem
    Modul nicht vor. Wer M3 hinter sich hat, kann direkt hier weitermachen.

**In diesem Modul:** [Sortieren als Vorverarbeitung](#sortieren-als-vorverarbeitung)
· [Binäre Suche](#binare-suche)

Bisher hast du die Daten so verarbeitet, wie sie in der Datei standen. Dieses
Modul dreht das um. Manche Probleme werden erst einfach, wenn man die Daten
vorher **umordnet**. Sortieren ist keine Lösung für sich — es ist eine
Vorbereitung, nach der die eigentliche Lösung kurz wird.

---

## Sortieren als Vorverarbeitung

### Worum es geht

Du bestellst Sushi. Jedes Stück hat einen Preis. Es gibt ein Angebot: Wer zu
einem Sushi eine Flasche Sake bestellt, bekommt ein zweites Sushi gratis —
verrechnet wird das **teurere** der beiden Stücke plus der Sake.

Sechs Stücke, Sake gratis:

```
16  42  42  42  16  42
```

Welche Stücke paarst du? Solange die Preise durcheinander liegen, ist das eine
Frage mit vielen Möglichkeiten. Nach dem Sortieren ist es keine Frage mehr.

### Die Idee

> **Kernsatz:** Sortieren verschiebt Arbeit nach vorne. Du investierst einmal
> O(N log N), und danach ist jede einzelne Entscheidung **lokal** — du musst nur
> noch auf die Nachbarn schauen statt auf alle anderen.

Beim Sushi heisst das: Von jedem Paar zahlst du das teurere Stück, das billigere
ist geschenkt. Du willst also, dass die **geschenkten Stücke zusammen möglichst
teuer** sind. Sortierst du absteigend und paarst benachbart, ist jedes
geschenkte Stück das teuerstmögliche.

> **Analogie:** Ein Kartenblatt auf der Hand. Solange die Karten durcheinander
> stecken, musst du für jede Frage — „habe ich etwas Höheres als diese Karte?" —
> das ganze Blatt durchsehen. Einmal nach Wert geordnet, beantwortest du dieselbe
> Frage mit einem Blick auf die Nachbarkarte.
>
> **Bruchstelle:** Ein Kartenblatt ordnet man nach *einem* Kriterium. Sobald
> mehrere Eigenschaften gleichzeitig zählen, sagt dir die Analogie nicht mehr,
> wonach du sortieren sollst — und ob die anderen Eigenschaften dann von selbst
> mitkommen. Genau das ist die Vertiefungsaufgabe dieses Moduls.

### An einem Beispiel

Die sechs Preise, absteigend sortiert:

```
unsortiert:   16  42  42  42  16  42

sortiert:     42  42  |  42  42  |  16  16
Paar:            1    |     2    |     3
zahlst:         42    |    42    |    16     Summe 100
geschenkt:      42    |    42    |    16
```

Rechne gegen: Alle sechs einzeln kosten 200. Geschenkt sind 42 + 42 + 16 = 100,
es bleiben 100. Das ist die Antwort.

Probier von Hand eine andere Paarung, etwa 42 mit 16 und 42 mit 16. Dann sind
nur 16 + 16 = 32 geschenkt, und du zahlst 168. Sortiert paaren ist besser, und
zwar immer.

### Im Code

Python sortiert für dich. Du schreibst nie selbst eine Sortierung.

```python
preise.sort()                  # aufsteigend, aendert die Liste
preise.sort(reverse=True)      # absteigend
kopie = sorted(preise)         # neue Liste, Original bleibt
```

Mehrere Werte, die zusammengehören, packst du in ein **Tupel** — runde Klammern
statt eckige. Sortiert wird dann nach dem ersten Wert, bei Gleichstand nach dem
zweiten und so weiter:

```python
quellen = []
for i in range(N):
    quellen.append((temperatur[i], mineralien[i], i))

quellen.sort()                 # nach Temperatur, bei Gleichstand nach Mineralien
```

Der letzte Eintrag `i` ist ein Handgriff, den du oft brauchst: Er nimmt die
**ursprüngliche Nummer** mit ins Tupel. Ohne ihn weisst du nach dem Sortieren
nicht mehr, welches Element woher kam.

### Laufzeit

`sort()` braucht O(N log N) Schritte. Das `log N` ist der Grund, warum Sortieren
fast immer bezahlbar ist: Bei N = 10 000 ist log₂ N ungefähr 14, also rund
140 000 Schritte statt 100 Millionen.

Die Sushi-Aufgabe mit T = 100 Testfällen:

| Weg | Komplexität | bei N ≤ 10³ | bei N ≤ 10⁴ |
|---|---|---|---|
| jedes Mal das teuerste Stück suchen | O(N²) | 10⁸ — Sekunden | 10¹⁰ — ausgeschlossen |
| einmal sortieren, dann durchlaufen | O(N log N) | 10⁶ | 10⁷ — Sekundenbruchteil |

Beide Zeilen enthalten den Faktor T = 100. Der Sprung von N ≤ 10³ auf N ≤ 10⁴
verzehnfacht die Eingabe, aber verhundertfacht die Arbeit der langsamen Lösung.
Bei O(N log N) wird sie kaum grösser.

!!! note "Wie genau ist das?"
    Wie immer eine Näherung. Ein Schritt beim Sortieren kostet nicht dasselbe wie
    ein einfacher Schleifendurchlauf, und Geräte unterscheiden sich. Zusammen
    leicht eine Grössenordnung. Es geht hier aber um den Unterschied zwischen 10⁷
    und 10¹⁰, und den ändert ein Faktor 3 nicht.

### Woran du es erkennst

Sortieren ist einen Versuch wert, sobald eines davon zutrifft:

- Die **Reihenfolge der Eingabe ist für die Antwort egal**. Dann darfst du
  umordnen, ohne etwas kaputtzumachen.
- Du suchst wiederholt das **Grösste oder Kleinste** unter den noch offenen
  Elementen.
- Die Aufgabe fragt nach **Paaren oder Gruppen** mit möglichst grossen oder
  kleinen Werten.
- Du sollst prüfen, ob es überhaupt eine **Reihenfolge gibt**, die eine Bedingung
  erfüllt.
- Du suchst **Duplikate** oder die zwei Werte mit dem kleinsten Abstand. Nach dem
  Sortieren stehen die Kandidaten nebeneinander.

### Typische Fallen

- **`sort()` ändert die Liste, `sorted()` gibt eine neue zurück.** Wer die
  ursprüngliche Reihenfolge später noch braucht, verliert sie mit `sort()`
  unwiederbringlich.
- **Nach dem Sortieren stimmen die Indizes nicht mehr.** Wenn die Ausgabe die
  ursprünglichen Nummern verlangt, musst du sie vorher ins Tupel packen.
- **Sortieren ist nicht gratis.** Bei einer einzigen Frage an die Daten lohnt es
  sich manchmal nicht, bei vielen Fragen fast immer.
- **Schreib nie selbst eine Sortierung.** Eine handgeschriebene Schleifenlösung
  ist O(N²) und macht die Aufgabe langsamer statt schneller. Wie die fertigen
  Verfahren innen funktionieren, steht unter
  [Sortierverfahren](../hintergrund/sortierverfahren.md) — als Hintergrund, nicht
  zum Nachbauen.

---

## Binäre Suche

!!! note "Dieses Konzept hat keine Ankeraufgabe"
    In den zugänglichen Runden gibt es dafür keine passende SOI-Teilaufgabe. Es
    steht trotzdem hier, weil es zum Sortieren gehört und in der Ersten Runde als
    Quizfrage vorkommen kann. Die Übungen dazu sind Trockenübungen auf Papier.

### Worum es geht

Du hast eine **sortierte** Liste mit einer Million Zahlen und willst wissen, ob
837 291 darin vorkommt. Von vorne durchsuchen heisst im schlimmsten Fall eine
Million Vergleiche.

### Die Idee

> **Kernsatz:** Jeder Vergleich halbiert den Suchraum. Nach k Vergleichen sind
> noch N / 2ᵏ Kandidaten übrig, also genügen log₂ N Vergleiche.

Du schaust in die Mitte. Ist der Wert dort zu klein, kann die gesuchte Zahl nur
rechts liegen — die ganze linke Hälfte ist erledigt, ohne dass du sie angesehen
hast. Das funktioniert nur, weil die Liste sortiert ist.

> **Analogie:** Zahlenraten von 1 bis 100, mit „höher" oder „tiefer" als Antwort.
> Wer immer die Mitte nennt, ist nach sieben Fragen fertig. Wer bei 1 anfängt und
> hochzählt, braucht im schlimmsten Fall hundert.
>
> **Bruchstelle:** Beim Zahlenraten *sagt* dir jemand die Richtung. In der Liste
> musst du sie selbst aus dem Vergleich ablesen — und wenn die Liste nicht
> sortiert ist, sagt der Vergleich gar nichts.

### An einem Beispiel

Gesucht: 37 unter den Zahlen 1 bis 100.

```
links=1   rechts=100   Mitte 50   zu gross   -> rechts = 49
links=1   rechts=49    Mitte 25   zu klein   -> links  = 26
links=26  rechts=49    Mitte 37   gefunden
```

Drei Vergleiche statt siebenunddreissig.

### Im Code

```python
def suche(liste, gesucht):
    links = 0
    rechts = len(liste) - 1
    while links <= rechts:
        mitte = (links + rechts) // 2
        if liste[mitte] == gesucht:
            return mitte
        if liste[mitte] < gesucht:
            links = mitte + 1
        else:
            rechts = mitte - 1
    return -1
```

In der Standardbibliothek steht das fertig als `bisect`. Die Schleife oben ist
trotzdem nützlich, weil man sie umbauen kann, wenn nicht ein Listeneintrag
gesucht ist, sondern die Antwort selbst.

### Laufzeit

O(log N). Bei einer Million Elementen sind das 20 Vergleiche, bei einer Milliarde
30. Die Zahl wächst so langsam, dass sie in einer Aufwandsrechnung praktisch nie
der Engpass ist.

Aufpassen musst du woanders: **Sortieren kostet O(N log N).** Wer einmal sucht,
gewinnt durch vorheriges Sortieren nichts. Wer Q-mal sucht, rechnet
O(N log N + Q log N) gegen O(Q · N).

### Woran du es erkennst

- Die Daten sind sortiert oder lassen sich sortieren, und es kommen **viele
  Anfragen**.
- Die Antwort ist eine Zahl, und du kannst zu einem geratenen Wert leicht prüfen,
  ob er **zu gross oder zu klein** ist. Dann suchst du binär über die Antwort
  statt über eine Liste.

### Typische Fallen

- **Die Liste muss sortiert sein.** Auf unsortierten Daten liefert die Suche
  falsche Ergebnisse, ohne abzustürzen — der übelste Fehlertyp, weil nichts
  auffällt.
- **Endlosschleife.** Wenn `links` oder `rechts` nicht bei jedem Durchgang um
  mindestens eins wandern, läuft die Schleife ewig. Deshalb `mitte + 1` und
  `mitte - 1`, nicht `mitte`.
- **Um eins daneben.** Prüf deine Suche an einer Liste mit einem Element und an
  einer leeren Liste.

---

## Prüfe dich selbst

??? success "Vergleiche deine Antwort — Frage 1"
    **Du löst Sushi Teilaufgabe 4 (N ≤ 10⁴, T = 100), indem du in einer Schleife
    jedes Mal das teuerste verbliebene Stück suchst. Reichst du damit ein?**

    Nein. Die Suche nach dem Maximum kostet O(N), und du machst sie N-mal — also
    O(N²) und damit 10⁸ Schritte pro Testfall. Mal 100 Testfälle sind das 10¹⁰,
    eine halbe Stunde und mehr. Das liegt weit ausserhalb der fünf Minuten.

    Bei Teilaufgabe 2 mit N ≤ 10³ wäre dieselbe Lösung 10⁸ insgesamt und damit
    völlig in Ordnung. Dieselbe Idee, andere Schranke, anderes Urteil — genau
    darum geht es in M3.

??? success "Vergleiche deine Antwort — Frage 2"
    **Deine Ausgabe soll die ursprünglichen Nummern der Elemente enthalten. Nach
    dem Sortieren stimmen die Zahlenwerte, aber die Nummern sind falsch. Was ist
    passiert?**

    Du hast nur die Werte sortiert. Damit ist die Verbindung zwischen Wert und
    ursprünglicher Position verloren — `liste[3]` ist nach dem Sortieren nicht
    mehr das vierte Element der Eingabe.

    Die Nummer muss vor dem Sortieren ins Tupel: `(wert, i)` statt nur `wert`.
    Dann wandert sie mit.

??? success "Vergleiche deine Antwort — Frage 3"
    **Eine Liste mit N Zahlen ist sortiert. Du suchst die zwei Zahlen mit dem
    kleinsten Abstand zueinander. Musst du alle Paare prüfen?**

    Nein, nur die Nachbarn. In einer sortierten Liste liegen die zwei
    ähnlichsten Zahlen zwangsläufig nebeneinander — läge etwas dazwischen, wäre
    der Abstand zu diesem Etwas kleiner.

    Das senkt O(N²) auf O(N) nach dem Sortieren, insgesamt also O(N log N). Das
    ist der Kernsatz in Reinform: Nach dem Sortieren ist die Entscheidung lokal.

??? success "Vergleiche deine Antwort — Frage 4"
    **Du hast N = 10⁶ sortierte Zahlen und beantwortest Q = 10⁵ Anfragen „kommt
    dieser Wert vor?". Wie viele Schritte mit linearer Suche, wie viele mit
    binärer?**

    Linear: Q · N = 10⁵ · 10⁶ = 10¹¹. Ausgeschlossen.

    Binär: Q · log₂ N, also rund 10⁵ · 20 = 2 · 10⁶. Sekundenbruchteil.

    Der Unterschied ist ein Faktor 50 000. Solche Sprünge sind gemeint, wenn es
    heisst, kleine Unterschiede seien egal und grosse tödlich.

---

## Übungen

Weiter geht es mit [den Übungen zu M5](uebungen.md): Sushi Teilaufgabe 2 und 4,
eine versteckte Sortieraufgabe aus der Runde 2022/2023 und zwei Trockenübungen
zur binären Suche.

**Ab diesem Modul arbeitest du mit `vorlage-stufe3.py`.** Du bekommst keine
Leser-Funktionen und keinen fertigen Hauptteil mehr, sondern nur noch die Datei
als Wortliste. Das Einlesen und das Ausgabeformat gehören ab jetzt zur Aufgabe.

---

## Weiter zu M6

Sortieren ordnet nach einem Kriterium und macht Entscheidungen lokal. In M6
kommen zwei Bausteine dazu, die Text und Gitter handhabbar machen —
Zeichenketten und zweidimensionale Felder. Beides taucht im Archiv regelmässig
auf, und beides scheitert selten am Konzept, meist an der Indexrechnung.
<!-- TODO Link setzen, sobald M6 existiert -->
