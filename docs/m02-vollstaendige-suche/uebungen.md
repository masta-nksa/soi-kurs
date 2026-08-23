# M2 — Übungen

Zwei SOI-Aufgaben und drei Übungen auf Papier. Die Papierübungen sind kein
Ersatz — sie üben genau das, was beim blossen Einreichen wegfällt.

!!! note "Du musst nichts nachschlagen"
    Alles zum Lösen steht auf dieser Seite: Geschichte, Format, Schranken und
    Beispiel. Auf soi.ch gehst du erst, wenn deine Lösung am Beispiel läuft —
    dort holst du die Eingabedaten, und dann läuft die Uhr.

!!! tip "Gerüststufe 1"
    `vorlage.py` aus dem Ordner `vorlagen/`. Leser und Hauptteil sind fertig, du
    füllst `loese` aus. Beide Aufgaben hier haben Testfälle und `Case #i:` —
    die Vorlage passt also ohne Umbau.

!!! note "Auch alte Runden zählen"
    Für jede archivierte Aufgabe lassen sich weiterhin Eingabedaten erzeugen und
    Ausgabedateien prüfen. Der Ablauf ist derselbe wie in M0: lokal testen,
    herunterladen, `EINGABE` umstellen, hochladen. Auch die fünf Minuten gelten.
    Was fehlt, ist nur die Rangliste.

---

## Die Ankeraufgabe: Ausdauer

Aus der laufenden Vorrunde, auf soi.ch **Ausdauer**, in der Adresszeile
`endurance`. Diese Aufgabe begleitet dich durch drei Module.

Binna organisiert einen Marathon. Die Strasse ist in **N** Abschnitte
unterteilt; `1` bedeutet Loch, `0` heile Strasse. Gelaufen wird nur auf einem
zusammenhängenden Stück ohne Loch. Gesucht ist die Länge des längsten solchen
Stücks.

| Teilaufgabe | Schranke | Punkte | |
|---|---|---|---|
| 1 | N = 3 | 20 | **dieses Modul** |
| 2 | 1 ≤ N ≤ 100 | 20 | **dieses Modul** |
| 3 | 1 ≤ N ≤ 100 000 | 20 | M3 |
| 4 | mit einer zusätzlichen Regel | 20 | M4 |
| 5 | mit einer zusätzlichen Regel | 20 | M4 |

T = 100 in allen Teilaufgaben.

**Eingabe.** Erste Zeile T. Pro Testfall: eine Zeile mit N, dann eine Zeile mit
N Zahlen `p_i`.

**Ausgabe.** Pro Testfall eine Zeile `Case #i: l`. Nullbasiert.

```
Eingabe:              Ausgabe:

2                     Case #0: 2
3                     Case #1: 1
1 0 0
3
0 1 0
```

Im ersten Testfall ist gleich am Anfang ein Loch, danach kommen zwei heile
Abschnitte — also 2. Im zweiten liegt das Loch in der Mitte und zerteilt die
Strasse in zwei Stücke der Länge 1.

**Behalte deinen Aufgabenordner.** In M3 und M4 baust du auf dem Programm auf,
das du hier schreibst.

### Einstieg — Teilaufgabe 1 (20 Punkte)

Die Strasse ist immer genau drei Abschnitte lang. Dasselbe Beispiel wie oben.

Nimm dir **15 Minuten**. Du kommst hier mit Nachdenken und ein paar `if` durch —
und das ist völlig in Ordnung. Schau danach genau hin, warum dieser Weg bei
Teilaufgabe 2 nicht mehr trägt.

??? tip "Hinweis 1 — erst selbst versuchen"
    Bei N = 3 gibt es nicht viele Möglichkeiten.

    Wie viele zusammenhängende Abschnitte hat eine Strasse der Länge 3? Schreib
    sie alle auf ein Blatt, bevor du weiterliest. Nicht nur die lochfreien —
    alle.

??? tip "Hinweis 2 — erst selbst versuchen"
    Halt das linke Ende fest.

    Du stehst am Abschnitt Nummer 0 und weisst noch nichts über den Rest. Wie
    weit kommst du von dort nach rechts, bevor das erste Loch auftaucht? Und
    dann dasselbe ab Abschnitt 1, ab Abschnitt 2.

??? tip "Hinweis 3 — erst selbst versuchen"
    Zwei Randfälle, an denen viele scheitern:

    Die Strasse kann **nur aus Löchern** bestehen. Was ist dann die Antwort, und
    was heisst das für den Startwert deiner Ergebnisvariablen?

    Und sobald du beim Verlängern nach rechts auf ein Loch triffst, ist dieser
    Startpunkt erledigt — weiterlaufen bringt nichts mehr.

