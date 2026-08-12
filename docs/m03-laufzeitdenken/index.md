# M3 — Laufzeitdenken

## Das Problem

Dieselbe Aufgabe wie in M2. Dieselbe Strasse, dieselben Löcher, dieselbe Frage:
Wie lang ist der längste Abschnitt ohne Loch?

**Endurance**, Teilaufgabe 3. Eingabe- und Ausgabeformat sind unverändert.
Geändert hat sich genau eine Zeile in den Limits:

| Teilaufgabe | Schranke | Punkte | |
|---|---|---|---|
| 1 | N = 3 | 20 | erledigt in M2 |
| 2 | 1 ≤ N ≤ 100 | 20 | erledigt in M2 |
| 3 | 1 ≤ N ≤ **100 000** | 20 | **dieses Modul** |
| 4 | mit einer zusätzlichen Regel | 20 | M4 |
| 5 | mit einer zusätzlichen Regel | 20 | M4 |

T = 100 wie immer.

!!! note "Du musst nichts nachschlagen"
    Alles zum Lösen steht auf dieser Seite: Geschichte, Format, Schranken und
    Beispiel. Auf soi.ch gehst du erst, wenn deine Lösung am Beispiel läuft —
    dort holst du die Eingabedaten, und dann läuft die Uhr.

Deine Lösung aus M2 ist **richtig**. Sie findet für jede Strasse die korrekte
Antwort, auch für eine mit 100 000 Abschnitten. Starte sie mit dieser Eingabe,
und sie wird trotzdem nie fertig.

Das ist die unangenehmste Sorte Fehler: Es gibt keine Fehlermeldung, keine
falsche Zahl, nichts zum Debuggen. Nur ein Programm, das läuft und läuft.

---

## Probier es selbst

Nimm dir **30 Minuten**, und zwar für zwei Aufträge in dieser Reihenfolge.

**Erstens: schätzen, bevor du programmierst.** Schreib auf ein Blatt, wie viele
Rechenschritte deine M2-Lösung für Teilaufgabe 3 ungefähr braucht, und wie lange
das dauert. Eine Zahl, kein Gefühl.

**Zweitens: eine Lösung suchen, die durchläuft.** Erst danach.

Die Reihenfolge ist der Kern dieses Moduls. Wer zuerst programmiert und dann
merkt, dass es zu lange dauert, hat die halbe Lektion verschenkt.

!!! tip "Ab jetzt: neue Vorlage"
    Verwende `vorlage-stufe2.py` aus dem Ordner `vorlagen/`. Die Werkzeuge zum
    Einlesen bekommst du weiterhin fertig, aber das Muster für einen Testfall
    trägst du selbst ein. Bei Endurance ist es dasselbe wie in M2 — ein guter
    Moment, um es einmal ohne Vorlage hinzuschreiben.

??? tip "Kommst du nicht weiter?"
    Dann arbeite dich durch die Hinweise unten, einen nach dem anderen.

    Wenn du beim Schätzen nicht weiterkommst und nicht beim Programmieren: Fang
    mit der Frage an, wie viele ineinander liegende Schleifen deine Lösung hat.

