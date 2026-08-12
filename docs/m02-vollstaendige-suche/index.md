# M2 — Vollständige Suche

## Das Problem

Binna organisiert einen Marathon auf einer Strasse. Die Strasse ist in **N**
Abschnitte unterteilt, und in manchen davon ist ein Loch. Gelaufen wird nur auf
einem zusammenhängenden Stück ohne Loch.

Wie lang ist das längste Stück, auf dem man laufen kann?

Die Aufgabe heisst **Endurance** und steht in der Vorrunde. Sie hat fünf
Teilaufgaben zu je 20 Punkten. Hier die ganze Leiter, damit du weisst, wo du
stehst:

| Teilaufgabe | Schranke | Punkte | |
|---|---|---|---|
| 1 | N = 3 | 20 | **dieses Modul** |
| 2 | 1 ≤ N ≤ 100 | 20 | **dieses Modul** |
| 3 | 1 ≤ N ≤ 100 000 | 20 | M3 |
| 4 | mit einer zusätzlichen Regel | 20 | M4 |
| 5 | mit einer zusätzlichen Regel | 20 | M4 |

In allen Teilaufgaben ist T = 100. **In diesem Modul lösen wir die ersten
beiden.**

Eingabe: zuerst die Anzahl Testfälle T. Pro Testfall die Länge N, dann N Zahlen
`p_i` — eine `1` bedeutet Loch, eine `0` bedeutet heile Strasse.

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

!!! note "Du musst nichts nachschlagen"
    Alles zum Lösen steht auf dieser Seite: Geschichte, Format, Schranken und
    Beispiel. Auf soi.ch gehst du erst, wenn deine Lösung am Beispiel läuft —
    dort holst du die Eingabedaten, und dann läuft die Uhr.

---

## Probier es selbst

Nimm dir **25 Minuten**. Erst Teilaufgabe 1, dann Teilaufgabe 2.

Bei Teilaufgabe 1 ist die Strasse immer genau drei Abschnitte lang. Du kommst
dort mit Nachdenken und ein paar `if` durch — und das ist völlig in Ordnung. Aber
schau danach genau hin, warum dieser Weg bei Teilaufgabe 2 nicht mehr trägt.

??? tip "Kommst du nicht weiter?"
    Dann arbeite dich durch die Hinweise unten, einen nach dem anderen. Nach
    jedem Hinweis probierst du wieder selbst weiter.

    Wenn es am Ablauf hakt und nicht am Denken: Play-Knopf, `EINGABE`, Upload —
    das steht in [M0 — Werkzeugkasten](../m00-werkzeugkasten/index.md).

