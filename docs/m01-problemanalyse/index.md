# M1 — Problemanalyse und Modellierung

## Das Problem

Stofl organisiert seine jährliche Käseparty und lädt **N Familien** ein. Zu jeder
Familie gehören zwei Elterntiere und **K Kinder**. Stofl selbst ist auch da.
Jede Maus an der Party möchte **S Stück Käse**.

Wie viele Stück Käse muss Stofl besorgen?

Die Aufgabe heisst **Cheeseparty** und steht in der Vorrunde. So sieht ihre
Leiter aus:

| Teilaufgabe | worum es geht | Punkte | |
|---|---|---|---|
| 1 | Käse berechnen | 50 | **dieses Modul** |
| 2 | eine Rechnung prüfen | 50 | **dieses Modul** |

Beide zusammen sind 100 Punkte — die ganze Aufgabe.

**Teilaufgabe 1.** Gegeben sind N, K und S auf einer Zeile. Gesucht ist die
Anzahl Stück Käse.

```
Eingabe:  4 3 6
Ausgabe:  126
```

**Teilaufgabe 2.** Stofl hat selbst gerechnet und kommt auf **R** Stück. Gegeben
sind jetzt vier Zahlen: N, K, S und R. Gesucht ist `YES`, wenn R stimmt, sonst
`NO`.

```
Eingabe:  4 3 6 120        Eingabe:  4 3 6 126
Ausgabe:  NO               Ausgabe:  YES
```

Schranken: 0 ≤ N, K, S < 100 und 0 ≤ R < 2 000 000.

!!! warning "Diese Aufgabe hat keine Testfälle"
    In M0 gab es eine Zahl T und Zeilen der Form `Case #0: ...`. Hier nicht.
    Cheeseparty liest eine Zeile und schreibt eine Zeile — ohne Präfix.

    Das Ausgabeformat steht in jeder Aufgabenstellung. Übernimm es nie aus der
    Aufgabe von letzter Woche.

!!! note "Du musst nichts nachschlagen"
    Alles zum Lösen steht auf dieser Seite: Geschichte, Format, Schranken und
    Beispiel. Auf soi.ch gehst du erst, wenn deine Lösung am Beispiel läuft —
    dort holst du die Eingabedaten, und dann läuft die Uhr.

---

## Probier es selbst

Nimm dir **20 Minuten**. Erst Teilaufgabe 1, dann Teilaufgabe 2.

Rechne beide Beispiele von Hand nach, bevor du programmierst. Wenn du auf 126
kommst, hast du das Problem verstanden — und wenn nicht, weisst du genau, wo es
klemmt.

??? tip "Kommst du nicht weiter?"
    Dann arbeite dich durch die Hinweise unten, einen nach dem anderen. Nach
    jedem Hinweis probierst du wieder selbst weiter.

    Wenn du beim Einrichten hängst statt beim Denken: Der Ablauf mit
    `loesung.py`, dem Play-Knopf und `bsp_ein.txt` steht in
    [M0 — Werkzeugkasten](../m00-werkzeugkasten/index.md).

