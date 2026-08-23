# M1 — Übungen

Drei SOI-Aufgaben und eine Trockenübung. Alle drei geben echte Punkte.

!!! note "Du musst nichts nachschlagen"
    Alles zum Lösen steht auf dieser Seite: Geschichte, Format, Schranken und
    Beispiel. Auf soi.ch gehst du erst, wenn deine Lösung am Beispiel läuft —
    dort holst du die Eingabedaten, und dann läuft die Uhr.

!!! tip "Gerüststufe 1"
    `vorlage.py` aus dem Ordner `vorlagen/`. Das Einlesen und das Schreiben der
    Ausgabe sind fertig; du füllst nur `loese` aus.

    **Achtung beim Käsefest:** Diese Aufgabe hat keine Testfälle und kein
    `Case #i:`. Die Vorlage ist auf das übliche Format eingerichtet — hier musst
    du den Hauptteil anpassen. Genau hinschauen lohnt sich, das ist der Fehler
    Nummer eins in diesem Modul.

!!! note "Auch alte Runden zählen"
    Für jede archivierte Aufgabe lassen sich weiterhin Eingabedaten erzeugen und
    Ausgabedateien prüfen. Der Ablauf ist derselbe wie in M0: lokal testen,
    herunterladen, `EINGABE` umstellen, hochladen. Auch die fünf Minuten gelten.
    Was fehlt, ist nur die Rangliste. Das Feedback bekommst du.

---

## Einstieg — Käsefest

Die Ankeraufgabe des Moduls, aus der laufenden Vorrunde. Auf soi.ch heisst sie
**Käsefest**, in der Adresszeile `cheeseparty`.

| Teilaufgabe | worum es geht | Punkte | |
|---|---|---|---|
| 1 | Käse berechnen | 50 | **dieses Modul** |
| 2 | eine Rechnung prüfen | 50 | **dieses Modul** |

Beide zusammen sind 100 Punkte — die ganze Aufgabe.

Stofl lädt **N Familien** ein. Zu jeder Familie gehören zwei Elterntiere und
**K Kinder**. Stofl selbst ist auch da. Jede Maus möchte **S Stück Käse**.

Schranken: 0 ≤ N, K, S < 100 und 0 ≤ R < 2 000 000.

### Teilaufgabe 1 — Käse berechnen (50 Punkte)

Gegeben sind N, K und S auf einer Zeile. Gesucht ist die Anzahl Stück Käse.

```
Eingabe:  4 3 6
Ausgabe:  126
```

Nimm dir **10 Minuten**. Rechne das Beispiel von Hand nach, bevor du
programmierst. Wenn du auf 126 kommst, hast du das Problem verstanden — und
wenn nicht, weisst du genau, wo es klemmt.

??? tip "Hinweis 1 — erst selbst versuchen"
    Vergiss den Käse für einen Moment.

    Wie viele Mäuse sind an der Party? Schreib die Zahl für N = 4 und K = 3 auf
    ein Blatt Papier, bevor du weiterliest.

??? tip "Hinweis 2 — erst selbst versuchen"
    Setz N = 0. Niemand ist eingeladen. Wie viele Mäuse sind an der Party, und
    wie viel Käse braucht es?

    Wenn deine Rechnung hier 0 ergibt, fehlt jemand.

??? tip "Hinweis 3 — erst selbst versuchen"
    Zu jeder Familie gehören K + 2 Mäuse: die K Kinder und die beiden
    Elterntiere. Stofl kommt **einmal** dazu — nicht einmal pro Familie.

    Bestimm die Anzahl Mäuse als eigene Zwischengrösse und rechne den Käse erst
    danach. Zwei kleine Schritte sind leichter zu prüfen als ein grosser.

