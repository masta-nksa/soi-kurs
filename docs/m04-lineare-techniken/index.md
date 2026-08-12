# M4 — Felder und lineare Techniken

## Das Problem

Wieder dieselbe Strasse mit denselben Löchern. Aber jetzt hat Binna Material
dabei: Sie darf **bis zu K Löcher reparieren**, bevor der Marathon startet.

Wie lang ist die längste Strecke, die sie so hinbekommt?

**Endurance**, Teilaufgabe 4 und 5. Das Eingabeformat ändert sich leicht: In
der ersten Zeile eines Testfalls stehen jetzt zwei Zahlen, N und K.

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

| Teilaufgabe | Schranken | Punkte |
|---|---|---|
| 4 | 1 ≤ N ≤ 100, K = 3 | 20 |
| 5 | 1 ≤ N ≤ 100 000, 1 ≤ K ≤ 100 | 20 |

T = 100 wie immer.

!!! note "Du musst nichts nachschlagen"
    Alles zum Lösen steht auf dieser Seite: Geschichte, Format, Schranken und
    Beispiel. Auf soi.ch gehst du erst, wenn deine Lösung am Beispiel läuft —
    dort holst du die Eingabedaten, und dann läuft die Uhr.

---

## Probier es selbst

Nimm dir **35 Minuten**. Erst Teilaufgabe 4, dann Teilaufgabe 5.

Bevor du programmierst, mach den Schritt aus M3: Schätz für deine Idee die
Grössenordnung, für beide Teilaufgaben getrennt. Bei Teilaufgabe 4 wirst du
merken, dass du grosszügig sein darfst. Bei Teilaufgabe 5 nicht.

!!! tip "Weiterhin Gerüststufe 2"
    `vorlage-stufe2.py` aus dem Ordner `vorlagen/`. Achtung, das Einleseformat
    hat sich geändert — pro Testfall stehen jetzt **zwei** Zahlen vor der Liste.
    Genau dafür ist die Lücke da.

??? tip "Kommst du nicht weiter?"
    Dann arbeite dich durch die Hinweise unten, einen nach dem anderen.

    Wenn du gar nicht erst anfängst, weil dir das Reparieren zu kompliziert
    vorkommt: Hinweis 1 räumt genau das aus dem Weg.

