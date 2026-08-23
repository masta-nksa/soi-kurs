# M4 — Übungen

Drei SOI-Teilaufgaben und zwei Übungen auf Papier. Nach diesem Modul sind sowohl
die Ausdauer als auch der Treppenlauf vollständig gelöst.

!!! note "Du musst nichts nachschlagen"
    Alles zum Lösen steht auf dieser Seite. Auf soi.ch gehst du erst, wenn deine
    Lösung am Beispiel läuft — dort holst du die Eingabedaten, und dann läuft die
    Uhr.

!!! tip "Weiterhin Gerüststufe 2"
    `vorlage-stufe2.py` aus dem Ordner `vorlagen/`. **Achtung, das Einleseformat
    ändert sich**: Bei der Ausdauer stehen pro Testfall jetzt **zwei** Zahlen vor
    der Liste, N und K. Genau dafür ist die Lücke da.

---

## Die Ankeraufgabe: Ausdauer, Teilaufgabe 4 und 5

Wieder dieselbe Strasse mit denselben Löchern. Aber jetzt hat Binna Material
dabei: Sie darf **bis zu K Löcher reparieren**, bevor der Marathon startet.

Wie lang ist die längste Strecke, die sie so hinbekommt?

| Teilaufgabe | Schranken | Punkte | |
|---|---|---|---|
| 1 bis 3 | ohne Reparaturen | 60 | erledigt in M2 und M3 |
| 4 | 1 ≤ N ≤ 100, K = 3 | 20 | **dieses Modul** |
| 5 | 1 ≤ N ≤ 100 000, 1 ≤ K ≤ 100 | 20 | **dieses Modul** |

T = 100 wie immer. Nach diesem Modul sind alle 100 Punkte dieser Aufgabe
erreicht.

**Eingabe.** Erste Zeile T. Pro Testfall: eine Zeile mit **N und K**, dann eine
Zeile mit N Zahlen (`1` = Loch, `0` = heil). Ausgabe wie bisher `Case #i: l`.

```
Eingabe:                        Ausgabe:

2                               Case #0: 10
10 3                            Case #1: 8
0 0 0 1 1 1 0 0 0 0
12 3
0 1 0 0 1 1 0 1 0 0 1 0
```

Im ersten Testfall gibt es genau drei Löcher, und alle drei dürfen repariert
werden — also ist die ganze Strasse befahrbar, Länge 10. Im zweiten liegt die
beste Strecke von Position 2 bis Position 9; dort sind drei Löcher, genau so
viele, wie Binna reparieren kann.

### Einstieg — Teilaufgabe 4 (20 Punkte)

N ≤ 100 und K = 3. Nimm dir **20 Minuten**.

Mach vorher den Schritt aus M3: Schätz für deine Idee die Grössenordnung. Bei
dieser Schranke wirst du merken, dass du grosszügig sein darfst — **jede**
Lösung, die alle Abschnitte durchgeht, reicht hier. Das sind 20 Punkte, ohne
etwas Neues zu können.

??? tip "Hinweis 1 — erst selbst versuchen"
    Formuliere die Aufgabe um, **ohne das Wort „reparieren" zu benutzen**.

    Binna sucht einen Abschnitt. Welche Bedingung muss dieser Abschnitt erfüllen,
    damit er nach der Reparatur befahrbar ist? Schreib den Satz auf, bevor du
    weiterliest.

??? tip "Hinweis 2 — erst selbst versuchen"
    Ein Abschnitt ist brauchbar, wenn er höchstens K Löcher enthält. Welche
    Löcher man repariert, ist keine Entscheidung — es sind alle im Abschnitt.

    Damit ist es die alte Aufgabe mit einer weicheren Bedingung. Deine Lösung aus
    M2 ging alle Abschnitte durch und prüfte „kein Loch". Was musst du daran
    ändern?

??? tip "Hinweis 3 — erst selbst versuchen"
    Statt beim ersten Loch abzubrechen, zählst du die Löcher mit und brichst ab,
    sobald es mehr als K sind.

    Prüf deine Lösung gegen Teilaufgabe 3: Mit K = 0 muss sie exakt dasselbe
    liefern wie vorher.