!!! success "Erst wenn deine Lösung am Beispiel läuft"
    [Käsefest Teilaufgabe 1 einreichen](https://soi.ch/contests/2025/preround/cheeseparty/#teilaufgabe-1-50-points)

    Ab dem Klick auf „Eingabedaten herunterladen" hast du fünf Minuten.
    Hochgeladen wird nur die Ausgabedatei, nie dein Programm.

### Teilaufgabe 2 — eine Rechnung prüfen (50 Punkte)

Stofl hat selbst gerechnet und kommt auf **R** Stück. Gegeben sind jetzt vier
Zahlen: N, K, S und R. Gesucht ist `YES`, wenn R stimmt, sonst `NO`.

```
Eingabe:  4 3 6 120        Eingabe:  4 3 6 126
Ausgabe:  NO               Ausgabe:  YES
```

Nimm dir **10 Minuten**.

??? tip "Hinweis 1 — erst selbst versuchen"
    Musst du wirklich aus R zurückrechnen, was N, K und S waren?

    Überleg zuerst, ob es einen Weg gibt, der ohne Rückwärtsrechnen auskommt.

??? tip "Hinweis 2 — erst selbst versuchen"
    Du hast den richtigen Wert bereits ausgerechnet — in Teilaufgabe 1.

    R ist einfach eine weitere Zahl, die du einliest.

??? tip "Hinweis 3 — erst selbst versuchen"
    Was fehlt, ist ein Vergleich und eine andere Ausgabe.

    `YES` und `NO` werden gross geschrieben. Ein `Yes` gibt null Punkte.

!!! success "Erst wenn deine Lösung am Beispiel läuft"
    [Käsefest Teilaufgabe 2 einreichen](https://soi.ch/contests/2025/preround/cheeseparty/#teilaufgabe-2-50-points)

---

## Kern — Wegbeschreibung

Aus derselben Vorrunde, auf soi.ch **Wegbeschreibung**, in der Adresszeile
`directions`. Dieselbe Denkarbeit wie beim Käsefest, andere Oberfläche: Statt
Zahlen zu zählen, vergleichst du Zeichenketten.

Binna und Stofl haben sich verirrt und je eine Wegbeschreibung aus lauter `l`
und `r` bekommen. Stofl hat ein schlechtes Gedächtnis und die **letzten**
Anweisungen womöglich vergessen. Stimmt das, woran er sich erinnert, mit dem
**Anfang** von Binnas Beschreibung überein?

Formell: Gib `YES` aus, wenn Stofls Zeichenkette ein **Präfix** von Binnas
Zeichenkette ist, sonst `NO`.

| Teilaufgabe | Schranken | Punkte | |
|---|---|---|---|
| 1 | \|b\| = \|s\|, beide ≤ 100 | 20 | **dieses Modul** |
| 2 | \|s\| = 1, \|b\| ≤ 100 | 20 | **dieses Modul** |
| 3 | \|b\|, \|s\| ≤ 100, sonst nichts | 60 | **dieses Modul** |

T = 100 in allen Teilaufgaben.

**Eingabe.** Erste Zeile T. Pro Testfall zwei Zeilen: zuerst Binnas Zeichenkette
`b`, dann Stofls Zeichenkette `s`.

**Ausgabe.** Pro Testfall eine Zeile `Case #i: YES` oder `Case #i: NO`.

!!! danger "Achtung, das Format wechselt"
    Anders als das Käsefest hat die Wegbeschreibung eine Anzahl Testfälle T, und
    jede Ausgabezeile beginnt mit `Case #0:`, `Case #1:` und so weiter.
    Nullbasiert.

### Teilaufgaben 1 und 2 (je 20 Punkte)

Zwei geschenkte Sonderfälle. In Teilaufgabe 1 sind beide Beschreibungen gleich
lang, in Teilaufgabe 2 hat Stofl sich nur an **ein einziges** Zeichen erinnert.

```
Teilaufgabe 1                   Teilaufgabe 2

Eingabe:      Ausgabe:          Eingabe:        Ausgabe:
3             Case #0: NO       3               Case #0: YES
rrlr          Case #1: YES      llrlrr          Case #1: NO
rrrr          Case #2: NO       l               Case #2: YES
lrrrl                           llrlrr
lrrrl                           r
rrll                            rrl
llrr                            r
```

Nimm dir **15 Minuten** für beide. Stell dir zuerst die drei Fragen — was ist
gegeben, was ist gesucht, welche Beziehung verbindet beides.

??? tip "Hinweis 1 — erst selbst versuchen"
    Es lohnt sich, kurz zu überlegen, ob du die beiden Teilaufgaben wirklich
    getrennt lösen musst.

    Schreib die Bedingung hin, die in **beiden** Fällen gelten muss. Sind das
    zwei verschiedene Bedingungen oder ist es dieselbe?

??? tip "Hinweis 2 — erst selbst versuchen"
    Vergleiche die Zeichen an Position 0, 1, 2 und so weiter — so viele, wie
    Stofls Beschreibung lang ist.

    Bei Teilaufgabe 1 sind das alle, bei Teilaufgabe 2 genau eines. Dieselbe
    Schleife.

??? tip "Hinweis 3 — erst selbst versuchen"
    Sobald ein Zeichenpaar nicht übereinstimmt, steht die Antwort fest — du
    musst nicht weitersuchen.

    Achte auf die Ausgabe: hier mit `Case #i:` davor, nullbasiert.

!!! success "Erst wenn deine Lösung am Beispiel läuft"
    - [Wegbeschreibung Teilaufgabe 1](https://soi.ch/contests/2025/preround/directions/#teilaufgabe-1-sehr-gutes-gedachtnis-20-punkte)
    - [Teilaufgabe 2](https://soi.ch/contests/2025/preround/directions/#teilaufgabe-2-sehr-schlechtes-gedachtnis-20-punkte)

### Teilaufgabe 3 — der allgemeine Fall (60 Punkte)

Jetzt fallen beide geschenkten Annahmen weg: Beide Beschreibungen sind
irgendwie lang, zwischen 1 und 100 Zeichen.

```
Eingabe:            Ausgabe:

4                   Case #0: YES
rrlrl               Case #1: NO
rrl                 Case #2: NO
lrrrl               Case #3: YES
llrr
lr
lrrr
llrr
llrr
```

Die Schranken bleiben klein, es geht also nicht um Geschwindigkeit. Verschärft
wird auf einer anderen Achse: **vom Spezialfall zum allgemeinen Fall.** Hier
zeigt sich, ob dein Modell den allgemeinen Fall trifft oder nur die Sonderfälle.

Nimm dir **15 Minuten**.

??? tip "Hinweis 1 — erst selbst versuchen"
    Schau dir Testfall 2 im Beispiel an: Binna hat `lr`, Stofl hat `lrrr`.
    Stofl erinnert sich an **mehr**, als Binna überhaupt aufgeschrieben hat.

    Was macht deine Lösung aus Teilaufgabe 1 in diesem Fall?

??? tip "Hinweis 2 — erst selbst versuchen"
    Dieser Fall muss `NO` ergeben — Stofls Beschreibung kann kein Anfang von
    Binnas sein, wenn sie länger ist.

    Prüf das, **bevor** du anfängst, Zeichen zu vergleichen. Sonst greifst du in
    der Schleife über das Ende von Binnas Zeichenkette hinaus.

??? tip "Hinweis 3 — erst selbst versuchen"
    Zwei Bedingungen zusammen: Stofls Beschreibung darf nicht länger sein, und
    alle ihre Zeichen müssen mit dem Anfang von Binnas übereinstimmen.

    Wenn du deine Lösung von Teilaufgabe 1 um die Längenprüfung ergänzt, löst
    sie alle drei Teilaufgaben auf einmal.

!!! success "Erst wenn deine Lösung am Beispiel läuft"
    [Wegbeschreibung Teilaufgabe 3 einreichen](https://soi.ch/contests/2025/preround/directions/#teilaufgabe-3-allgemeiner-fall-60-punkte)

    Prüf vorher gegen: Deine neue Lösung muss auf den Beispielen von
    Teilaufgabe 1 und 2 weiterhin dasselbe liefern.

---

## Vertiefung — Sushi

**Sushi** aus der Runde 2018. Hier steht nirgends, dass es ums Modellieren geht.

Stofl bestellt Sushi. Es gibt ein Angebot: Wer eine Flasche Sake dazu bestellt,
bekommt ein zweites Sushi geschenkt — bezahlt werden das teurere der beiden
Sushi und die Flasche. Gesucht ist der kleinstmögliche Gesamtpreis.

| Teilaufgabe | Schranken | Punkte | |
|---|---|---|---|
| 1 | N = 2, S = 0 | 10 | **dieses Modul** |
| 2 | grössere Bestellung | 30 | M5 |
| 3 | N = 2, 0 ≤ S ≤ 10³ | 10 | **dieses Modul** |
| 4 | grössere Bestellung, Sake kostet | 50 | M5 |

Beschränke dich auf **Teilaufgabe 1** (zwei Sushi, Sake gratis) und
**Teilaufgabe 3** (zwei Sushi, Sake kostet etwas). Teilaufgabe 2 und 4 brauchen
ein Werkzeug, das du erst in M5 bekommst.

**Eingabe.** Erste Zeile T. Pro Testfall zwei Zeilen: zuerst N und S, dann N
Preise. **Ausgabe.** Pro Testfall `Case #i: P` mit dem minimalen Gesamtpreis.

```
Teilaufgabe 1                   Teilaufgabe 3

Eingabe:      Ausgabe:          Eingabe:      Ausgabe:
2             Case #0: 42       1             Case #0: 58
2 0           Case #1: 100      2 32
16 42                           16 42
2 0
100 64
```

Die Aufgabe klingt nach Optimierung, nach Ausprobieren, nach etwas Grösserem.
Ist sie nicht. Nimm dir **20 Minuten**.

??? tip "Hinweis 1 — erst selbst versuchen"
    Bei genau zwei Sushi: Wie viele verschiedene Arten zu bestellen gibt es
    überhaupt?

    Schreib sie alle hin. Es sind nicht viele.

??? tip "Hinweis 2 — erst selbst versuchen"
    Zwei Möglichkeiten: beide einzeln bezahlen, oder das Angebot nutzen.

    Rechne für das Beispiel `16 42` mit S = 32 beide Preise aus und vergleiche.

??? tip "Hinweis 3 — erst selbst versuchen"
    Du hast zwei Zahlen und nimmst die kleinere. Mehr ist es nicht.

    Bei Teilaufgabe 1 mit S = 0 gewinnt immer dieselbe Möglichkeit — überleg
    kurz, welche, und ob dein Programm das automatisch richtig macht.

!!! success "Erst wenn deine Lösung am Beispiel läuft"
    - [Sushi Teilaufgabe 1](https://soi.ch/contests/2018/round1/sushi/#teilaufgabe-1-happy-hour-10-punkte)
    - [Teilaufgabe 3](https://soi.ch/contests/2018/round1/sushi/#teilaufgabe-3-die-happy-hour-vorbei-10-punkte)

??? tip "Die Runde 2018 heisst „First Round" — bin ich hier richtig?"
    Ja. Die SOI hat 2025 die Namen geändert. Was damals „First Round" hiess, ist
    nach heutiger Zählung die **Zweite Runde** — also eigentlich zu schwer für
    diesen Kurs.

    Die ersten Teilaufgaben sind trotzdem gut lösbar. Genau darum picken wir
    einzelne heraus und nicht ganze Runden. Lass dich vom Namen nicht
    einschüchtern.

---

## Trockenübung — stimmt diese Formel?

Papier. Kein Programm.

Zwei Mitschülerinnen haben das Käsefest gelöst und kommen auf verschiedene
Formeln:

```
Anna:  Käse = (N · K + 1) · S
Bea:   Käse = (N · (K + 2)) · S
```

Beide sind falsch.

1. Sag bei jeder Formel, **wen** sie vergisst.
2. Beide liefern beim Beispiel `4 3 6` etwas anderes als 126, fallen also sofort
   auf. Finde für **jede** Formel Eingaben, bei denen sie trotzdem das richtige
   Ergebnis liefert.
3. Was sagt dir das über das Testen mit dem mitgelieferten Beispiel?

Die dritte Frage ist die eigentliche. Nimm dir dafür einen Moment.

---

Wenn du eine Aufgabe wirklich versucht hast, findest du die
[Musterlösungen zu M1](loesung.md).