!!! success "Erst wenn deine Lösung am Beispiel läuft"
    Dann geht es zum Einreichen. Die Links springen direkt zur richtigen
    Teilaufgabe:

    - [Endurance Teilaufgabe 3](https://soi.ch/contests/2025/preround/endurance/#teilaufgabe-3-ein-sehr-langer-weg-20-punkte)

    Ab dem Klick auf „Eingabedaten herunterladen" hast du fünf Minuten.

---

## Hinweise

??? tip "Hinweis 1 — erst selbst versuchen"
    Nimm eine ganz kurze Strasse ohne ein einziges Loch, etwa fünf Abschnitte.

    Wie oft schaut deine M2-Lösung die **letzte** Position an? Zähl es auf
    Papier durch, indem du die Startpunkte der Reihe nach durchgehst.

??? tip "Hinweis 2 — erst selbst versuchen"
    > **Analogie:** Du willst wissen, wie viele Schritte du am Stück gehen
    > kannst, ohne auf eine Fuge zu treten. Du stellst dich auf die erste
    > Bodenplatte und gehst los, bis eine Fuge kommt. Dann gehst du zurück,
    > stellst dich auf die zweite Platte und gehst wieder los. Dann auf die
    > dritte.
    >
    > Bei zwanzig Platten ist das mühsam. Bei hunderttausend gehst du dieselbe
    > Strecke immer wieder ab, obwohl sich am Boden nichts ändert.

    Der Boden ändert sich nicht. Deine Information über ihn auch nicht — du
    wirfst sie nur jedes Mal weg.

??? tip "Hinweis 3 — erst selbst versuchen"
    Geh ein einziges Mal von links nach rechts.

    Was musst du dir unterwegs merken, damit du am Ende die Antwort hast? Es
    sind zwei Zahlen. Überleg, welche das sind, bevor du weiterliest.

??? tip "Hinweis 4 — erst selbst versuchen"
    Jede Position wird genau einmal angeschaut.

    Wenn ein Loch kommt, beginnt die laufende Länge wieder bei null. Alles, was
    du vorher gezählt hast, ist nicht verloren — es steckt bereits im Maximum,
    das du mitführst.

??? tip "Hinweis 5 — nur bei Implementierungsproblemen"
    Zwei Variablen vor der Schleife: eine für die **laufende** Länge, eine für
    die **beste bisher**. Beide starten bei 0.

    Pro Position: Ist dort ein Loch, setzt du die laufende Länge auf 0. Sonst
    erhöhst du sie um 1 und vergleichst sie mit der besten.

    Achte darauf, dass du auch nach dem letzten Abschnitt noch verglichen hast.
    Am einfachsten ist es, bei **jedem** Schritt zu vergleichen — dann kann der
    Fall gar nicht auftreten.

---

## Das Konzept

### Die Schranke ist eine Nachricht

In der Aufgabenstellung steht nicht zufällig N ≤ 100 000. Wer die Aufgabe
gestellt hat, hat sich bei jeder Teilaufgabe überlegt, welche Lösungen damit
noch durchlaufen und welche nicht.

**Kernsatz:** Die Schranke sagt dir, welche Komplexität erlaubt ist. Lies sie,
bevor du programmierst — nicht danach.

Die Rechnung dazu geht immer gleich:

1. **Schleifen zählen.** Ineinander liegende Schleifen über die Eingabe:
   eine ist O(N), zwei sind O(N²), drei sind O(N³).
2. **N einsetzen.** Aus O(N²) mit N = 100 000 werden 10¹⁰ Schritte.
3. **Mal T.** Bei 100 Testfällen also 10¹².
4. **Grössenordnung nachschlagen** und mit deinem Budget vergleichen.

Schritt 3 wird am häufigsten vergessen, und er ist ein Faktor 100.

| Schritte | Grössenordnung der Dauer |
|---|---|
| 10⁶ | Sekundenbruchteil |
| 10⁷ | rund eine Sekunde |
| 10⁸ | rund zehn Sekunden |
| 10⁹ | Minuten |
| 10¹⁰ | halbe Stunde |
| 10¹² | Tage |

!!! warning "Diese Rechnung ist absichtlich grob"
    Der Tabelle liegt eine Annahme zugrunde: **Python schafft rund 10⁷ Schritte
    pro Sekunde, und jeder Schritt ist gleich teuer.** Beides stimmt nicht genau.

    - Ein Schleifendurchlauf mit Multiplikation und Listenzugriff dauert länger
      als einer mit einem einzigen Vergleich — leicht ein Faktor 3.
    - Dein Gerät rechnet schneller oder langsamer als das der Nachbarin.
    - Sehr grosse Listen werden zusätzlich langsamer.

    Zusammen kann das eine Grössenordnung ausmachen. Trotzdem reicht die
    Näherung, denn die Unterschiede, um die es geht, sind **Faktoren von tausend
    und mehr**. Ob 10⁸ Schritte nun sieben oder dreissig Sekunden dauern, ändert
    an keiner Entscheidung etwas. Ob es 10⁸ oder 10¹² sind, entscheidet alles.

    **Schätze also die Grössenordnung, nie die Sekunden.**

### Dein Budget sind fünf Minuten, keine Sekunde

Hier weicht unser Kurs von allem ab, was du sonst über Wettbewerbsprogrammierung
liest. Dort gilt meist ein Zeitlimit von ein bis zwei Sekunden, und das
Programm wird abgebrochen, wenn es länger braucht.

**Bei uns nicht.** Wir laden eine Ausgabedatei hoch, kein Programm. Niemand misst
deine Laufzeit. Die einzige Uhr sind die fünf Minuten zwischen Download und
Upload.

| Schritte insgesamt | Grössenordnung | Urteil |
|---|---|---|
| bis 10⁸ | Sekunden | unproblematisch |
| 10⁹ | Minuten | ohne Reserve für einen zweiten Versuch |
| ab 10¹⁰ | halbe Stunde und mehr | ausgeschlossen |

Daraus folgt eine Regel, die überraschend viel erklärt:

> **Kleine Unterschiede sind egal. Grosse sind tödlich.**

Ob dein Programm einen Sekundenbruchteil oder ein paar Sekunden braucht, ändert
an deiner Punktzahl nichts. Zwischen Sekunden und Tagen liegt dagegen alles.
Deshalb geht es beim Laufzeitdenken um **Grössenordnungen**, nie um Feinschliff —
und deshalb darf die Rechnung so grob sein.

### Die Rechnung für Endurance

| | Schritte pro Testfall | mal T = 100 | Grössenordnung |
|---|---|---|---|
| Teilaufgabe 2, O(N²), N = 100 | 10⁴ | 10⁶ | Sekundenbruchteil |
| Teilaufgabe 3, O(N²), N = 10⁵ | 10¹⁰ | 10¹² | Tage |
| Teilaufgabe 3, O(N), N = 10⁵ | 10⁵ | 10⁷ | rund eine Sekunde |

Dieselbe Lösung, dieselbe Aufgabe, nur eine andere Zahl in den Limits — und der
Unterschied zwischen „läuft sofort" und „wird nie fertig".

### Ein einziger Durchgang

Die schnelle Lösung schaut jede Position **genau einmal** an und führt dabei zwei
Zahlen mit: die laufende Länge und das bisher beste Ergebnis.

Während die Schleife läuft, gilt durchgehend:

> **`laenge` ist die Länge des lochfreien Stücks, das an der aktuellen Position
> endet. `bestes` ist das längste lochfreie Stück, das ganz links davon liegt
> oder hier endet.**

Am Ende ist die ganze Strasse angeschaut, und `bestes` ist die Antwort. Das ist
die **Invariante** aus M2, nur schärfer formuliert: Sie erlaubt, das Ergebnis für
eine Position aus dem Ergebnis der vorherigen abzuleiten, statt neu zu zählen.

Genau das ist der Sprung von O(N²) auf O(N): **weitergeben statt neu berechnen.**

### Was du nicht siehst: das Einlesen zählt mit

Bei N = 100 000 und T = 100 stehen **zehn Millionen Zahlen** in der
Eingabedatei.

Jede einzelne davon muss gelesen und in eine Zahl umgewandelt werden. Das ist
selbst eine Schleife über die ganze Eingabe, also **O(N · T)** — dieselbe
Grössenordnung wie dein Algorithmus. Der Aufwand steht nirgends im Code, den du
schreibst, aber er ist da.

Daraus folgt eine Grenze, die du nicht unterbieten kannst:

> **Dein Programm kann nie schneller sein als das Einlesen.**

Bei Endurance Teilaufgabe 3 sind beide Teile gleich gross. Das ist ein gutes
Zeichen: Wenn das Einlesen mit dem Algorithmus gleichzieht, ist beim Algorithmus
nichts mehr zu holen.

Gefährlich wird es, wenn die Eingabe grösser ist als nötig. Eine Aufgabe mit
N ≤ 10⁶ und T = 100 hat **hundert Millionen Zahlen** in der Eingabe. Das sind
allein fürs Einlesen 10⁸ Schritte — dort wird selbst eine perfekte O(N)-Lösung
unangenehm, und die Datei ist mehrere hundert Megabyte gross.

Merk dir: Die Grösse der Eingabe ist Teil der Laufzeit.

### Die versteckte Schleife

Nicht jede Schleife ist als Schleife zu erkennen. Manche stecken in einer
harmlosen Zeile:

```python
liste.pop(0)
```

Das entfernt das **erste** Element einer Liste. Dabei müssen alle übrigen
Elemente um einen Platz nach vorne rücken — das ist selbst eine Schleife über
die ganze Liste. Wer `pop(0)` in einer Schleife aufruft, hat O(N²) geschrieben,
ohne eine zweite Schleife zu tippen.

Zähl nach, was es kostet, eine Liste mit N Elementen so ganz zu leeren:

| | Schritte pro Aufruf | Schritte insgesamt | |
|---|---|---|---|
| `pop(0)` (vorne) | bis zu N | rund N² / 2 | O(N²) |
| `pop()` (hinten) | 1 | N | O(N) |

Beim ersten Aufruf rücken N−1 Elemente nach, beim zweiten N−2, und so weiter.
Diese Summe ist ungefähr N²/2.

Die Signatur erkennst du beim Messen: Bei `pop(0)` brauchen **doppelt so viele
Elemente etwa viermal so lange**, bei `pop()` nur doppelt so lange. In den
Übungen misst du genau das selbst.

`pop()` ohne Argument nimmt das letzte Element — dahinter steht nichts, was
verschoben werden müsste, also ein Schritt unabhängig von der Länge.

### Die Analogie und ihre Grenze

> **Analogie:** Für jede Bodenplatte zurückgehen und neu loslaufen, statt einmal
> durchzugehen.

**Bruchstelle:** Die Analogie zeigt dir die Verschwendung, aber nicht, was du
stattdessen tun sollst. Sie verführt ausserdem zu der Annahme, Wiederholung
lasse sich immer vermeiden. Das stimmt nicht. Bei manchen Problemen hilft kein
einzelner Durchgang, sondern erst eine andere Anordnung der Daten — Sortieren
etwa, und das kommt in M5.

Was sie richtig zeigt: Wenn du beim zweiten Durchgang dasselbe erfährst wie beim
ersten, war der zweite überflüssig.

---

## Prüfe dich selbst

??? success "Vergleiche deine Antwort — Frage 1"
    **Eine Aufgabe hat N ≤ 200 000 und T = 100. Du hast eine O(N²)-Lösung.
    Reicht das?**

    Nein, und zwar nicht knapp.

    200 000² sind 4 · 10¹⁰ Schritte pro Testfall, mal 100 also rund 10¹².
    Grössenordnung: Tage.

    Wichtig ist nicht die genaue Zahl, sondern die Grössenordnung. Ob es zwei
    oder acht Tage werden, spielt keine Rolle — alles ab etwa 10¹⁰ ist
    ausserhalb deines Budgets. Diese Rechnung machst du auf Papier in einer
    Minute.

??? success "Vergleiche deine Antwort — Frage 2"
    **Deine Rechnung ergibt 10⁹ Schritte. Ist das ein Problem?**

    Grenzwertig — und du solltest es wissen, bevor du herunterlädst.

    10⁹ Schritte sind die Grössenordnung von Minuten. Das passt in die fünf
    Minuten, aber ohne Reserve: Wenn etwas schiefgeht und du noch einmal starten
    musst, wird es knapp. Und ob es bei dir eine Minute oder fünf werden, sagt
    dir die Schätzung nicht.

    Genau hier lohnt sich das Messen — nicht als Ersatz für die Schätzung,
    sondern als Kontrolle: einmal mit dem Beispiel laufen lassen, hochrechnen,
    und **dann** herunterladen. Nicht umgekehrt.

??? success "Vergleiche deine Antwort — Frage 3"
    **Warum ist `while liste: liste.pop(0)` langsam, `while liste: liste.pop()`
    aber nicht?**

    Weil `pop(0)` alle übrigen Elemente um einen Platz nach vorne schiebt. Bei
    einer Liste mit N Elementen ist dieser eine Aufruf also selbst N Schritte
    wert, und N solche Aufrufe ergeben O(N²).

    `pop()` nimmt das letzte Element. Dahinter steht nichts, was verschoben
    werden müsste — ein Schritt, unabhängig von der Länge.

    Die allgemeine Lehre: Eine Zeile ist nicht deshalb billig, weil sie kurz
    ist. Frag bei jeder Listenoperation, wie viele Elemente sie anfassen muss.

??? success "Vergleiche deine Antwort — Frage 4"
    **Du liest eine neue Aufgabe. Teilaufgabe 1 hat N ≤ 100, Teilaufgabe 2 hat
    N ≤ 100 000. Was weisst du, bevor du die Aufgabe überhaupt verstanden hast?**

    Dass für Teilaufgabe 2 eine grundsätzlich andere Idee nötig ist.

    Ein Sprung von 100 auf 100 000 ist kein Sprung, den man mit sauberer
    Programmierung überbrückt. Der Faktor 1000 in N bedeutet Faktor 1 000 000
    bei O(N²). Die Aufgabenstellenden trennen mit dieser Schranke absichtlich
    zwei Lösungswege.

    Umgekehrt gilt genauso: Wenn eine Teilaufgabe N ≤ 100 erlaubt, ist Brute
    Force dort nicht nur geduldet, sondern **beabsichtigt**.

---

## Übungen

Weiter geht es mit [den Übungen zu M3](uebungen.md): Treppenlauf, wo dich deine
alte Lösung weiter trägt als gedacht, eine versteckte Bremse zum Selbermessen
und eine Schätzrunde über echte Aufgabenschranken.

---

## Weiter zu M4

Wenn du Endurance Teilaufgabe 3 gelöst hast, kannst du aus einer Schranke
ablesen, welche Lösung überhaupt in Frage kommt — und du hast einmal erlebt,
wie aus O(N²) ein einzelner Durchgang wird.

In [M4 — Felder und lineare Techniken](../m04-lineare-techniken/index.md) wird
daraus ein Werkzeug. Der Trick „weitergeben statt neu berechnen" hat einen Namen
und mehrere Formen: Präfixsummen und Zweizeiger. Damit fallen Teilaufgabe 4 und 5
von Endurance — und Treppenlauf Teilaufgabe 4, die du hier nur diagnostiziert
hast.