!!! success "Erst wenn deine Lösung am Beispiel läuft"
    [Ausdauer Teilaufgabe 4 einreichen](https://soi.ch/contests/2025/preround/endurance/#teilaufgabe-4-strasse-flicken-20-punkte)

    Ab dem Klick auf „Eingabedaten herunterladen" hast du fünf Minuten.

### Kern — Teilaufgabe 5 (20 Punkte)

Dieselbe Frage mit N ≤ 100 000 und K ≤ 100. Beispiel und Format sind unverändert.

Rechne zuerst nach, was deine Lösung von Teilaufgabe 4 hier kosten würde. Nimm
dir dann **25 Minuten**.

??? tip "Hinweis 1 — erst selbst versuchen"
    Denk an einen Abschnitt als **Fenster** mit einem linken und einem rechten
    Ende, das höchstens K Löcher enthält.

    Jetzt schiebst du das rechte Ende um eine Position weiter, und dort ist ein
    Loch — es sind K + 1 geworden. Das Fenster ist nicht mehr erlaubt. Was tust
    du?

??? tip "Hinweis 2 — erst selbst versuchen"
    Die eigentliche Frage: Musst du das linke Ende dabei je **nach links**
    bewegen?

    Überleg, warum nicht. Wenn ein Fenster bei einem bestimmten linken Ende schon
    zu viele Löcher hatte, wird es durch ein weiter rechts liegendes rechtes Ende
    nicht besser.

??? tip "Hinweis 3 — erst selbst versuchen"
    Zwei Positionen, beide starten bei 0, dazu ein Zähler für die Löcher im
    Fenster.

    Die äussere Schleife schiebt das rechte Ende Schritt für Schritt nach rechts
    und erhöht den Zähler, wenn dort ein Loch ist. **Solange** der Zähler grösser
    als K ist, schiebst du das linke Ende nach rechts und verringerst den Zähler,
    wenn du dabei über ein Loch hinweggehst.

    Die Länge des Fensters ist `rechts - links + 1`. Vergiss das `+ 1` nicht.

!!! success "Erst wenn deine Lösung am Beispiel läuft"
    [Ausdauer Teilaufgabe 5 einreichen](https://soi.ch/contests/2025/preround/endurance/#teilaufgabe-5-marathon-20-punkte)

    Zwei Kontrollen vorher: Mit K = 0 muss dieselbe Zahl herauskommen wie bei
    Teilaufgabe 3, und auf kleinen Zufallseingaben muss deine neue Lösung mit
    der aus Teilaufgabe 4 übereinstimmen.

---

## Vertiefung — Treppenlauf, Teilaufgabe 4

Die Aufgabe, die du in [M3](../m03-laufzeitdenken/uebungen.md) ausgerechnet und
liegen gelassen hast: N ≤ 100 000, und deine Lösung mit zwei Schleifen bräuchte
10¹² Schritte.

Jetzt hast du das Werkzeug — aber nicht das aus dem Fenster, sondern die andere
Form von „weitergeben statt neu berechnen".

| Teilaufgabe | Schranke | Punkte | |
|---|---|---|---|
| 1 bis 3 | bis N ≤ 1000 | 75 | erledigt in M0, M2 und M3 |
| 4 | 1 ≤ N ≤ 100 000 | 25 | **dieses Modul** |

Zur Erinnerung die gesuchte Grösse: das Maximum von `a[i] + |i − j| + b[j]` über
alle Paare aus einem Wolkenkratzer links und einem rechts.

**Der Weg dorthin ist eine Umformung, keine neue Idee.** Nimm dir **30 Minuten**.

??? tip "Hinweis 1 — erst selbst versuchen"
    Nimm an, der linke Wolkenkratzer steht **links vom** rechten, also `i ≤ j`.
    Wie sieht die Summe dann aus, wenn du den Betrag auflöst?

    Sortier sie so um, dass alles mit `i` auf der einen und alles mit `j` auf der
    anderen Seite steht.

??? tip "Hinweis 2 — erst selbst versuchen"
    Die Summe zerfällt in `(a[i] − i)` und `(b[j] + j)`. Die beiden
    Wolkenkratzer hängen nicht mehr voneinander ab.

    Wenn du für jede Position `j` den besten Partner links davon brauchst — musst
    du dafür jedes Mal neu suchen, oder kannst du das Beste bisher mitführen?

??? tip "Hinweis 3 — erst selbst versuchen"
    Ein Durchgang von links nach rechts. Führ das grösste bisher gesehene
    `a[i] − i` mit und kombinier es an jeder Position `j` mit `b[j] + j`.

    Achte darauf, dass `i ≤ j` gilt — der Partner muss **vor** oder **an** der
    aktuellen Position liegen. Aktualisiere das Maximum also zum richtigen
    Zeitpunkt im Schleifenrumpf.

    Der zweite Fall, bei dem der linke Wolkenkratzer rechts steht, geht genauso:
    Dort ist `|i − j| = i − j`, die Summe wird `(a[i] + i) + (b[j] − j)`, und du
    läufst einmal von rechts nach links. Am Schluss nimmst du das grössere der
    beiden Ergebnisse.

!!! success "Erst wenn deine Lösung am Beispiel läuft"
    [Treppenlauf Teilaufgabe 4 einreichen](https://soi.ch/contests/2021/round1/stairracing/#teilaufgabe-4-eine-lange-strasse-25-punkte)

    Deine neue Lösung muss auf dem Beispiel von Teilaufgabe 3 dasselbe liefern:
    `Case #0: 11`. Und auf zufälligen kleinen Eingaben muss sie mit deiner alten
    O(N²)-Lösung aus M2 übereinstimmen. Zwei Lösungen gegeneinander laufen zu
    lassen ist die zuverlässigste Fehlersuche überhaupt — und du hast hier beide.

---

## Trockenübung 1 — die Frage, die hundertmal gestellt wird

Papier. Kein Programm.

Ein Sportverein hat für **N Tage** die Anzahl verkaufter Tickets notiert. Die
Vereinsleitung stellt **Q Fragen** der Form:

> „Wie viele Tickets wurden zwischen Tag a und Tag b verkauft?"

Es gilt N ≤ 100 000 und Q ≤ 100 000.

1. Wie viele Schritte braucht die naheliegende Lösung, die für jede Frage die
   Tage von a bis b durchzählt? Gib eine Formel in N und Q an und setz die
   Schranken ein.
2. Wie lange dauert das? Nutz die Grössenordnungstabelle aus M3.
3. Beschreib eine Lösung, die jede Frage in **einem** Schritt beantwortet. Was
   musst du dafür vorher tun, und was kostet diese Vorbereitung?
4. Wie viele Schritte sind es insgesamt mit dieser Lösung?
5. Ab wie vielen Fragen lohnt sich die Vorbereitung ungefähr? Begründe mit den
   beiden Formeln, nicht mit Ausprobieren.

Diese Aufgabe sieht nach Addieren aus und ist eine Aufgabe über Vorbereitung.
Genau deshalb steht sie hier.

## Trockenübung 2 — warum zwei Schleifen nicht immer O(N²) sind

Papier. Diese Übung ist der Kern der Vertiefungsspur.

Der Zweizeiger hat eine Schleife in einer Schleife. Im schlimmsten Fall macht die
innere Schleife bei **einem** Durchgang der äusseren fast N Schritte.

1. Konstruier eine Eingabe, bei der die innere Schleife in einem einzigen
   Durchgang tatsächlich sehr viele Schritte macht. Beschreib sie in einem Satz.
2. Zeig trotzdem, dass **über den ganzen Durchlauf** höchstens 2N Schritte
   passieren. Argumentiere über die Bewegungen der beiden Enden, nicht über die
   Schleifen.
3. Formuliere in einem Satz, warum aus 1 und 2 kein Widerspruch wird.

Wenn du das sauber aufschreiben kannst, hast du ein Argument verstanden, das in
der Informatik **amortisierte Analyse** heisst und dir noch oft begegnet.

---

Wenn du eine Aufgabe wirklich versucht hast, findest du die
[Musterlösungen zu M4](loesung.md).
