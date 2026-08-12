# M4 — Übungen

Die Aufgabe, die in M3 offen geblieben ist, dazu zwei Trockenübungen.

---

## Variation — Treppenlauf, Teilaufgabe 4

**[Treppenlauf, Teilaufgabe 4](https://soi.ch/contests/2021/round1/stairracing/#teilaufgabe-4-eine-lange-strasse-25-punkte)**
aus der Runde 2021. Diese hast du in M3 ausgerechnet und liegen gelassen: N ≤ 100 000,
deine Lösung mit zwei Schleifen bräuchte 10¹² Schritte.

Jetzt hast du das Werkzeug.

Zur Erinnerung die gesuchte Grösse: die längste Strecke aus Höhe links, Höhe
rechts und dem Abstand entlang der Strasse zwischen den beiden gewählten
Wolkenkratzern.

**Der Weg dorthin ist eine Umformung, keine neue Idee.** Zwei Fragen führen dich
hin:

1. Nimm an, der linke Wolkenkratzer steht **links vom** rechten, also bei einer
   kleineren Position. Wie sieht die Strecke dann aus, wenn du den Betrag
   auflöst? Sortier die Summe so um, dass alles mit `i` auf der einen und alles
   mit `j` auf der anderen Seite steht.
2. Wenn du für jede Position `j` den besten Partner links davon brauchst — musst
   du dafür jedes Mal neu suchen, oder kannst du das Beste bisher mitführen?

Der zweite Fall, bei dem der linke Wolkenkratzer rechts steht, geht genauso.
Rechne beide getrennt und nimm das grössere Ergebnis.

!!! tip "Prüf dich an der kleinen Teilaufgabe"
    Deine neue Lösung muss auf dem Beispiel von Teilaufgabe 1 dieselben Zahlen
    liefern wie früher: `Case #0: 5` und `Case #1: 1337`. Und sie sollte auf
    zufälligen kleinen Eingaben mit deiner alten Lösung aus M2 übereinstimmen.

    Zwei Lösungen gegeneinander laufen zu lassen ist die zuverlässigste
    Fehlersuche überhaupt — und du hast hier beide.

---

## Verkleidung — die Frage, die hundertmal gestellt wird

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

Diese Aufgabe sieht nach Addieren aus und ist eine Aufgabe über Vorbereitung.
Genau deshalb steht sie hier.

---

## Laufzeitbeweis — warum zwei Schleifen nicht immer O(N²) sind

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

## Lösungen

Erst wenn du es wirklich versucht hast: [Musterlösungen zu M4](loesung.md).
