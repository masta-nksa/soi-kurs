# M2 — Vollständige Suche

!!! note "Du kannst hier einsteigen, wenn ..."
    ... du zu einem unbekannten Aufgabentext ohne Hilfe aufschreiben kannst, was
    gegeben ist, was gesucht ist und welche Beziehung beides verbindet — und
    dein Modell an einem Extremfall prüfst, bevor du programmierst. Das ist der
    Inhalt von [M1](../m01-problemanalyse/index.md).

    Programmieren musst du können: Schleifen, `if`, Listen. Mehr nicht.

**In diesem Modul:** [Vollständige Suche](#vollstandige-suche)
· [Die Invariante](#die-invariante)
· [Teilpunkte mitnehmen](#teilpunkte-mitnehmen)

In M1 liess sich die Antwort ausrechnen. Ab hier nicht mehr. Für die Aufgaben
dieses Moduls gibt es keine Formel — nur die Möglichkeit, alle Fälle
durchzugehen und den besten zu behalten.

Das klingt nach Kapitulation und ist das Gegenteil: Vollständige Suche ist ein
Verfahren mit Regeln, und wer sie beherrscht, holt in der SOI zuverlässig
Punkte.

---

## Vollständige Suche

### Worum es geht

Binna organisiert einen Marathon auf einer Strasse. Die Strasse ist in **N**
Abschnitte unterteilt, und in manchen davon ist ein Loch. Gelaufen wird nur auf
einem zusammenhängenden Stück ohne Loch.

Wie lang ist das längste Stück, auf dem man laufen kann?

```
Strasse:   0 1 0 0 1 1 0
```

Man sieht die Antwort hier mit blossem Auge — zwei. Bei hundert Abschnitten
nicht mehr, und ein Programm sieht ohnehin nichts.

### Die Idee

> **Kernsatz:** Schau jede Möglichkeit genau einmal an und behalte die beste.
> Nicht raten, nicht abkürzen, nicht hoffen.

Um das auf ein Problem anzuwenden, beantwortest du drei Fragen:

| Frage | Bei der Ausdauer |
|---|---|
| Was ist **eine Möglichkeit**? | ein zusammenhängender Abschnitt der Strasse |
| Wie zähle ich **alle** auf? | über jedes linke Ende, dazu jedes rechte Ende rechts davon |
| Woran erkenne ich die **beste**? | sie ist lochfrei und am längsten |

Die mittlere Frage ist die, an der es hängt. „Alle aufzählen" muss heissen:
keine vergessen **und** keine doppelt. Ein Abschnitt ist durch linkes und
rechtes Ende eindeutig festgelegt — zählst du beide Enden systematisch durch,
ist beides automatisch erfüllt.

> **Analogie:** Du suchst im Kalender die längste zusammenhängende Zeit ohne
> Termin. Du gehst nicht auf gut Glück vor, sondern der Reihe nach: Ab dem
> Ersten — wie weit komme ich? Ab dem Zweiten? Ab dem Dritten? Am Ende nimmst du
> die längste der gefundenen Strecken.
>
> **Bruchstelle:** Die Analogie tut so, als müsstest du bei jedem Tag neu zu
> zählen beginnen. Bei einem Jahreskalender geht das noch, bei 100 000
> Abschnitten nicht mehr. Sie zeigt dir, *wie* man vollständig sucht, aber nicht,
> *wann* man es besser lässt. Diese Frage ist der Inhalt von
> [M3](../m03-laufzeitdenken/index.md).

### An einem Beispiel

Die Strasse `0 1 0` hat sechs zusammenhängende Abschnitte. Alle sechs:

```
Position:      0 1 2
Strasse:       0 1 0

von 0 bis 0:   0          lochfrei, Länge 1
von 0 bis 1:   0 1        Loch
von 0 bis 2:   0 1 0      Loch
von 1 bis 1:     1        Loch
von 1 bis 2:     1 0      Loch
von 2 bis 2:       0      lochfrei, Länge 1

bestes: 1
```

Allgemein hat eine Strasse der Länge N genau

```
N · (N + 1) / 2
```

zusammenhängende Abschnitte. Bei N = 3 sind das 6, bei N = 100 schon 5050.

### Im Code

Zwei Schleifen zählen die Enden auf. Das linke Ende steht fest, das rechte
wandert nach rechts, bis ein Loch kommt:

```python
bestes = 0
for links in range(n):
    laenge = 0
    for rechts in range(links, n):
        if p[rechts] == 1:
            break
        laenge = laenge + 1
        if laenge > bestes:
            bestes = laenge
```

`bestes` startet bei 0, nicht bei 1. Eine Strasse kann ausschliesslich aus
Löchern bestehen, und dann ist 0 die richtige Antwort.

### Laufzeit

Es gibt zwei naheliegende Wege, und der Unterschied wird ab M3 wichtig.

**Weg A.** Für jedes Paar aus linkem und rechtem Ende noch einmal durch den
ganzen Abschnitt laufen und nach Löchern suchen. Drei ineinander liegende
Schleifen, also **O(N³)**.

**Weg B.** Das linke Ende festhalten und nach rechts wandern, dabei die Länge
mitzählen — der Code oben. Zwei Schleifen, also **O(N²)**.

Bei Teilaufgabe 2 mit N = 100 und T = 100 Testfällen:

| Weg | pro Testfall | insgesamt | Grössenordnung |
|---|---|---|---|
| A: O(N³) | 10⁶ | 10⁸ | Sekunden |
| B: O(N²) | 10⁴ | 10⁶ | Sekundenbruchteil |

Als grobe Faustregel rechnen wir mit **10⁷ Schritten pro Sekunde in Python**.
Diese Zahl solltest du dir merken; ab M3 ist sie das wichtigste Werkzeug
überhaupt.

!!! note "Beide Wege geben hier volle Punkte"
    Ein paar Sekunden klingen nach viel, sind aber kein Problem: Du lädst eine
    Ausgabedatei hoch, kein Programm. Niemand misst, wie lange dein Programm
    gelaufen ist. Die einzige Uhr sind die fünf Minuten zwischen Download und
    Upload.

    Weg A ist also nicht falsch — er ist nur verschwenderisch. Merk dir trotzdem,
    wo der Unterschied herkommt: In Teilaufgabe 3 wird aus denselben zwei
    Grössenordnungen der Unterschied zwischen Sekunden und Tagen.

!!! warning "Eine bewusst grobe Rechnung"
    Wir tun so, als wäre jeder Schleifendurchlauf gleich teuer. Das stimmt nicht:
    Ein Durchlauf mit Multiplikation und Listenzugriff dauert länger als einer
    mit einem Vergleich, und dein Gerät ist schneller oder langsamer als das der
    Nachbarin.

    Solche Unterschiede machen leicht einen Faktor 3 aus. Das ist in Ordnung,
    denn worauf es ankommt, sind Faktoren von **tausend und mehr**. Schätz die
    Grössenordnung, nicht die Sekunden.

### Woran du es erkennst

- Die Aufgabe fragt nach dem **grössten, kleinsten, besten** von etwas — und es
  gibt keine Formel dafür.
- Die Aufgabe fragt, **ob es überhaupt** etwas gibt, das eine Bedingung erfüllt.
- Die Schranken sind **klein**: N = 3, N ≤ 100, „genau zwei Objekte". Das ist
  kein Zufall, sondern eine Einladung. Kleine Schranken in einer frühen
  Teilaufgabe heissen fast immer: Probier alles durch.
- Du kannst eine einzelne Möglichkeit leicht **beschreiben und bewerten**, weisst
  aber nicht, welche die beste ist.

### Typische Fallen

- **Der Startwert.** `bestes = 0` gegen `bestes = 1` entscheidet über den Fall,
  in dem es gar keine gültige Möglichkeit gibt.
- **Doppelt oder gar nicht gezählt.** Wer die Enden nicht systematisch durchgeht,
  übersieht Fälle. Zähl bei einem winzigen Beispiel von Hand nach, ob dein
  Programm wirklich alle sechs Abschnitte anschaut.
- **Eine Abkürzung raten.** „Ich nehme einfach den höchsten Wert" fühlt sich
  richtig an und ist es fast nie. Wer abkürzen will, braucht ein Argument, kein
  Gefühl — und wer eines sucht, findet meist ein Gegenbeispiel.

---

## Die Invariante

### Worum es geht

Deine Schleife läuft 5050 Mal. Woher weisst du, dass am Ende die richtige Zahl
dasteht? Nachrechnen kannst du das nicht.

### Die Idee

> **Kernsatz:** Formuliere einen Satz, der vor und nach jedem
> Schleifendurchlauf stimmt. Wenn er am Anfang stimmt und jeder Durchlauf ihn
> erhält, dann stimmt er auch am Ende — und am Ende ist er die Antwort.

Bei der Ausdauer lautet er:

> **`bestes` enthält die Länge des längsten lochfreien Abschnitts unter allen,
> die bisher geprüft wurden.**

Am Anfang wurde noch keiner geprüft, deshalb steht dort 0 — der Satz stimmt. Jeder
Durchlauf prüft einen weiteren Abschnitt und aktualisiert `bestes`, falls nötig —
der Satz stimmt weiterhin. Am Ende wurden alle geprüft, und damit steht in
`bestes` die Antwort.

### An einem Beispiel

`0 1 0`, Schritt für Schritt:

```
                                         bestes   Satz stimmt?
Start, nichts geprüft                       0     ja, leere Menge
nach "von 0 bis 0" (lochfrei, 1)            1     ja
nach "von 0 bis 1" (Loch)                   1     ja
nach "von 0 bis 2" (Loch)                   1     ja
nach "von 1 bis 1" (Loch)                   1     ja
nach "von 1 bis 2" (Loch)                   1     ja
nach "von 2 bis 2" (lochfrei, 1)            1     ja, alle geprüft
```

### Wann du es brauchst

Bei jeder Schleife, deren Ergebnis du nicht von Hand nachrechnen kannst. Das
Aufschreiben dauert einen Satz und ersetzt stundenlanges Herumprobieren.

Woran du merkst, dass du keine hast:

- Du änderst eine Zeile, schaust, ob das Beispiel jetzt stimmt, und änderst
  wieder — statt zu wissen, warum.
- Du kannst nicht sagen, was in deiner Ergebnisvariablen steht, während die
  Schleife läuft.
- Beim Startwert bist du unsicher. Der Startwert ist genau der Wert, der den
  Satz für „noch nichts geprüft" wahr macht.

### Typische Fallen

- **Den Satz zu schwach formulieren.** „`bestes` ist irgendein gültiger Wert"
  hilft nicht. Er muss präzise genug sein, dass er am Ende die Antwort ergibt.
- **Suchen statt Optimieren.** Wenn du nur wissen willst, *ob* es etwas gibt,
  sieht der Satz anders aus: „`gefunden` ist wahr, sobald unter den bisher
  geprüften Möglichkeiten eine passende war."

---

## Teilpunkte mitnehmen

### Worum es geht

Die Ausdauer hat fünf Teilaufgaben zu je 20 Punkten. Nach diesem Modul kannst du
zwei davon — 40 Punkte. Die anderen drei brauchen Werkzeuge aus M3 und M4.

Die Frage ist: Reichst du jetzt ein oder wartest du?

### Die Idee

> **Kernsatz:** Jede Teilaufgabe zählt einzeln. Eine Lösung, die nur die kleinen
> Schranken schafft, gibt volle Punkte für genau diese Teilaufgaben.

Brute Force ist deshalb **keine Notlösung und kein Trostpreis**. Die Aufgaben
sind absichtlich so gebaut: Die ersten Teilaufgaben haben winzige Schranken,
damit jede Lösung durchläuft. Das ist eine Einladung, keine Schwelle.

### An einem Beispiel

Zwei Vorgehensweisen an derselben Aufgabe:

```
A: erst denken, dann einreichen
   Woche 1: an Teilaufgabe 3 gescheitert     0 Punkte
   Woche 2: immer noch dran                  0 Punkte

B: einreichen, dann weiterdenken
   Woche 1: Teilaufgabe 1 und 2 gelöst      40 Punkte
   Woche 2: Teilaufgabe 3 dazu              60 Punkte
```

Am Ende der zweiten Woche hat B mindestens 40 Punkte mehr — auch dann, wenn
beide gleich gut denken.

### Wann du es brauchst

Immer, sobald irgendeine Teilaufgabe läuft. Die Vorrunde ist das ganze Jahr
offen, und jeder Download liefert frische Testfälle. Es gibt keinen Grund zu
warten.

Woran du merkst, dass du es vergisst: Du hast ein Programm, das das Beispiel
richtig löst, und arbeitest trotzdem weiter, ohne eingereicht zu haben.

### Typische Fallen

- **Auf die perfekte Lösung warten.** Der teuerste Fehler der ganzen Olympiade,
  und er kostet nichts als Punkte.
- **Die einfache Lösung wegwerfen.** Behalte sie. In M3 und M4 baust du auf ihr
  auf, und sie ist die zuverlässigste Kontrolle für die neue: Auf kleinen
  Eingaben müssen beide dasselbe liefern.

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
    Fehlermeldung bekommt, hat die Ergebnisvariable falsch gestartet oder den
    Fall gar nicht bedacht.

    Solche Randfälle stehen selten im Beispiel der Aufgabenstellung. Denk sie dir
    selbst aus — das ist dieselbe Probe am Extremfall wie in
    [M1](../m01-problemanalyse/index.md#die-probe-am-extremfall).

??? success "Vergleiche deine Antwort — Frage 3"
    **Deine Lösung prüft jeden Abschnitt, indem sie ihn noch einmal ganz
    durchläuft. Bei N ≤ 100 und T = 100: Reicht das in Python?**

    Ja — es reicht.

    Drei Schleifen ergeben rund 100³ = 10⁶ Schritte pro Testfall, bei 100
    Testfällen also etwa 10⁸. Bei 10⁷ Schritten pro Sekunde ist das die
    Grössenordnung von Sekunden. Unangenehm, aber innerhalb der fünf Minuten
    problemlos.

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

??? success "Vergleiche deine Antwort — Frage 5"
    **Du suchst nicht das längste Stück, sondern willst nur wissen, *ob* es
    irgendwo ein lochfreies Stück der Länge 5 gibt. Wie lautet die Invariante?**

    „`gefunden` ist wahr, sobald unter den bisher geprüften Abschnitten einer
    lochfrei und mindestens 5 lang war."

    Der Startwert ist entsprechend `False` — für „noch nichts geprüft" muss der
    Satz stimmen. Und anders als beim Optimieren darfst du abbrechen, sobald du
    fündig wirst: Der Satz bleibt wahr, egal was noch käme.

---

## Übungen

Weiter geht es mit [den Übungen zu M2](uebungen.md): Treppenlauf aus dem Archiv,
eine versteckte Suche und eine Schätzaufgabe, die dich direkt nach M3 führt.

---

## Weiter zu M3

Wenn du Ausdauer Teilaufgabe 1 und 2 gelöst hast, kannst du ein Problem in
Möglichkeiten zerlegen, sie systematisch aufzählen und die beste behalten.

In [M3 — Laufzeitdenken](../m03-laufzeitdenken/index.md) kommt die Frage dazu,
die hier schon angeklopft hat: **Wie viele Möglichkeiten sind zu viele?** Der
Sprung von N ≤ 100 auf N ≤ 100 000 in Teilaufgabe 3 ist keine Fleissarbeit — er
zwingt zu einer anderen Idee.
