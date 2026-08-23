# M1 — Problemanalyse und Modellierung

!!! note "Du kannst hier einsteigen, wenn ..."
    ... du den Ablauf „lokal testen → Eingabedaten herunterladen → Ausgabedatei
    hochladen" ohne Anleitung wiederholen kannst und schon einmal Punkte auf
    soi.ch bekommen hast. Das ist der Inhalt von
    [M0](../m00-werkzeugkasten/index.md).

    Wenn dir der Play-Knopf, `EINGABE` und `bsp_ein.txt` nichts sagen, fang dort
    an — sonst geht dieses Modul für Werkzeugfragen drauf statt fürs Denken.

**In diesem Modul:** [Vom Text zum Modell](#vom-text-zum-modell)
· [Die Probe am Extremfall](#die-probe-am-extremfall)
· [Prüfen statt Rechnen](#prufen-statt-rechnen)

Zwischen dem Aufgabentext und dem Programm liegt ein Schritt, den fast alle
überspringen. Er heisst Modellieren, dauert zwei Minuten auf Papier und
entscheidet öfter über Punkte als das Programmieren danach.

Die drei Konzepte hier sind keine Tricks für bestimmte Aufgaben, sondern
Gewohnheiten für alle. Sie kommen in jedem folgenden Modul wieder vor.

---

## Vom Text zum Modell

### Worum es geht

Stofl organisiert ein **Käsefest** und lädt **N Familien** ein. Zu jeder Familie
gehören zwei Elterntiere und **K Kinder**. Stofl selbst ist auch da. Jede Maus
möchte **S Stück Käse**.

Wie viele Stück Käse muss Stofl besorgen?

Die Rechnung ist eine Multiplikation. Trotzdem verlieren an dieser Aufgabe viele
alle 50 Punkte — und zwar nicht beim Rechnen.

### Die Idee

Ein Modell zu bilden heisst, aus dem Text drei Dinge herauszulesen:

| Frage | Beim Käsefest |
|---|---|
| Was ist **gegeben**? | N, K, S — drei Zahlen |
| Was ist **gesucht**? | eine Zahl: Stück Käse |
| Welche **Beziehung** verbindet beides? | jede Maus will S Stück |

> **Kernsatz:** Der schwierige Teil einer einfachen Aufgabe ist fast nie das
> Rechnen. Er ist die Frage, wer oder was alles mitzählt.

> **Analogie:** Du organisierst eine Klassenreise und reservierst Betten. Du
> zählst die Klasse durch und bestellst genau so viele Betten. In der
> Jugendherberge stehst du dann mit der Begleitperson im Gang — ihr habt kein
> Bett.
>
> **Bruchstelle:** Die Analogie erklärt den Fehler, nicht die Lösung. Sie sagt
> dir nicht, wer in einer *anderen* Aufgabe leicht vergessen geht. Das steht
> jedes Mal neu im Text, und es ist nicht immer eine Person — es kann eine
> Randzeile sein, ein Zeitpunkt null oder ein leeres Feld. Wer sich merkt „immer
> plus eins", rechnet beim nächsten Mal falsch.

### An einem Beispiel

Vier Familien, drei Kinder pro Familie, sechs Stück Käse pro Maus.

```
pro Familie:   3 Kinder + 2 Elterntiere      =  5 Mäuse
vier Familien: 4 · 5                         = 20 Mäuse
Stofl dazu:    20 + 1                        = 21 Mäuse
Käse:          21 · 6                        = 126 Stück
```

Das `+ 2` und das `+ 1` stehen beide im Aufgabentext, beide sind leicht zu
übersehen, und beide kosten die vollen 50 Punkte — eine Antwort ist entweder
richtig oder falsch.

Allgemein:

```
Anzahl Mäuse = N · (K + 2) + 1
Anzahl Käse  = Anzahl Mäuse · S
```

### Im Code

Schreib das Modell in **zwei Schritten** hin, nicht als eine Formel:

```python
maeuse = n * (k + 2) + 1
kaese = maeuse * s
```

Das ist nicht bloss Geschmack. Die Zwischengrösse `maeuse` kannst du dir mit
`print` ausgeben lassen und von Hand nachzählen. Bei einer einzeiligen Formel
siehst du nur, dass das Ergebnis falsch ist, nicht wo.

### Wann du es brauchst

Bei jeder Aufgabe, vor der ersten Zeile Code. Die drei Fragen dauern zwei
Minuten.

Woran du merkst, dass du den Schritt übersprungen hast:

- Du fängst an zu tippen und weisst noch nicht, welche Zwischengrössen du
  brauchst.
- Du liest den Aufgabentext beim Programmieren immer wieder nach.
- Dein Programm läuft, liefert aber eine Zahl, die du nicht von Hand
  nachrechnen kannst.

### Typische Fallen

- **Eine Gruppe wird gezählt, ein Einzelner vergessen.** Der Gastgeber, die
  Begleitperson, das Startfeld, der Tag null.
- **Eine Angabe im Text wird für Dekoration gehalten.** „Zu jeder Familie
  gehören zwei Elterntiere" klingt nach Geschichte, ist aber Teil der Rechnung.
- **Direkt zur Formel springen.** Wer die drei Fragen überspringt, merkt einen
  Denkfehler erst, wenn der Grader `WRONG` sagt.

---

## Die Probe am Extremfall

### Worum es geht

Du hast ein Modell. Ist es richtig? Das Beispiel aus der Aufgabenstellung sagt
dir das nur teilweise — es ist ein einziger Fall, und meist ein bequemer.

### Die Idee

> **Kernsatz:** Setz die kleinstmöglichen Werte ein und schau, ob das Ergebnis
> noch stimmt. Ein falsches Modell fällt fast immer schon am Extremfall auf.

Das kostet zehn Sekunden auf Papier und braucht kein Programm.

### An einem Beispiel

Setz beim Käsefest **N = 0**. Niemand ist eingeladen.

```
falsches Modell:   0 · (K + 2) · S        = 0 Stück
richtiges Modell:  (0 · (K + 2) + 1) · S  = S Stück
```

Stofl sitzt trotzdem da und will seine S Stück. Ein Modell, das hier 0 liefert,
ist falsch — und du siehst das, bevor du irgendetwas programmiert hast.

Die üblichen Extremfälle:

| Extremfall | typische Frage |
|---|---|
| N = 0 | Ist überhaupt jemand oder etwas da? |
| N = 1 | Funktioniert es auch ohne Nachbarn, ohne Paare? |
| alle Werte gleich | Kommt dann das heraus, was du erwartest? |
| grösster erlaubter Wert | Passt das Ergebnis noch in die Schranken? |

### Wann du es brauchst

Direkt nach dem Modellieren, vor dem Programmieren. Und nochmals, wenn dein
Programm läuft, aber der Grader nicht zufrieden ist.

Woran du merkst, dass du sie ausgelassen hast: Du testest nur mit dem Beispiel
aus der Aufgabenstellung — und das ist genau der Fall, für den auch ein falsches
Modell oft das Richtige liefert. Die Widerlegungsübung auf der Übungsseite zeigt,
wie leicht das passiert.

### Typische Fallen

- **Den Extremfall nur denken, nicht ausrechnen.** „Das geht schon auf" ist
  keine Probe.
- **Nur nach unten prüfen.** Die obere Schranke ist genauso wichtig, gerade wenn
  eine Antwort in einen bestimmten Bereich passen muss.

---

## Prüfen statt Rechnen

### Worum es geht

Zweiter Teil derselben Aufgabe: Stofl hat selbst gerechnet und kommt auf **R**
Stück. Gegeben sind jetzt vier Zahlen — N, K, S und R. Gesucht ist `YES`, wenn R
stimmt, sonst `NO`.

Das sieht nach einer neuen, schwereren Aufgabe aus. Viele suchen an dieser Stelle
nach einer Möglichkeit, die Rechnung **rückwärts** laufen zu lassen: aus R wieder
auf N, K und S zu schliessen.

### Die Idee

> **Kernsatz:** Wer eine Grösse berechnen kann, kann auch prüfen, ob ein
> gegebener Wert richtig ist — man rechnet den richtigen Wert aus und
> vergleicht.

Rückwärtsrechnen ist nicht nötig und wäre auch gar nicht eindeutig möglich.

> **Analogie:** Jemand behauptet, sein Einkauf habe 43.20 gekostet. Du musst den
> Kassenzettel nicht rückwärts aufrollen. Du rechnest die Posten zusammen und
> vergleichst.
>
> **Bruchstelle:** Das funktioniert, weil hier alles gegeben ist, was zur
> Rechnung nötig ist. Wenn eine Angabe fehlt, wird Prüfen wieder schwierig — und
> es gibt Probleme, bei denen Prüfen viel leichter ist als Rechnen. Das ist eine
> der grossen Fragen der Informatik, aber nicht die Sorge dieses Kurses.

### An einem Beispiel

```
Eingabe:  4 3 6 120        Eingabe:  4 3 6 126
Ausgabe:  NO               Ausgabe:  YES
```

Du rechnest in beiden Fällen 126 aus — genau wie vorher — und vergleichst dann
mit der vierten Zahl.

### Im Code

Teilaufgabe 2 ist Teilaufgabe 1 plus eine Zeile:

```python
maeuse = n * (k + 2) + 1
kaese = maeuse * s

if kaese == r:
    ergebnis = "YES"
else:
    ergebnis = "NO"
```

`YES` und `NO` werden gross geschrieben. Ein `Yes` gibt null Punkte.

### Laufzeit

Ein paar Multiplikationen und ein Vergleich, unabhängig davon, wie gross N ist.
Das ist **O(1)**, konstante Laufzeit: Die Arbeit wächst nicht mit der Eingabe.
Für das ganze Modul gilt dasselbe.

Geniess es — das bleibt nicht so. Ab M2 hängt die Rechenzeit von den Daten ab,
und ab [M3](../m03-laufzeitdenken/index.md) entscheidet sie über Punkte.

### Woran du es erkennst

- Die Aufgabe **gibt dir einen Wert und fragt, ob er stimmt** — statt ihn zu
  verlangen.
- Die Aufgabe fragt nach `YES`/`NO`, `richtig`/`falsch`, `möglich`/`unmöglich`.
- Eine spätere Teilaufgabe dreht eine frühere um. Das ist bei SOI ein häufiges
  Muster, und die Umkehrung ist fast immer der einfachere Weg.

### Typische Fallen

- **Rückwärtsrechnen versuchen.** Der teuerste Irrweg dieser Aufgabe.
- **Das Ausgabeformat vergessen.** Statt einer Zahl kommen jetzt Buchstaben, in
  genau der Schreibweise aus der Aufgabenstellung.

---

## Das Ausgabeformat steht in der Aufgabe

Keine Konzeptfrage, aber der teuerste Fehler dieses Moduls, weil er nichts mit
Denken zu tun hat.

!!! warning "Das Käsefest hat keine Testfälle"
    In M0 gab es eine Zahl T und Zeilen der Form `Case #0: ...`. Hier nicht. Das
    Käsefest liest eine Zeile und schreibt eine Zeile — ohne Präfix.

    Die **Wegbeschreibung** auf der Übungsseite hat wieder T Testfälle und verlangt
    `Case #0:`, nullbasiert. Beides steht jeweils ausdrücklich in der
    Aufgabenstellung.

    **Übernimm das Format nie aus der Aufgabe von letzter Woche.**

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
    das zweite Konzept dieses Moduls: Prüfen heisst rechnen und vergleichen,
    nicht rückwärts rechnen.

??? success "Vergleiche deine Antwort — Frage 4"
    **Eine Aufgabe gibt N Zahlen und fragt nach ihrem Durchschnitt. Welchen
    Extremfall prüfst du zuerst, und was fällt dabei auf?**

    N = 0. Dann teilst du durch null.

    Ob dieser Fall überhaupt vorkommen kann, steht in den Schranken — bei
    `1 ≤ N` nicht. Aber genau das ist der Punkt der Probe: Sie führt dich
    zwangsläufig in die Schranken, und die hast du sonst vielleicht nicht
    gelesen.

---

## Übungen

Weiter geht es mit [den Übungen zu M1](uebungen.md): die **Wegbeschreibung** aus derselben
Vorrunde, **Sushi** als versteckte Modellieraufgabe und eine Formel, die du
widerlegen sollst.

---

## Weiter zu M2

Wenn du beide Teilaufgaben des Käsefests gelöst und die Übungen gemacht hast,
kannst du aus einem Aufgabentext ein Modell bauen und es am Extremfall prüfen.

In [M2 — Vollständige Suche](../m02-vollstaendige-suche/index.md) reicht das
Hinschauen nicht mehr: Dort gibt es keine Formel, sondern nur noch die
Möglichkeit, alle Fälle durchzuprobieren.
