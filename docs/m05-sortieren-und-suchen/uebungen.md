# M5 — Übungen

Drei SOI-Aufgaben und zwei Trockenübungen. Die ersten beiden sind dieselbe
Aufgabe in zwei Schwierigkeitsstufen, die dritte ist Sortieren in Verkleidung.

!!! note "Du musst nichts nachschlagen"
    Alles zum Lösen steht auf dieser Seite: Geschichte, Format, Schranken und
    Beispiel. Auf soi.ch gehst du erst, wenn deine Lösung am Beispiel läuft —
    dort holst du die Eingabedaten, und dann läuft die Uhr.

!!! tip "Neu: Gerüststufe 3"
    `vorlage-stufe3.py` aus dem Ordner `vorlagen/`. Du bekommst die Datei als
    Wortliste, sonst nichts. Leser, Hauptteil und Ausgabezeilen schreibst du
    selbst. Die Merkliste im Kopf der Vorlage sagt dir, was dazugehört.

---

## Die Aufgabe: Sushi

Maus Stofl ist in einem Sushi-Restaurant in Tsukuba und bestellt für die ganze
Schweizer Delegation. Heute gibt es ein Spezialangebot: **Wer zu einem Sushi eine
Flasche Sake bestellt, bekommt ein zweites Sushi gratis.** Verrechnet werden das
teurere der beiden Stücke und die Flasche Sake.

Insgesamt werden N Stück Sushi bestellt, das i-te kostet pᵢ Yen. Eine Flasche
Sake kostet S Yen. Gesucht ist der minimale Gesamtpreis.

| Teilaufgabe | Schranken | Punkte | |
|---|---|---|---|
| 1 | N = 2, S = 0 | 10 | erledigt in M1 |
| 2 | 1 ≤ N ≤ 10³, S = 0 | 30 | **dieses Modul** |
| 3 | N = 2, 0 ≤ S ≤ 10³ | 10 | erledigt in M1 |
| 4 | 1 ≤ N ≤ 10⁴, 0 ≤ S ≤ 10⁵ | 50 | **dieses Modul** |

T = 100 wie immer. Nach diesem Modul sind alle 100 Punkte dieser Aufgabe
erreicht.

**Eingabe.** Die erste Zeile enthält die Anzahl Testfälle T. Jeder Testfall
besteht aus zwei Zeilen: zuerst N und S, dann N Preise pᵢ.

**Ausgabe.** Pro Testfall eine Zeile `Case #i: P` mit dem minimalen Gesamtpreis.
`Case #i` ist nullbasiert — der erste Testfall ist `Case #0`.

---

### Einstieg — Teilaufgabe 2 (30 Punkte)

Die Happy Hour läuft, Sake ist gratis (S = 0). Es geht nur noch darum, richtig
zu paaren.

Schranken: 1 ≤ N ≤ 10³, S = 0, 1 ≤ pᵢ ≤ 10³.

```
Eingabe:                        Ausgabe:

1                               Case #0: 100
6 0
16 42 42 42 16 42
```

Nimm dir **20 Minuten**. Rechne vorher aus, wie viele Schritte deine Idee
braucht — bei dieser Schranke darfst du grosszügig sein.

??? tip "Hinweis 1 — erst selbst versuchen"
    Von jedem Paar zahlst du das teurere Stück. Das billigere ist geschenkt.

    Dreh die Frage um: Statt zu überlegen, was du zahlst, überleg, was du
    **geschenkt bekommst**. Welche Stücke sollen möglichst teuer sein?

??? tip "Hinweis 2 — erst selbst versuchen"
    Nimm die sechs Preise aus dem Beispiel und probier von Hand drei
    verschiedene Paarungen durch. Schreib jedes Mal auf, was geschenkt ist.

    Bei welcher Paarung ist die Summe der geschenkten Stücke am grössten? Und was
    haben die gepaarten Stücke dort gemeinsam?

??? tip "Hinweis 3 — erst selbst versuchen"
    Sortier absteigend und paar die Nachbarn: erstes mit zweitem, drittes mit
    viertem und so weiter.

    Überleg, warum das nicht besser geht. Wenn du das teuerste Stück mit etwas
    Billigerem paarst als dem zweitteuersten, verschenkst du weniger — und das
    zweitteuerste Stück musst du dann irgendwo anders unterbringen.

