# M4 — Felder und lineare Techniken

!!! note "Du kannst hier einsteigen, wenn ..."
    ... du zu einer unbekannten Teilaufgabe aus Schranke, Komplexität und
    Testfallzahl eine Dauer ausrechnest und begründet entscheidest, ob du damit
    einreichen kannst — **bevor** du programmierst. Das ist der Inhalt von
    [M3](../m03-laufzeitdenken/index.md).

    **Bring deine Lösung von Ausdauer Teilaufgabe 3 mit.** Sie ist der
    Ausgangspunkt und zugleich deine Kontrolle.

**In diesem Modul:** [Präfixsummen](#prafixsummen)
· [Zweizeiger und Fenster](#zweizeiger-und-fenster)

In M3 hast du eine Lösung von O(N²) auf O(N) gebracht, indem du unterwegs etwas
mitgeführt hast statt neu zu rechnen. Das war kein Einzelfall — es ist ein
Muster mit zwei festen Formen, und beide bekommen hier einen Namen.

**Präfixsummen** beantworten viele Fragen nach einer einmaligen Vorbereitung.
**Der Zweizeiger** schiebt ein Fenster über die Daten, ohne je zurückzugehen.
Beide beruhen auf demselben Gedanken: weitergeben statt neu berechnen.

---

## Präfixsummen

### Worum es geht

Du hast eine Reihe von Zahlen und musst immer wieder dieselbe Sorte Frage
beantworten:

> *Wie viele Löcher liegen zwischen Position a und Position b?*

Naiv zählst du sie jedes Mal durch. Bei einer Frage ist das in Ordnung. Bei
tausend Fragen zählst du dieselben Abschnitte tausendmal.

### Die Idee

> **Kernsatz:** Rechne **einmal** eine Hilfsliste aus, in der jeder Eintrag die
> Summe von ganz links bis zu dieser Stelle enthält. Danach ist jede
> Bereichsfrage eine Subtraktion — ein Schritt statt einer Schleife.

`praefix[i]` ist die Anzahl Löcher in den **ersten i** Positionen. Die Liste hat
ein Element mehr als die Strasse und beginnt mit 0.

> **Analogie:** Ein Kilometerzähler im Auto. Er zählt nicht die Länge einzelner
> Etappen, sondern nur die Gesamtstrecke seit dem ersten Tag. Willst du wissen,
> wie weit du zwischen Bern und Chur gefahren bist, liest du zweimal ab und
> ziehst voneinander ab — du musst die Strecke nicht nachfahren.
>
> **Bruchstelle:** Der Kilometerzähler geht nur vorwärts, und genau das ist die
> Voraussetzung: Präfixsummen funktionieren, solange sich die Daten nicht
> ändern. Sobald sich unterwegs ein einzelner Wert ändert, musst du die ganze
> Hilfsliste ab dieser Stelle neu bauen — dann ist der Vorteil weg.

### An einem Beispiel

```
Position:      0   1   2   3   4   5   6
Strasse:       0   1   0   0   1   1   0

praefix:     0   0   1   1   1   2   3   3
Index:       0   1   2   3   4   5   6   7
```

Für jeden Abschnitt von a bis b (beide eingeschlossen) gilt:

```
Anzahl Löcher = praefix[b + 1] - praefix[a]
```

Löcher von Position 1 bis 4: `praefix[5] - praefix[1]` = 2 − 0 = 2.
Nachzählen: Positionen 1, 2, 3, 4 sind `1 0 0 1` — stimmt.

Das `+ 1` und der Startwert 0 sind der Grund, warum die Liste ein Element länger
ist. Wer sie gleich lang macht, muss ständig Sonderfälle für a = 0 behandeln.

### Im Code

```python
def baue_praefix(p):
    praefix = [0]
    summe = 0
    for wert in p:
        summe = summe + wert
        praefix.append(summe)
    return praefix


def bereich(praefix, a, b):
    return praefix[b + 1] - praefix[a]
```

### Laufzeit

Die Hilfsliste kostet einmal **O(N)**. Danach ist **jede** Bereichsfrage **O(1)**.

Bei Q Fragen an N Zahlen:

| | Schritte | |
|---|---|---|
| jede Frage durchzählen | Q · N | O(Q · N) |
| einmal vorbereiten, dann ablesen | N + Q | O(N + Q) |

Bei N = Q = 100 000 ist das der Unterschied zwischen 10¹⁰ und 2 · 10⁵ — und der
Faktor T kommt bei beiden noch dazu.

### Woran du es erkennst

- Die Aufgabe stellt **viele Fragen** nach Summen oder Anzahlen über Bereiche.
- In deiner Lösung steht eine Schleife, die ein Teilstück durchzählt, und diese
  Schleife steckt in einer weiteren Schleife.
- Zwei benachbarte Bereiche **überlappen sich stark** — du rechnest fast dasselbe
  noch einmal.
- Die Daten ändern sich während der Fragen **nicht**.

### Typische Fallen

- **Verrutschen um eins.** Der häufigste Fehler überhaupt. Prüf deine Formel
  immer an einem winzigen Beispiel, bei dem du von Hand nachzählen kannst.
- **Die Hilfsliste gleich lang machen wie die Daten.** Dann brauchst du einen
  Sonderfall für den Bereichsanfang bei 0. Das zusätzliche führende 0-Element
  kostet nichts und spart die Fallunterscheidung.
- **Vorbereiten, obwohl es nur eine Frage gibt.** Dann lohnt es sich nicht — die
  Vorbereitung kostet ja selbst O(N).

---

## Zweizeiger und Fenster

### Worum es geht

Dieselbe Strasse wie in M2 und M3, aber Binna hat jetzt Material dabei: Sie darf
**bis zu K Löcher reparieren**, bevor der Marathon startet. Wie lang ist die
längste Strecke, die sie so hinbekommt?

Der erste Denkschritt hat mit Programmieren nichts zu tun. „Bis zu K Löcher
reparieren" klingt nach einer Entscheidung — welche Löcher denn? In Wahrheit gibt
es nichts zu entscheiden:

> **Ein Abschnitt ist genau dann brauchbar, wenn er höchstens K Löcher enthält.**

Wenn du einen Abschnitt gewählt hast, ist klar, was zu reparieren ist — alle
Löcher darin. Und wenn es höchstens K sind, reicht dein Material. Damit ist aus
der Aufgabe wieder die alte geworden, nur mit einer weicheren Bedingung. Für
K = 0 ist es exakt Teilaufgabe 3.

Das ist dasselbe Modellieren wie in [M1](../m01-problemanalyse/index.md), nur auf
einem Problem, das du schon kennst.

### Die Idee

> **Kernsatz:** Führ ein Fenster mit einem linken und einem rechten Ende mit.
> Das rechte Ende wandert Schritt für Schritt weiter; wird das Fenster ungültig,
> ziehst du das linke Ende nach. **Das linke Ende wandert nie zurück.**

Während das läuft, gilt durchgehend:

> **Das Fenster von `links` bis `rechts` enthält höchstens K Löcher, und es ist
> das längste gültige Fenster, das bei `rechts` endet.**

Der zweite Teil ist der entscheidende. Er stimmt, weil das linke Ende nur so weit
vorgerückt ist, wie es musste — keinen Schritt weiter.

**Warum das linke Ende nie zurück muss:** Angenommen, es steht an Position L,
weil weiter links zu viele Löcher lagen. Wenn das rechte Ende nun weiter nach
rechts geht, kommen höchstens Löcher dazu. Ein linkes Ende weiter links war schon
vorher zu viel und ist es jetzt erst recht.

> **Analogie:** Im Klassenbuch stehen die Absenzen eines ganzen Jahres. Du darfst
> drei Fehltage nachträglich entschuldigen lassen. Wie lang ist die längste
> Strecke ohne unentschuldigte Absenz?
>
> **Bruchstelle:** Die Analogie legt nahe, dass du für jeden Starttag neu
> durchzählst. Genau das ist die langsame Lösung — sie erklärt das Problem, nicht
> die Lösung. Dass die Bruchstelle hier der naive Weg ist, macht sie brauchbar:
> Sie motiviert den nächsten Schritt, statt ihn vorwegzunehmen.
>
> Was sie ausserdem verschweigt: Der Zweizeiger funktioniert nur, weil die
> Bedingung **monoton** ist — ein längeres Fenster hat nie weniger Löcher als ein
> kürzeres. Bei Bedingungen ohne diese Eigenschaft hilft er nicht.

### An einem Beispiel

Die Strasse `0 1 0 0 1 1 0 1 0 0 1 0` mit K = 3. Das Fenster wandert:

Die Tabelle zeigt den Zustand am **Ende** jedes Durchlaufs, also nachdem das
linke Ende gegebenenfalls nachgezogen wurde:

```
rechts  Wert   links   Löcher   Fenster      Länge
   0      0      0       0      [0 ..  0]      1
   1      1      0       1      [0 ..  1]      2
   2      0      0       1      [0 ..  2]      3
   3      0      0       1      [0 ..  3]      4
   4      1      0       2      [0 ..  4]      5
   5      1      0       3      [0 ..  5]      6
   6      0      0       3      [0 ..  6]      7
   7      1      2       3      [2 ..  7]      6     links nachgezogen 0 -> 2
   8      0      2       3      [2 ..  8]      7
   9      0      2       3      [2 ..  9]      8     <- beste
  10      1      5       3      [5 .. 10]      6     links nachgezogen 2 -> 5
  11      0      5       3      [5 .. 11]      7
```

Die beste Länge ist 8, von Position 2 bis 9.

Zwei Dinge lohnen einen zweiten Blick. Erstens: Das linke Ende geht nur vorwärts,
0 → 2 → 5, und insgesamt fünf Schritte über den ganzen Durchlauf. Zweitens: In
der Spalte „Löcher" steht nie mehr als 3 — genau das ist die Invariante, und sie
gilt am Ende jedes Durchlaufs.

### Im Code

```python
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
```

Die Länge ist `rechts - links + 1`. Vergiss das `+ 1` nicht.

### Laufzeit

**O(N)** — obwohl eine Schleife in einer Schleife steht. Der Grund ist eine
schöne Überlegung:

**Zähl nicht die Schleifendurchläufe, sondern die Bewegungen der beiden Enden.**

Das rechte Ende bewegt sich N mal, einmal pro Position. Das linke Ende bewegt
sich ebenfalls höchstens N mal, denn es geht nur nach rechts und kommt nie über
das Ende der Strasse hinaus. Zusammen höchstens 2N Bewegungen, egal wie sie sich
auf die Durchläufe verteilen.

In einem einzelnen Durchgang kann die innere Schleife durchaus viele Schritte
machen — aber dann macht sie in den übrigen entsprechend weniger. Man nennt das
**amortisiert O(N)**: nicht jeder einzelne Schritt ist billig, aber die Summe
über alle ist es.

Zum Vergleich, bei T = 100 Testfällen:

| | Idee | Komplexität | bei N = 100 | bei N = 10⁵ |
|---|---|---|---|---|
| A | alle Abschnitte, Löcher jedes Mal neu zählen | O(N³) | 10⁸ | — |
| B | alle Abschnitte, Löcher per Präfixsumme | O(N²) | 10⁶ | 10¹² |
| C | Zweizeiger | O(N) | 10⁴ | 10⁷ |

**Für Teilaufgabe 4 reichen alle drei.** Selbst A landet bei der Grössenordnung
von Sekunden — 20 Punkte, ohne etwas Neues zu können. Für Teilaufgabe 5 bleibt
nur C.

### Woran du es erkennst

- Du suchst den **längsten oder kürzesten zusammenhängenden Abschnitt**, der eine
  Bedingung erfüllt.
- Die Bedingung ist **monoton**: Wenn ein Fenster sie verletzt, verletzt jedes
  längere sie auch.
- Du hast eine O(N²)-Lösung, die alle Paare aus linkem und rechtem Ende
  durchgeht.
- Beim Verschieben des rechten Endes um eins ändert sich am Fensterinhalt nur
  **ein** Element.

Der zweite Punkt ist die Bedingung, ohne die es nicht geht. Prüf ihn, bevor du
programmierst.

### Typische Fallen

- **Das `+ 1` bei der Länge.** Von Position 2 bis 9 sind es 8 Positionen, nicht
  7.
- **Die Reihenfolge im Schleifenrumpf.** Erst das neue Element aufnehmen, dann
  nachziehen, dann messen. Wer zuerst misst, misst ein ungültiges Fenster.
- **`if` statt `while` beim Nachziehen.** Ein einzelner Schritt reicht nicht
  immer — bei K = 0 und mehreren Löchern hintereinander muss das linke Ende
  mehrfach vorrücken.
- **Monotonie nicht geprüft.** Wenn ein längeres Fenster die Bedingung auch mal
  wieder erfüllen kann, liefert der Zweizeiger falsche Ergebnisse, ohne
  abzustürzen.

---

## Prüfe dich selbst

??? success "Vergleiche deine Antwort — Frage 1"
    **Was liefert deine Zweizeiger-Lösung, wenn K = 0 ist?**

    Genau das Ergebnis von Teilaufgabe 3 — den längsten Abschnitt ganz ohne
    Löcher.

    Bei K = 0 wird das linke Ende sofort hinter jedes Loch nachgezogen, das
    Fenster enthält also nie eines. Das ist eine gute Kontrolle: Wenn deine neue
    Lösung mit K = 0 nicht dasselbe liefert wie die alte, ist irgendwo ein
    Fehler.

??? success "Vergleiche deine Antwort — Frage 2"
    **Im Code steht eine Schleife in einer Schleife. Warum ist das trotzdem nicht
    O(N²)?**

    Weil man nicht die Verschachtelung zählt, sondern die Bewegungen.

    Das rechte Ende geht N Schritte nach rechts, das linke höchstens N. Keines
    geht je zurück. Zusammen sind das höchstens 2N Bewegungen über den ganzen
    Durchlauf — unabhängig davon, wie ungleich sie verteilt sind.

    Bei O(N²) dagegen würde die innere Schleife für **jeden** äusseren Durchlauf
    wieder von vorne beginnen. Genau das tut sie hier nicht.

??? success "Vergleiche deine Antwort — Frage 3"
    **Die Strasse ist `1 0 1 1 0`. Wie sieht `praefix` aus, und wie viele Löcher
    liegen zwischen Position 1 und 3?**

    ```
    Strasse:      1   0   1   1   0
    praefix:    0   1   1   2   3   3
    ```

    Löcher von 1 bis 3: `praefix[4] - praefix[1]` = 3 − 1 = 2.

    Nachzählen: Positionen 1, 2, 3 sind `0 1 1` — zwei Löcher. Stimmt.

    Der häufigste Fehler ist ein Verrutschen um eins. Prüf deine Formel immer an
    einem winzigen Beispiel, bei dem du von Hand nachzählen kannst.

??? success "Vergleiche deine Antwort — Frage 4"
    **Teilaufgabe 4 hat N ≤ 100. Lohnt sich der Zweizeiger dort überhaupt?**

    Für die Punkte nicht — für dich schon.

    Bei N ≤ 100 gibt selbst die dreifach geschachtelte Lösung volle 20 Punkte.
    Wer sie hat, soll sie einreichen und nicht warten.

    Der Zweizeiger lohnt sich, weil Teilaufgabe 5 dieselbe Aufgabe mit
    N ≤ 100 000 ist. Du schreibst ihn also einmal und bekommst beide
    Teilaufgaben — dasselbe Muster wie in M2 und M3.

??? success "Vergleiche deine Antwort — Frage 5"
    **Du suchst den längsten Abschnitt, in dem die Summe der Werte *genau* 100
    ist. Werte dürfen auch negativ sein. Funktioniert der Zweizeiger?**

    Nein. Die Bedingung ist nicht monoton.

    Bei negativen Werten kann ein längeres Fenster eine **kleinere** Summe haben
    als ein kürzeres. Das rechte Ende weiterzuschieben macht die Lage also nicht
    zwangsläufig schlechter, und damit gilt das Argument nicht mehr, dass das
    linke Ende nie zurück muss.

    Bei ausschliesslich positiven Werten wäre es dagegen wieder monoton, und der
    Zweizeiger funktioniert. Diese Prüfung gehört vor jede Anwendung.

---

## Übungen

Weiter geht es mit [den Übungen zu M4](uebungen.md): Ausdauer Teilaufgabe 4 und
5, Treppenlauf Teilaufgabe 4, die du in M3 nur diagnostiziert hast, eine
versteckte Anwendung von Präfixsummen und ein kleiner Laufzeitbeweis.

---

## Weiter zu M5

Wenn du Ausdauer Teilaufgabe 4 und 5 gelöst hast, kennst du zwei Werkzeuge mit
demselben Kern: **weitergeben statt neu berechnen**. Präfixsummen geben
Zwischenergebnisse an spätere Fragen weiter, der Zweizeiger gibt das Fenster von
einer Position zur nächsten weiter.

In [M5 — Sortieren und Suchen](../m05-sortieren-und-suchen/index.md) kommt ein
Werkzeug dazu, das anders ansetzt: Manche Probleme werden erst lösbar, wenn man
die Daten vorher **umordnet**. Sortieren ist keine Lösung für sich, sondern eine
Vorbereitung.