!!! success "Erst wenn deine Lösung am Beispiel läuft"
    [Ausdauer Teilaufgabe 1 einreichen](https://soi.ch/contests/2025/preround/endurance/#teilaufgabe-1-eine-kurze-strecke-20-punkte)

    Ab dem Klick auf „Eingabedaten herunterladen" hast du fünf Minuten.
    Hochgeladen wird nur die Ausgabedatei, nie dein Programm.

### Kern — Teilaufgabe 2 (20 Punkte)

Dieselbe Frage, jetzt mit 1 ≤ N ≤ 100. Eingabe, Ausgabe und Beispiel sind
unverändert.

Nimm dir **20 Minuten**. Das ist die Verschärfung: dasselbe Problem, aber deine
Lösung muss wachsen.

??? tip "Hinweis 1 — erst selbst versuchen"
    Funktioniert deine Lösung von Teilaufgabe 1 auch bei N = 100?

    Wenn du dort ein paar `if` geschrieben hast: Wie viele bräuchtest du jetzt?
    Genau das ist der Grund, warum Fallunterscheidung hier nicht mehr trägt.

??? tip "Hinweis 2 — erst selbst versuchen"
    Die Anzahl Möglichkeiten hängt jetzt von N ab. Also müssen es auch deine
    Schleifen tun.

    Jeder mögliche Laufabschnitt ist durch zwei Angaben eindeutig festgelegt:
    sein linkes und sein rechtes Ende. Wenn du beide systematisch durchgehst,
    kannst du keinen übersehen und keinen doppelt zählen.

??? tip "Hinweis 3 — erst selbst versuchen"
    Leg vor den Schleifen eine Variable für das bisher beste Ergebnis an und
    setz sie auf 0.

    Formuliere die Invariante, bevor du tippst: Was genau steht in dieser
    Variablen, während die Schleife läuft? Wenn du den Satz hinschreiben kannst,
    schreibt sich der Code fast von selbst.

!!! success "Erst wenn deine Lösung am Beispiel läuft"
    [Ausdauer Teilaufgabe 2 einreichen](https://soi.ch/contests/2025/preround/endurance/#teilaufgabe-2-ein-langerer-weg-20-punkte)

    Deine Lösung für Teilaufgabe 2 löst Teilaufgabe 1 gleich mit — dieselbe
    Ausgabedatei, zwei Einsendungen, 40 Punkte.

---

## Vertiefung — Treppenlauf, Teilaufgabe 2

Aus der Runde 2020/2021, auf soi.ch **Treppenlauf**. Teilaufgabe 1 kennst du
schon aus [M0](../m00-werkzeugkasten/index.md).

Binnas Laufstrecke startet auf dem Dach eines Wolkenkratzers **links**, führt
hinunter, ein Stück die Strasse entlang und auf einem Wolkenkratzer **rechts**
wieder hinauf. Gesucht ist die längstmögliche Gesamtdistanz:

```
Höhe links  +  Distanz entlang der Strasse  +  Höhe rechts
```

Auf jeder Seite stehen N Wolkenkratzer, jeder genau gegenüber einem der anderen
Seite. Die Distanz entlang der Strasse ist der Abstand der beiden Positionen.

| Teilaufgabe | Schranke | Punkte | |
|---|---|---|---|
| 1 | N = 1 | 25 | erledigt in M0 |
| 2 | N = 2 | 25 | **dieses Modul** |
| 3 | 1 ≤ N ≤ 1000 | 25 | M3 |
| 4 | 1 ≤ N ≤ 100 000 | 25 | M4 |

T = 100, Höhen zwischen 1 und 10⁶.

**Eingabe.** Erste Zeile T. Pro Testfall: eine Zeile mit N, eine Zeile mit den N
Höhen links, eine Zeile mit den N Höhen rechts.

```
Eingabe:              Ausgabe:

3                     Case #0: 3
2                     Case #1: 1338
1 1                   Case #2: 2672
1 1
2
1336 1336
1 1
2
1 1336
1 1336
```

Testfall 1 ist der lehrreiche: Zwei Türme der Höhe 1336 stehen links, rechts nur
zwei der Höhe 1. Man nimmt einen der hohen links, einen rechts, und weil sie
nicht gegenüberliegen, kommt noch 1 für die Strasse dazu — 1336 + 1 + 1 = 1338.

!!! note "Ein Wolkenkratzer links, einer rechts"
    Beide auf derselben Strassenseite zu wählen ist nicht erlaubt. Testfall 2
    zeigt den Grenzfall: Beide 1336er liegen einander gegenüber, die Strecke
    entlang der Strasse ist dann 0.

Dieselbe Denkfigur wie bei der Ausdauer, andere Oberfläche: Statt Abschnitten
zählst du Kombinationen auf. Nimm dir **20 Minuten**.

??? tip "Hinweis 1 — erst selbst versuchen"
    Stell dir die drei Fragen aus dem Konzept, vor allem die erste: Was ist hier
    **eine Möglichkeit**?

    Nicht „ein Wolkenkratzer", sondern etwas, das die ganze Laufstrecke
    festlegt.

??? tip "Hinweis 2 — erst selbst versuchen"
    Naheliegend wäre die Abkürzung: den höchsten Wolkenkratzer links nehmen, den
    höchsten rechts, fertig.

    Bevor du das programmierst, such ein Gegenbeispiel auf Papier. Mit zwei
    Wolkenkratzern pro Seite wirst du keines finden — nimm drei. Denk daran,
    dass zur Höhe noch der Abstand dazukommt.

??? tip "Hinweis 3 — erst selbst versuchen"
    Zwei Schleifen: eine über die Wolkenkratzer links, eine über die rechts. Für
    jedes Paar rechnest du die Gesamtdistanz aus und behältst die grösste.

    Schreib das gleich für **beliebiges N**, nicht für genau zwei. Vier Fälle von
    Hand hinzuschreiben ginge auch — aber dann fängst du in M3 wieder von vorne
    an.

!!! success "Erst wenn deine Lösung am Beispiel läuft"
    [Treppenlauf Teilaufgabe 2 einreichen](https://soi.ch/contests/2021/round1/stairracing/#teilaufgabe-2-eine-kurze-strasse-25-punkte)

    Prüf danach mit einem selbst gebauten Beispiel, bei dem N = 5 ist. Die
    Antwort musst du dafür von Hand ausrechnen — das ist Teil der Übung.
    Hochladen brauchst du nichts mehr, die Punkte hast du schon.

---

## Trockenübung 1 — wo hört das auf?

Papier und Bleistift. Kein Programm, kein Upload.

Du hast jetzt zwei allgemeine Lösungen: eine für die Ausdauer mit zwei Schleifen
über die Strasse, eine für den Treppenlauf mit zwei Schleifen über die
Strassenseiten. Beide Aufgaben haben mehr Teilaufgaben, als du gelöst hast.

Schätze für jede Zeile, wie viele Schritte deine Lösung ungefähr braucht, rechne
das in eine Dauer um und entscheide, ob du damit einreichen kannst.

| Aufgabe | Teilaufgabe | Schranke |
|---|---|---|
| Ausdauer | 3 | N ≤ 100 000 |
| Treppenlauf | 3 | N ≤ 1 000 |
| Treppenlauf | 4 | N ≤ 100 000 |

Drei Dinge, die du dafür brauchst:

- **T = 100 Testfälle** — der Faktor wird am häufigsten vergessen
- Python schafft rund **10⁷ Schritte pro Sekunde**
- Dein Zeitbudget sind die **fünf Minuten** zwischen Download und Upload. Der
  Grader misst deine Laufzeit nicht, du lädst ja nur die Ausgabedatei hoch.

Die letzte Angabe überrascht viele. Überleg, was sie für deine Urteile bedeutet.

Schreib zu jeder Zeile eine Zahl und ein Urteil hin. Erst danach vergleichst du
mit der Lösung.

Diese Schätzung ist keine Trockenübung im abwertenden Sinn. Sie ist die
Entscheidung, die du in der Prüfungssituation als Erstes treffen musst — bevor du
eine halbe Stunde in eine Lösung steckst, die nicht durchlaufen kann.

## Trockenübung 2 — wo steckt hier eine Suche?

Papier. Kein Programm.

Stofl hat **N Käsestücke** mit bekannten Gewichten. Er möchte wissen, ob sich
**genau zwei** davon zusammen auf exakt **W Gramm** bringen lassen.

Die Frage sieht aus wie eine Ja-oder-Nein-Frage und nicht nach einer Suche. Sie
ist aber eine.

1. Was ist hier **eine Möglichkeit**?
2. Wie viele Möglichkeiten gibt es bei N = 100? Gib eine Formel an, nicht nur
   eine Zahl.
3. Formuliere die Invariante deiner Suche. Achtung: Sie sieht anders aus als bei
   der Ausdauer, weil du nicht das Beste suchst, sondern nur wissen willst, ob es
   überhaupt etwas gibt.
4. Was ändert sich an deiner Antwort auf Frage 2, wenn Stofl dasselbe Käsestück
   zweimal nehmen dürfte?

## Trockenübung 3 — eine Abkürzung widerlegen

Papier. Kein Programm.

Für den Treppenlauf behauptet jemand:

> „Man nimmt einfach den höchsten Wolkenkratzer links und den höchsten rechts.
> Höher geht nicht."

1. Schau dir Testfall 0 des offiziellen Beispiels an: `1 1` links, `1 1` rechts,
   Antwort 3. Was liefert die Abkürzung dort, und warum?
2. Bau ein Gegenbeispiel mit **drei** Wolkenkratzern pro Seite, bei dem alle
   sechs Höhen **verschieden** sind. Gib beide Höhenlisten an und rechne beide
   Strecken aus — die nach der Behauptung und die tatsächlich beste.
3. Jemand repariert die Abkürzung: *„Bei Gleichstand nehme ich unter allen
   höchsten Türmen die Kombination mit dem grössten Abstand."* Hält diese
   Fassung bei N = 2? Hält sie bei N = 3?
4. Angenommen, du testest deine Abkürzung nur mit Höhen, die alle verschieden
   sind. Ab welchem N fällt sie dann auf? Was folgt daraus für die Art, wie du
   Testbeispiele baust?

Die vierte Frage ist die eigentliche.

---

Wenn du eine Aufgabe wirklich versucht hast, findest du die
[Musterlösungen zu M2](loesung.md).