!!! success "Erst wenn deine Lösung am Beispiel läuft"
    [Sushi Teilaufgabe 2 einreichen](https://soi.ch/contests/2018/round1/sushi/#teilaufgabe-2-mehr-sushi-30-punkte)

    Ab dem Klick auf „Eingabedaten herunterladen" hast du fünf Minuten.
    Hochgeladen wird nur die Ausgabedatei, nie dein Programm.

---

### Kern — Teilaufgabe 4 (50 Punkte)

Die Happy Hour ist vorbei, Sake kostet jetzt Geld. Und es sind weitere
Delegationen dazugekommen.

Schranken: 1 ≤ N ≤ 10⁴, 0 ≤ S ≤ 10⁵, 1 ≤ pᵢ ≤ 10⁵.

```
Eingabe:                        Ausgabe:

1                               Case #0: 180
6 32
16 42 42 42 16 42
```

Dieselben Preise wie oben, nur kostet die Flasche jetzt 32. Das Ergebnis steigt
von 100 auf 180 — und nicht bloss um dreimal 32.

Nimm dir **25 Minuten**. Zwei Dinge ändern sich gegenüber Teilaufgabe 2, und du
solltest beide vorher benennen können.

??? tip "Hinweis 1 — erst selbst versuchen"
    Ein Paar zu bilden ist jetzt nicht mehr immer gut.

    Rechne für ein einzelnes Paar aus zwei Stücken aus: Was kostet es gepaart,
    was kostet es einzeln? Ab wann lohnt sich das Paar?

??? tip "Hinweis 2 — erst selbst versuchen"
    Das Paar lohnt sich genau dann, wenn das **billigere** der beiden Stücke mehr
    kostet als die Flasche Sake.

    Du gehst deine absteigend sortierte Liste von vorne durch. Wenn ein Paar sich
    nicht mehr lohnt — was weisst du dann über alle Stücke, die noch kommen?

??? tip "Hinweis 3 — erst selbst versuchen"
    Die zweite Änderung ist die Schranke. N ≤ 10⁴ bei T = 100.

    Rechne beide Wege durch: einmal mit einer Schleife, die jedes Mal das
    teuerste verbliebene Stück sucht, und einmal mit einmaligem Sortieren. Einer
    der beiden ist bei dieser Schranke ausgeschlossen — und bei Teilaufgabe 2 war
    er es noch nicht.

!!! success "Erst wenn deine Lösung am Beispiel läuft"
    [Sushi Teilaufgabe 4 einreichen](https://soi.ch/contests/2018/round1/sushi/#teilaufgabe-4-mehrere-delegationen-50-punkte)

    Prüf vorher mit S = 0 gegen: Deine neue Lösung muss dann dasselbe liefern wie
    die aus Teilaufgabe 2. Das ist die billigste Kontrolle, die du bekommen
    kannst.

---

## Vertiefung — Thermalquellen, Teilaufgabe 1 (20 Punkte)

**[Thermalquellen](https://soi.ch/contests/2023/round1/thermalsprings/#teilaufgabe-1-alle-quellen-20-punkte)**
aus der Runde 2022/2023. Hier steht nirgends etwas von Sortieren.

Maus Binna wandert durch Ungarn und badet in Thermalquellen. Damit die Reise in
einem Höhepunkt endet, soll **jede Quelle strikt besser sein als die
vorhergehende**: höhere Temperatur, höherer Mineralanteil, **weniger**
Schwefelgeruch und mehr Panorama.

Teilaufgabe 1 fragt: Kann Binna in **allen** Quellen baden? Wenn ja, in welcher
Reihenfolge?

**Eingabe.** Erste Zeile T. Pro Testfall: eine Zeile mit N, dann vier Zeilen mit
je N Zahlen — Temperatur tᵢ, Mineralien mᵢ, Schwefelgeruch sᵢ, Panorama pᵢ.

**Ausgabe.** Pro Testfall eine Zeile `Case #t: YES` oder `Case #t: NO`. Bei
`YES` folgt **eine weitere Zeile** mit N Zahlen: die Reihenfolge der Quellen,
nummeriert von 0 bis N−1.

Schranken: T = 100, 1 ≤ N ≤ 300, alle Werte zwischen 1 und 10⁹.

```
Eingabe:              Ausgabe:

4                     Case #0: YES
2                     1 0
2 1                   Case #1: NO
2 1                   Case #2: YES
1 2                   1 2 0
2 1                   Case #3: NO
2
1 2
1 2
1 2
1 2
3
9 4 7
8 2 3
12 44 13
5 1 4
3
1 1 1
2 2 2
3 3 3
4 4 4
```

!!! warning "Das Ausgabeformat hat es in sich"
    Die Anzahl Zeilen pro Testfall ist nicht fest — bei `NO` eine, bei `YES`
    zwei. Das Muster „eine Zeile pro Testfall" trägt hier nicht mehr. Genau
    dafür ist Gerüststufe 3 da.

Nimm dir **30 Minuten**.

??? tip "Hinweis 1 — erst selbst versuchen"
    Angenommen, es gibt eine gültige Reihenfolge. Was gilt dann zwangsläufig für
    die **Temperaturen** entlang dieser Reihenfolge?

    Und wenn du das beantwortet hast: Wie viele Reihenfolgen kommen dann
    überhaupt noch als Kandidaten in Frage?

??? tip "Hinweis 2 — erst selbst versuchen"
    Es gibt nur einen einzigen Kandidaten. Damit zerfällt die Aufgabe in zwei
    Teile, die beide leicht sind: den Kandidaten herstellen und ihn prüfen.

    Beim Prüfen gehst du einmal durch und vergleichst jede Quelle mit ihrer
    Vorgängerin. Vorsicht bei der dritten Eigenschaft — sie läuft andersherum.

??? tip "Hinweis 3 — erst selbst versuchen"
    Zwei Stolpersteine, an denen die meisten hängenbleiben:

    Erstens: Was passiert, wenn zwei Quellen **dieselbe** Temperatur haben? Die
    Bedingung heisst „strikt besser", nicht „mindestens so gut".

    Zweitens: Ausgegeben werden die **ursprünglichen Nummern** der Quellen, nicht
    ihre Werte. Nach dem Sortieren weisst du die nur noch, wenn du vorgesorgt
    hast.

---

## Trockenübung 1 — wann lohnt sich Sortieren?

Papier. Kein Programm.

Ein Programm bekommt N Zahlen und beantwortet danach Q Fragen der Form „kommt
der Wert x vor?".

1. Wie viele Schritte braucht die naheliegende Lösung, die für jede Frage die
   ganze Liste durchsucht? Gib eine Formel in N und Q an.
2. Wie viele Schritte braucht die Lösung, die zuerst sortiert und dann binär
   sucht? Auch als Formel.
3. Setz N = 10⁵ und Q = 10⁵ ein. Welche Lösung gewinnt, und um welchen Faktor?
4. Setz N = 10⁵ und Q = 1 ein. Welche gewinnt jetzt?
5. Ab welcher Grössenordnung von Q lohnt sich das Sortieren ungefähr? Begründe
   mit den beiden Formeln, nicht mit Ausprobieren.

## Trockenübung 2 — binär suchen ohne Liste

Papier. Kein Programm.

Ein Verlag will N Bücher auf K Regale verteilen. Die Bücher stehen in fester
Reihenfolge und dürfen nicht umsortiert werden; jedes Regal bekommt einen
zusammenhängenden Block. Gesucht ist eine Verteilung, bei der das **am
schwersten beladene Regal so leicht wie möglich** ist.

1. Angenommen, jemand nennt dir eine Zahl G und behauptet: „Es geht mit höchstens
   G Gewicht pro Regal." Wie prüfst du das in einem Durchgang durch die Bücher?
   Beschreib das Verfahren in zwei bis drei Sätzen.
2. Wenn es mit G geht — geht es dann auch mit G + 1? Und wenn es mit G nicht
   geht, kann es mit G − 1 gehen?
3. Die Antwort auf Frage 2 ist der Grund, warum man hier binär suchen kann,
   obwohl es gar keine sortierte Liste gibt. Erklär in einem Satz, worüber genau
   die binäre Suche läuft.
4. Zwischen welchen beiden Werten musst du suchen? Nenn eine untere und eine
   obere Schranke, die sicher stimmen.

---

Wenn du eine Aufgabe wirklich versucht hast, findest du die
[Musterlösungen zu M5](loesung.md).