!!! success "Erst wenn deine Lösung am Beispiel läuft"
    Dann geht es zum Einreichen. Die Links springen direkt zur richtigen
    Teilaufgabe:

    - [Endurance Teilaufgabe 4](https://soi.ch/contests/2025/preround/endurance/#teilaufgabe-4-strasse-flicken-20-punkte)
    - [Teilaufgabe 5](https://soi.ch/contests/2025/preround/endurance/#teilaufgabe-5-marathon-20-punkte)

    Ab dem Klick auf „Eingabedaten herunterladen" hast du fünf Minuten.

---

## Hinweise

??? tip "Hinweis 1 — erst selbst versuchen"
    Formuliere die Aufgabe um, **ohne das Wort „reparieren" zu benutzen**.

    Binna sucht einen Abschnitt. Welche Bedingung muss dieser Abschnitt erfüllen,
    damit er nach der Reparatur befahrbar ist? Schreib den Satz auf, bevor du
    weiterliest.

??? tip "Hinweis 2 — erst selbst versuchen"
    > **Analogie:** Im Klassenbuch stehen die Absenzen eines ganzen Jahres. Du
    > darfst drei Fehltage nachträglich entschuldigen lassen. Wie lang ist die
    > längste Strecke ohne unentschuldigte Absenz?

    Nimm ein kleines Beispiel und such die Antwort von Hand:

    ```
    0 1 0 0 1 1 0 1 0 0 1 0     mit K = 3
    ```

    Wie bist du vorgegangen? Vermutlich hast du irgendwo angefangen und nach
    rechts geschaut, bis es zu viele wurden. Genau darum geht es gleich.

??? tip "Hinweis 3 — erst selbst versuchen"
    Denk an einen Abschnitt als **Fenster** mit einem linken und einem rechten
    Ende, das höchstens K Löcher enthält.

    Jetzt schiebst du das rechte Ende um eine Position weiter, und dort ist ein
    Loch — es sind K + 1 geworden. Das Fenster ist nicht mehr erlaubt.

    Was tust du? Und die eigentliche Frage: Musst du dabei das linke Ende je
    **nach links** bewegen?

??? tip "Hinweis 4 — erst selbst versuchen"
    Das linke Ende muss nie zurückwandern.

    Überleg, warum. Wenn ein Fenster bei einem bestimmten linken Ende schon zu
    viele Löcher hatte, wird es durch ein weiter rechts liegendes rechtes Ende
    nicht besser.

??? tip "Hinweis 5 — nur bei Implementierungsproblemen"
    Zwei Positionen, beide starten bei 0, dazu ein Zähler für die Löcher im
    Fenster.

    Die äussere Schleife schiebt das rechte Ende Schritt für Schritt nach rechts
    und erhöht den Zähler, wenn dort ein Loch ist. Solange der Zähler grösser als
    K ist, schiebst du das linke Ende nach rechts und verringerst den Zähler,
    wenn du dabei über ein Loch hinweggehst.

    Die Länge des Fensters ist `rechts - links + 1`. Vergiss das `+ 1` nicht.

---

## Das Konzept

### Zuerst: die Umformulierung

„Bis zu K Löcher reparieren" klingt nach einer Entscheidung, die du treffen
musst: welche Löcher denn? In Wahrheit gibt es nichts zu entscheiden.

> **Ein Abschnitt ist genau dann brauchbar, wenn er höchstens K Löcher enthält.**

Wenn du einen Abschnitt gewählt hast, ist klar, was zu reparieren ist — nämlich
alle Löcher darin. Und wenn es höchstens K sind, reicht dein Material.

Damit ist aus der Aufgabe wieder die alte geworden, nur mit einer weicheren
Bedingung: statt „gar keine Löcher" jetzt „höchstens K Löcher". Für K = 0 ist es
exakt Teilaufgabe 3.

Diese Umformulierung ist der eigentliche Denkschritt — dasselbe Modellieren wie
in M1, nur auf einem Problem, das du schon kennst.

### Drei Lösungen, drei Grössenordnungen

| | Idee | Komplexität | mal T bei N = 100 | bei N = 10⁵ |
|---|---|---|---|---|
| A | alle Abschnitte, Löcher jedes Mal neu zählen | O(N³) | 10⁸ | — |
| B | alle Abschnitte, Löcher in einem Schritt zählen | O(N²) | 10⁶ | 10¹² |
| C | Zweizeiger | O(N) | 10⁴ | 10⁷ |

**Für Teilaufgabe 4 reichen alle drei.** Selbst A landet bei der Grössenordnung
von Sekunden — 20 Punkte, ohne etwas Neues zu können. Für Teilaufgabe 5 bleibt
nur C.

### Präfixsummen: eine Frage in einem Schritt beantworten

Der Schritt von A nach B lohnt sich weit über diese Aufgabe hinaus. Die Frage
lautet: *Wie viele Löcher liegen zwischen Position a und Position b?*

Naiv zählst du sie jedes Mal durch. Stattdessen baust du **einmal** eine
Hilfsliste: `praefix[i]` ist die Anzahl Löcher in den ersten i Positionen.

```
Strasse:      0   1   0   0   1   1   0
praefix:    0   0   1   1   1   2   3   3
```

`praefix` hat ein Element mehr als die Strasse und beginnt mit 0. Damit gilt für
jeden Abschnitt von a bis b (beide eingeschlossen):

```
Anzahl Löcher = praefix[b + 1] - praefix[a]
```

Im Beispiel: Löcher von Position 1 bis 4 sind `praefix[5] - praefix[1]` = 2 − 0 = 2.
Nachzählen: Positionen 1, 2, 3, 4 sind `1 0 0 1` — stimmt.

Die Hilfsliste kostet einmal O(N). Danach ist **jede** Bereichsfrage ein einziger
Schritt statt einer Schleife. Bei Endurance wird daraus O(N²) statt O(N³); wo
viele solche Fragen gestellt werden, ist der Gewinn noch grösser.

### Zweizeiger: das linke Ende wandert nie zurück

Jetzt der Sprung, der Teilaufgabe 5 löst.

Statt alle Abschnitte durchzugehen, führst du ein **Fenster** mit: ein linkes
Ende, ein rechtes Ende, und die Anzahl Löcher darin. Das rechte Ende wandert
Schritt für Schritt über die Strasse. Wird das Fenster ungültig, ziehst du das
linke Ende so weit nach, bis es wieder passt.

Während das läuft, gilt durchgehend:

> **Das Fenster von `links` bis `rechts` enthält höchstens K Löcher, und es ist
> das längste gültige Fenster, das bei `rechts` endet.**

Der zweite Teil ist der entscheidende. Er stimmt, weil das linke Ende nur so weit
vorgerückt ist, wie es musste — keinen Schritt weiter.

**Warum das linke Ende nie zurück muss:** Angenommen, es steht an Position L,
weil weiter links zu viele Löcher lagen. Wenn das rechte Ende nun weiter nach
rechts geht, kommen höchstens Löcher dazu. Ein linkes Ende weiter links war schon
vorher zu viel und ist es jetzt erst recht.

### Warum das O(N) ist, obwohl zwei Schleifen dastehen

Im Code steht eine Schleife in einer Schleife. Trotzdem ist das Verfahren O(N),
und der Grund ist eine schöne Überlegung:

**Zähl nicht die Schleifendurchläufe, sondern die Bewegungen der beiden Enden.**

Das rechte Ende bewegt sich N mal — einmal pro Position. Das linke Ende bewegt
sich ebenfalls höchstens N mal, denn es geht nur nach rechts und kommt nie über
das Ende der Strasse hinaus. Zusammen also höchstens 2N Bewegungen, egal wie sie
sich auf die Durchläufe verteilen.

In einem einzelnen Durchgang kann die innere Schleife durchaus viele Schritte
machen — aber dann macht sie in den übrigen Durchgängen entsprechend weniger. Man
nennt das **amortisiert O(N)**: nicht jeder einzelne Schritt ist billig, aber die
Summe über alle ist es.

### Die Analogie und ihre Grenze

> **Analogie:** Im Klassenbuch die längste Strecke ohne unentschuldigte Absenz
> suchen, wenn du drei Fehltage entschuldigen darfst.

**Bruchstelle:** Die Analogie legt nahe, dass du für jeden Starttag neu
durchzählst. Genau das ist die langsame Lösung — sie erklärt das Problem, nicht
die Lösung.

Dass die Bruchstelle hier der naive Weg ist, macht sie brauchbar: Sie motiviert
den nächsten Schritt, statt ihn vorwegzunehmen. Was die Analogie ausserdem
verschweigt: Der Zweizeiger funktioniert nur, weil die Bedingung **monoton** ist
— ein längeres Fenster hat nie weniger Löcher als ein kürzeres. Bei Bedingungen
ohne diese Eigenschaft hilft er nicht.

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
    **Im Code steht eine Schleife in einer Schleife. Warum ist das trotzdem
    nicht O(N²)?**

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

    Der Zweizeiger lohnt sich, weil Teilaufgabe 5 dieselbe Aufgabe mit N ≤ 100 000
    ist. Du schreibst ihn also einmal und bekommst beide Teilaufgaben — das ist
    dasselbe Muster wie in M2 und M3.

---

## Übungen

Weiter geht es mit [den Übungen zu M4](uebungen.md): Treppenlauf Teilaufgabe 4,
die du in M3 nur diagnostiziert hast, eine versteckte Anwendung von
Präfixsummen und ein kleiner Laufzeitbeweis.

---

## Weiter zu M5

Wenn du Endurance Teilaufgabe 4 und 5 gelöst hast, kennst du zwei Werkzeuge, die
denselben Kern haben: **weitergeben statt neu berechnen**. Präfixsummen geben
Zwischenergebnisse an spätere Fragen weiter, der Zweizeiger gibt das Fenster von
einer Position zur nächsten weiter.

In M5 kommt ein Werkzeug dazu, das anders ansetzt: Manche Probleme werden erst
lösbar, wenn man die Daten vorher **umordnet**. Sortieren ist keine Lösung für
sich, sondern eine Vorbereitung.
<!-- TODO Link setzen, sobald M5 existiert -->