!!! success "Erst wenn deine Lösung am Beispiel läuft"
    Dann geht es zum Einreichen. Die Links springen direkt zur richtigen
    Teilaufgabe:

    - [Endurance Teilaufgabe 1](https://soi.ch/contests/2025/preround/endurance/#teilaufgabe-1-eine-kurze-strecke-20-punkte)
    - [Teilaufgabe 2](https://soi.ch/contests/2025/preround/endurance/#teilaufgabe-2-ein-langerer-weg-20-punkte)

    Ab dem Klick auf „Eingabedaten herunterladen" hast du fünf Minuten.

---

## Hinweise

??? tip "Hinweis 1 — erst selbst versuchen"
    Bei N = 3 gibt es nicht viele Möglichkeiten.

    Wie viele zusammenhängende Abschnitte hat eine Strasse der Länge 3? Schreib
    sie alle auf ein Blatt, bevor du weiterliest. Nicht die lochfreien — alle.

??? tip "Hinweis 2 — erst selbst versuchen"
    > **Analogie:** Du suchst im Kalender die längste zusammenhängende Zeit ohne
    > Termin. Du gehst nicht auf gut Glück vor, sondern der Reihe nach: Ab dem
    > Ersten — wie weit komme ich? Ab dem Zweiten — wie weit? Ab dem Dritten?
    > Am Ende nimmst du die längste der gefundenen Strecken.

    Der entscheidende Teil ist nicht das Zählen. Es ist, dass du **jeden Starttag
    einmal ausprobierst** und keinen auslässt.

    Übertrag das auf die Strasse: Was entspricht dem Starttag?

??? tip "Hinweis 3 — erst selbst versuchen"
    Halt das linke Ende fest.

    Du stehst am Abschnitt Nummer 4 und weisst noch nichts über den Rest. Wie
    weit kommst du von dort nach rechts, bevor das erste Loch auftaucht?

    Das ist eine kleine Aufgabe für sich — und du kannst sie für jedes linke Ende
    stellen.

??? tip "Hinweis 4 — erst selbst versuchen"
    Jeder mögliche Laufabschnitt ist durch zwei Angaben eindeutig festgelegt: sein
    linkes und sein rechtes Ende.

    Wenn du beide systematisch durchgehst, kannst du keinen Abschnitt übersehen
    und keinen doppelt zählen. Genau das ist der Unterschied zwischen Ausprobieren
    und vollständiger Suche.

??? tip "Hinweis 5 — nur bei Implementierungsproblemen"
    Leg vor den Schleifen eine Variable an, in der das bisher beste Ergebnis
    steht, und setz sie auf 0. Nach jedem geprüften Abschnitt vergleichst du und
    ersetzt sie gegebenenfalls.

    Zwei Randfälle, an denen viele scheitern:

    - Die Strasse kann **nur aus Löchern** bestehen. Dann ist die Antwort 0 — und
      deshalb ist 0 der richtige Startwert.
    - Sobald du beim Verlängern nach rechts auf ein Loch triffst, ist dieser
      Startpunkt erledigt. Weiterlaufen bringt nichts mehr.

---

## Das Konzept

### Was vollständige Suche ist

Vollständige Suche heisst: **jede Möglichkeit genau einmal anschauen und die
beste behalten.** Nicht raten, nicht abkürzen, nicht hoffen.

Um sie auf ein Problem anzuwenden, beantwortest du drei Fragen:

| Frage | Bei Endurance |
|---|---|
| Was ist **eine Möglichkeit**? | ein zusammenhängender Abschnitt der Strasse |
| Wie zähle ich **alle** auf? | über jedes linke Ende, dazu jedes rechte Ende rechts davon |
| Woran erkenne ich die **beste**? | sie ist lochfrei und am längsten |

Die mittlere Frage ist die, an der es hängt. „Alle aufzählen" muss heissen:
keine vergessen **und** keine doppelt. Ein Abschnitt ist durch linkes und rechtes
Ende eindeutig festgelegt — zählst du beide Enden systematisch durch, ist beides
automatisch erfüllt.

Eine Strasse der Länge N hat

```
N · (N + 1) / 2
```

zusammenhängende Abschnitte. Bei N = 3 sind das 6, bei N = 100 sind es 5050.

### Die Invariante

Während die Suche läuft, gilt durchgehend derselbe Satz:

> **`bestes` enthält die Länge des längsten lochfreien Abschnitts unter allen,
> die bisher geprüft wurden.**

Am Anfang wurde noch keiner geprüft, deshalb steht dort 0. Am Ende wurden alle
geprüft — und damit steht dort die Antwort.

Diesen Satz nennt man eine **Invariante**: eine Aussage, die vor und nach jedem
Schleifendurchlauf stimmt. Sie ist der Grund, warum du dem Ergebnis trauen
kannst, ohne alle 5050 Fälle von Hand nachzurechnen.

### Laufzeit

Es gibt zwei naheliegende Wege, und der Unterschied entscheidet über Punkte.

**Weg A.** Für jedes Paar aus linkem und rechtem Ende noch einmal durch den
ganzen Abschnitt laufen und nach Löchern suchen. Das sind drei ineinander
liegende Schleifen, also **O(N³)**.

**Weg B.** Das linke Ende festhalten und nach rechts wandern, bis ein Loch kommt.
Dabei zählst du die Länge einfach mit. Zwei Schleifen, also **O(N²)**.

Rechne nach, was das bei Teilaufgabe 2 bedeutet — N = 100 und T = 100 Testfälle:

| Weg | Schritte pro Testfall | insgesamt | Grössenordnung |
|---|---|---|---|
| A: O(N³) | 10⁶ | 10⁸ | Sekunden |
| B: O(N²) | 10⁴ | 10⁶ | Sekundenbruchteil |

Als grobe Faustregel rechnen wir mit **10⁷ Schritten pro Sekunde in Python**.
Diese Zahl solltest du dir merken; ab M3 ist sie das wichtigste Werkzeug
überhaupt.

!!! warning "Eine bewusst grobe Rechnung"
    Wir tun so, als wäre jeder Schleifendurchlauf gleich teuer. Das stimmt nicht:
    Ein Durchlauf mit Multiplikation und Listenzugriff dauert länger als einer mit
    einem Vergleich, und dein Gerät ist schneller oder langsamer als das der
    Nachbarin.

    Solche Unterschiede machen leicht einen Faktor 3 aus. Das ist in Ordnung,
    denn worauf es ankommt, sind Faktoren von **tausend und mehr**. Schätz die
    Grössenordnung, nicht die Sekunden.

!!! note "Beide Wege geben hier volle Punkte"
    Ein paar Sekunden klingen nach viel, sind aber kein Problem: Du lädst eine
    Ausgabedatei hoch, kein Programm. Niemand misst, wie lange dein Programm
    gelaufen ist. Die einzige Uhr sind die fünf Minuten zwischen Download und
    Upload.

    Weg A ist also nicht falsch — er ist nur verschwenderisch. Der Unterschied
    zwischen 10⁶ und 10⁸ Schritten kostet dich hier nichts. Merk dir trotzdem,
    wo er herkommt: In Teilaufgabe 3 wird aus demselben Unterschied der zwischen
    Sekunden und Tagen.

### Brute Force ist keine Notlösung

Teilaufgabe 1 und 2 zusammen sind **40 von 100 Punkten**. Die bekommst du mit
einer Lösung, die stur alles durchprobiert.

In der Olympiade zählt jede Teilaufgabe einzeln. Wer die einfache Lösung
einreicht und danach weiterdenkt, steht immer besser da als wer auf die perfekte
Lösung wartet. Das ist keine Notlösung und kein Trostpreis — es ist die richtige
Reihenfolge.

### Die Analogie und ihre Grenze

> **Analogie:** Im Kalender die längste terminfreie Strecke suchen, indem du bei
> jedem Tag der Reihe nach anfängst zu zählen.

**Bruchstelle:** Die Analogie tut so, als müsstest du bei jedem Tag neu zu zählen
beginnen. Bei einem Jahreskalender geht das noch; bei 100 000 Abschnitten nicht
mehr. Sie zeigt dir, *wie* man vollständig sucht, aber nicht, *wann* man es
besser lässt. Diese Frage ist genau der Inhalt von M3.

---

## Prüfe dich selbst

??? success "Vergleiche deine Antwort — Frage 1"
    **Wie viele zusammenhängende Abschnitte hat eine Strasse der Länge 4?**

    10 Stück.

    Nach der Formel: 4 · 5 / 2 = 10. Zum Nachzählen: vier Abschnitte der Länge 1,
    drei der Länge 2, zwei der Länge 3, einer der Länge 4.

??? success "Vergleiche deine Antwort — Frage 2"
    **Was ist die Antwort für die Strasse `1 1 1`?**

    0.

    Es gibt keinen einzigen lochfreien Abschnitt. Wer hier 1 oder eine
    Fehlermeldung bekommt, hat die Variable für das beste Ergebnis falsch
    gestartet oder den Fall gar nicht bedacht.

    Solche Randfälle stehen selten im Beispiel der Aufgabenstellung. Denk sie dir
    selbst aus — das ist dieselbe Probe am Extremfall wie in M1.

??? success "Vergleiche deine Antwort — Frage 3"
    **Deine Lösung prüft jeden Abschnitt, indem sie ihn noch einmal ganz
    durchläuft. Bei N ≤ 100 und T = 100: Reicht das in Python?**

    Ja — es reicht.

    Drei Schleifen ergeben rund 100³ = 10⁶ Schritte pro Testfall, bei 100
    Testfällen also etwa 10⁸. Bei 10⁷ Schritten pro Sekunde ist das die
    Grössenordnung von Sekunden. Unangenehm, aber innerhalb der fünf Minuten
    problemlos.

    Mit zwei Schleifen sind es 10⁶ insgesamt und damit ein Sekundenbruchteil.

    Die richtige Antwort ist also nicht „zu langsam", sondern: **hundertmal mehr
    Arbeit für dasselbe Ergebnis.** Ob das schadet, hängt allein von der Schranke
    ab — und bei Teilaufgabe 3 schadet es.

??? success "Vergleiche deine Antwort — Frage 4"
    **Du hast eine Lösung für Teilaufgabe 1 und 2. Teilaufgabe 3 verlangt
    N ≤ 100 000, und dir fällt nichts Besseres ein. Was tust du?**

    Hochladen.

    40 Punkte sind 40 Punkte, und sie sind sicher. Teilaufgabe 3 kannst du danach
    immer noch angehen — die Vorrunde läuft das ganze Jahr, und jeder Download
    liefert frische Testfälle.

    Wer wartet, bis die perfekte Lösung steht, sammelt am Ende weniger Punkte als
    wer einreicht und weiterdenkt.

---

## Übungen

Weiter geht es mit [den Übungen zu M2](uebungen.md): Treppenlauf aus dem Archiv,
eine versteckte Suche und eine Schätzaufgabe, die dich direkt nach M3 führt.

---

## Weiter zu M3

Wenn du Endurance Teilaufgabe 1 und 2 gelöst hast, kannst du ein Problem in
Möglichkeiten zerlegen, sie systematisch aufzählen und die beste behalten.

In [M3 — Laufzeitdenken](../m03-laufzeitdenken/index.md) kommt die Frage dazu,
die hier schon angeklopft hat: **Wie viele Möglichkeiten sind zu viele?** Der
Sprung von N ≤ 100 auf N ≤ 100 000 in Teilaufgabe 3 ist keine Fleissarbeit — er
zwingt zu einer anderen Idee.