!!! success "Erst wenn deine Lösung am Beispiel läuft"
    Dann geht es zum Einreichen:
    [Cheeseparty Teilaufgabe 1](https://soi.ch/contests/2025/preround/cheeseparty/#teilaufgabe-1-50-points)
    und
    [Teilaufgabe 2](https://soi.ch/contests/2025/preround/cheeseparty/#teilaufgabe-2-50-points).
    Die Links springen direkt zur richtigen Teilaufgabe.

    Ab dem Klick auf „Eingabedaten herunterladen" hast du fünf Minuten.

---

## Hinweise

??? tip "Hinweis 1 — erst selbst versuchen"
    Vergiss den Käse für einen Moment.

    Wie viele Mäuse sind an der Party? Schreib die Zahl für N = 4 und K = 3 auf
    ein Blatt Papier, bevor du weiterliest.

??? tip "Hinweis 2 — erst selbst versuchen"
    Setz N = 0. Niemand ist eingeladen. Wie viele Mäuse sind an der Party, und
    wie viel Käse braucht es?

    Wenn deine Rechnung hier 0 ergibt, fehlt jemand.

    > **Analogie:** Du organisierst eine Klassenreise und reservierst Betten. Du
    > zählst die Klasse durch und bestellst genau so viele Betten. In der
    > Jugendherberge stehst du dann mit der Begleitperson im Gang — ihr habt
    > kein Bett.

    Der Fehler steckt nicht im Rechnen. Er steckt in der Frage, wer alles
    dazugehört.

??? tip "Hinweis 3 — erst selbst versuchen"
    Löse die Aufgabe in zwei Schritten statt in einer Formel.

    Bestimm zuerst die Anzahl Mäuse als eigene Zwischengrösse. Der Käse kommt
    danach. Zwei kleine Schritte sind leichter zu prüfen als ein grosser.

??? tip "Hinweis 4 — erst selbst versuchen"
    Zu jeder Familie gehören K + 2 Mäuse: die K Kinder und die beiden
    Elterntiere.

    Stofl kommt einmal dazu — nicht einmal pro Familie.

??? tip "Hinweis 5 — nur bei Implementierungsproblemen"
    Für Teilaufgabe 2 brauchst du keine neue Rechnung.

    Du hast den richtigen Wert bereits ausgerechnet. R ist einfach eine weitere
    Zahl, die du einliest. Was fehlt, ist ein Vergleich und die passende Ausgabe.

    `YES` und `NO` werden gross geschrieben. Ein `Yes` gibt null Punkte.

---

## Das Konzept

### Vom Text zum Modell

Zwischen der Aufgabenstellung und dem Programm liegt ein Schritt, den man leicht
überspringt: das **Modell**. Ein Modell zu bilden heisst, aus dem Text drei
Dinge herauszulesen.

| Frage | Bei Cheeseparty |
|---|---|
| Was ist **gegeben**? | N, K, S — drei Zahlen |
| Was ist **gesucht**? | eine Zahl: Stück Käse |
| Welche **Beziehung** verbindet beides? | jede Maus will S Stück |

Die Beziehung ist der interessante Teil, und sie zerfällt hier in zwei Stufen:

```
Anzahl Mäuse = N · (K + 2) + 1
Anzahl Käse  = Anzahl Mäuse · S
```

Das `+ 1` ist Stofl. Das `+ 2` sind die Eltern. Beide stehen im Aufgabentext,
beide sind leicht zu übersehen, und beide kosten alle 50 Punkte — denn eine
Antwort ist entweder richtig oder falsch.

**Kernsatz:** Der schwierige Teil einer einfachen Aufgabe ist fast nie das
Rechnen. Er ist die Frage, wer oder was alles mitzählt.

### Die Probe am Extremfall

Ein Modell lässt sich prüfen, bevor eine Zeile Code geschrieben ist: Setz die
kleinstmöglichen Werte ein und schau, ob das Ergebnis noch stimmt.

Bei N = 0 ist niemand eingeladen. Trotzdem sitzt Stofl da und will seine S
Stück. Ein Modell, das hier 0 liefert, ist falsch — und das merkst du auf dem
Papier in zehn Sekunden statt nach dem dritten Fehlversuch.

Diese Probe kostet fast nichts und lohnt sich in jeder Aufgabe dieses Kurses.

### Die Analogie und ihre Grenze

> **Analogie:** Betten für die Klassenreise bestellen und die Begleitperson
> vergessen.

Sie trifft die Struktur genau: eine Gruppe wird gezählt, eine einzelne Person
gehört dazu, und der Fehler fällt erst am Schluss auf.

**Bruchstelle:** Die Analogie erklärt den Fehler, nicht die Lösung. Sie sagt dir
nicht, wer in einer *anderen* Aufgabe leicht vergessen geht. Das steht jedes Mal
neu im Text, und es ist nicht immer eine Person — es kann eine Randzeile sein,
ein Zeitpunkt null oder ein leeres Feld. Wer sich merkt „immer plus eins",
rechnet beim nächsten Mal falsch.

### Prüfen ist Rechnen mit einem Vergleich

Teilaufgabe 2 sieht nach einer neuen, schwereren Aufgabe aus: Statt eine Zahl zu
berechnen, soll man beurteilen, ob eine gegebene Zahl stimmt. Viele suchen an
dieser Stelle nach einer Möglichkeit, die Rechnung *rückwärts* laufen zu lassen —
aus R wieder auf N, K und S zu schliessen.

Das ist nicht nötig.

**Kernsatz:** Wer eine Grösse berechnen kann, kann auch prüfen, ob ein gegebener
Wert richtig ist — man rechnet den richtigen Wert aus und vergleicht.

Teilaufgabe 2 ist also Teilaufgabe 1 plus eine Zeile. Diese Umkehrung taucht in
der Olympiade oft auf, und sie ist fast immer der einfachere Weg.

### Laufzeit

Beide Teilaufgaben rechnen ein paar Multiplikationen, unabhängig davon, wie
gross N ist. Das ist **O(1)**, konstante Laufzeit: Die Arbeit wächst nicht mit
der Eingabe.

Geniess es — das bleibt nicht so. Ab M2 hängt die Rechenzeit von den Daten ab,
und ab M3 entscheidet sie über Punkte.

---

## Prüfe dich selbst

??? success "Vergleiche deine Antwort — Frage 1"
    **N = 0, K = 7, S = 3. Wie viele Stück Käse?**

    3 Stück.

    Niemand ist eingeladen, also spielt K keine Rolle. Stofl ist trotzdem da und
    will seine 3 Stück. Wer hier 0 rechnet, hat Stofl vergessen; wer 21 rechnet,
    hat die Kinder einer nicht existierenden Familie mitgezählt.

??? success "Vergleiche deine Antwort — Frage 2"
    **R darf bis 1 999 999 gross sein. Gibt es Werte von R, bei denen die Antwort
    ohne Rechnen schon feststeht?**

    Ja. Der grösstmögliche richtige Wert ist

    ```
    N = 99, K = 99  ->  99 · 101 + 1 = 10 000 Mäuse
    S = 99          ->  10 000 · 99  = 990 000 Stück
    ```

    Jedes R über 990 000 kann nie stimmen. Die Antwort ist dann immer `NO`.

    Für dein Programm ändert das nichts — es rechnet und vergleicht ohnehin. Aber
    das Nachrechnen von Schranken ist eine Gewohnheit, die ab M3 über Punkte
    entscheidet.

??? success "Vergleiche deine Antwort — Frage 3"
    **Du hast Teilaufgabe 1 gelöst. Wie viel Arbeit ist Teilaufgabe 2 noch?**

    Eine zusätzlich eingelesene Zahl, ein Vergleich, und statt der Zahl gibst du
    `YES` oder `NO` aus.

    Wenn deine Antwort „ich muss die Rechnung umkehren" war, dann ist genau das
    die Idee dieses Moduls: Prüfen heisst rechnen und vergleichen, nicht
    rückwärts rechnen.

??? success "Vergleiche deine Antwort — Frage 4"
    **Woher weisst du, ob deine Ausgabe mit `Case #0:` beginnen muss?**

    Ausschliesslich aus dem Ausgabeformat der Aufgabenstellung.

    Cheeseparty hat keine Testfälle und schreibt nur die nackte Zahl. Directions
    auf der nächsten Seite hat T Testfälle und verlangt `Case #0:`, `Case #1:`
    und so weiter. Beides steht dort ausdrücklich.

    Das Format aus der letzten Aufgabe zu übernehmen ist der teuerste Fehler
    dieses Moduls, weil er nichts mit dem Denken zu tun hat.

---

## Übungen

Weiter geht es mit [den Übungen zu M1](uebungen.md): `directions` aus derselben
Vorrunde, eine Trockenübung zum Modellieren und eine Formel, die du widerlegen
sollst.

---

## Weiter zu M2

Wenn du beide Teilaufgaben von Cheeseparty gelöst und die Übungen gemacht hast,
kannst du aus einem Aufgabentext ein Modell bauen und es am Extremfall prüfen.

In [M2 — Vollständige Suche](../m02-vollstaendige-suche/index.md) reicht das
Hinschauen nicht mehr: Dort gibt es keine Formel, sondern nur noch die
Möglichkeit, alle Fälle durchzuprobieren.
