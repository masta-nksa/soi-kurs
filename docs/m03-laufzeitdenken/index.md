# M3 — Laufzeitdenken

!!! note "Du kannst hier einsteigen, wenn ..."
    ... du zu einem neuen Problem selbständig die drei Fragen beantwortest — was
    ist eine Möglichkeit, wie zähle ich alle auf, woran erkenne ich die beste —
    und eine Lösung schreiben kannst, die alle Möglichkeiten durchgeht. Das ist
    der Inhalt von [M2](../m02-vollstaendige-suche/index.md).

    **Bring deine Lösung von Ausdauer Teilaufgabe 2 mit.** Dieses Modul baut
    direkt auf ihr auf.

**In diesem Modul:** [Komplexität und Faktor T](#komplexitat-und-faktor-t)
· [Weitergeben statt neu berechnen](#weitergeben-statt-neu-berechnen)
· [Versteckte Schleifen](#versteckte-schleifen)
· [Mengen und Wörterbücher](#mengen-und-worterbucher)

Deine Lösung aus M2 ist **richtig**. Sie findet für jede Strasse die korrekte
Antwort, auch für eine mit 100 000 Abschnitten. Starte sie mit dieser Eingabe,
und sie wird trotzdem nie fertig.

Das ist die unangenehmste Sorte Fehler: keine Fehlermeldung, keine falsche Zahl,
nichts zum Debuggen. Nur ein Programm, das läuft und läuft. Dieses Modul bringt
dir bei, ihn zu sehen, **bevor** er passiert.

---

## Komplexität und Faktor T

### Worum es geht

In der Aufgabenstellung steht nicht zufällig N ≤ 100 000. Wer die Aufgabe
gestellt hat, hat sich bei jeder Teilaufgabe überlegt, welche Lösungen damit noch
durchlaufen und welche nicht.

Die Schranke ist also keine Randnotiz. Sie ist eine Nachricht an dich.

### Die Idee

> **Kernsatz:** Die Schranke sagt dir, welche Komplexität erlaubt ist. Lies sie,
> bevor du programmierst — nicht danach.

Die Rechnung geht immer gleich, in vier Schritten:

1. **Schleifen zählen.** Ineinander liegende Schleifen über die Eingabe: eine
   ist O(N), zwei sind O(N²), drei sind O(N³).
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

### An einem Beispiel

Dieselbe Aufgabe, dieselbe Lösung, nur eine andere Zahl in den Limits:

| | Schritte pro Testfall | mal T = 100 | Grössenordnung |
|---|---|---|---|
| Teilaufgabe 2, O(N²), N = 100 | 10⁴ | 10⁶ | Sekundenbruchteil |
| Teilaufgabe 3, O(N²), N = 10⁵ | 10¹⁰ | 10¹² | Tage |
| Teilaufgabe 3, O(N), N = 10⁵ | 10⁵ | 10⁷ | rund eine Sekunde |

Zwischen der zweiten und dritten Zeile liegt der Unterschied zwischen „wird nie
fertig" und „läuft sofort" — bei identischer Aufgabe.

### Dein Budget sind fünf Minuten, keine Sekunde

Hier weicht dieser Kurs von allem ab, was du sonst über
Wettbewerbsprogrammierung liest. Dort gilt meist ein Zeitlimit von ein bis zwei
Sekunden, und das Programm wird abgebrochen, wenn es länger braucht.

**Bei uns nicht.** Wir laden eine Ausgabedatei hoch, kein Programm. Niemand
misst deine Laufzeit. Die einzige Uhr sind die fünf Minuten zwischen Download
und Upload.

| Schritte insgesamt | Grössenordnung | Urteil |
|---|---|---|
| bis 10⁸ | Sekunden | unproblematisch |
| 10⁹ | Minuten | ohne Reserve für einen zweiten Versuch |
| ab 10¹⁰ | halbe Stunde und mehr | ausgeschlossen |

Daraus folgt eine Regel, die überraschend viel erklärt:

> **Kleine Unterschiede sind egal. Grosse sind tödlich.**

Ob dein Programm einen Sekundenbruchteil oder ein paar Sekunden braucht, ändert
an deiner Punktzahl nichts. Zwischen Sekunden und Tagen liegt dagegen alles.

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

    **Schätze die Grössenordnung, nie die Sekunden.**

### Wann du es brauchst

Vor dem Programmieren. Immer. Die Rechnung dauert eine Minute auf Papier und
entscheidet, ob die nächste halbe Stunde sinnvoll investiert ist.

Woran du merkst, dass du es übersprungen hast:

- Du startest dein Programm mit der echten Eingabe und wartest, ob es fertig
  wird. Das ist keine Messung, das ist Hoffen.
- Du liest die Limits erst, wenn etwas nicht funktioniert.
- Du kannst nicht sagen, welche Komplexität deine eigene Lösung hat.

### Typische Fallen

- **Den Faktor T vergessen.** Der häufigste Fehler überhaupt. N ≤ 1000 mit
  O(N²) klingt nach 10⁶ und ist in Wahrheit 10⁸.
- **Sekunden statt Grössenordnungen.** Wer „17,4 Sekunden" schätzt, täuscht eine
  Genauigkeit vor, die die Rechnung nicht hergibt.
- **Die Schranke als Warnung lesen statt als Einladung.** N ≤ 100 heisst nicht
  „pass auf", sondern „hier ist Brute Force beabsichtigt".

---

## Weitergeben statt neu berechnen

### Worum es geht

Teilaufgabe 3 der Ausdauer verlangt eine Lösung, die jede Position **einmal**
anschaut statt N-mal. Aber wie soll das gehen — man muss doch alle Abschnitte
prüfen?

Muss man nicht. Man muss nur aufhören, dieselbe Information wegzuwerfen.

### Die Idee

> **Kernsatz:** Wenn du für jede Position dasselbe neu ausrechnest, was du an der
> vorherigen schon wusstest, dann gib es weiter statt es neu zu berechnen.

Bei der Ausdauer führst du beim Durchgehen zwei Zahlen mit: die **laufende**
Länge und die **beste bisher**. Während die Schleife läuft, gilt:

> **`laenge` ist die Länge des lochfreien Stücks, das an der aktuellen Position
> endet. `bestes` ist das längste lochfreie Stück, das hier oder weiter links
> endet.**

Das ist die Invariante aus [M2](../m02-vollstaendige-suche/index.md#die-invariante),
nur schärfer: Sie erlaubt, das Ergebnis für eine Position aus dem Ergebnis der
vorherigen abzuleiten.

> **Analogie:** Du willst wissen, wie viele Schritte du am Stück gehen kannst,
> ohne auf eine Fuge zu treten. Du stellst dich auf die erste Bodenplatte und
> gehst los, bis eine Fuge kommt. Dann gehst du zurück, stellst dich auf die
> zweite Platte und gehst wieder los. Dann auf die dritte. Bei zwanzig Platten
> ist das mühsam, bei hunderttausend gehst du dieselbe Strecke immer wieder ab,
> obwohl sich am Boden nichts ändert.
>
> **Bruchstelle:** Die Analogie zeigt die Verschwendung, aber nicht, was du
> stattdessen tun sollst. Sie verführt ausserdem zu der Annahme, Wiederholung
> lasse sich immer vermeiden. Das stimmt nicht: Bei manchen Problemen hilft kein
> einzelner Durchgang, sondern erst eine andere Anordnung der Daten — Sortieren
> etwa, und das kommt in [M5](../m05-sortieren-und-suchen/index.md).

### An einem Beispiel

Die Strasse `0 0 1 0 0 0`, ein Durchgang von links nach rechts:

```
Position:      0    1    2    3    4    5
Wert:          0    0    1    0    0    0

laenge:        1    2    0    1    2    3
bestes:        1    2    2    2    2    3
```

An Position 2 kommt ein Loch: `laenge` fällt auf 0, `bestes` bleibt bei 2 — das
bisher Gefundene ist nicht verloren, es steckt schon in `bestes`. Ab Position 3
wächst `laenge` wieder und überholt am Schluss.

### Im Code

```python
def loese(n, p):
    bestes = 0
    laenge = 0
    for i in range(n):
        if p[i] == 1:
            laenge = 0
        else:
            laenge = laenge + 1
        if laenge > bestes:
            bestes = laenge
    return bestes
```

Bei **jedem** Schritt vergleichen, nicht nur beim Loch. Sonst geht das letzte
Stück verloren, wenn die Strasse ohne Loch endet.

### Laufzeit

Eine Schleife über N Positionen: **O(N)**. Bei N = 10⁵ und T = 100 sind das 10⁷
Schritte — rund eine Sekunde.

Aus O(N²) wird O(N), weil jede Position genau einmal angeschaut wird statt
einmal pro möglichem Startpunkt.

### Woran du es erkennst

- Deine Lösung hat **zwei ineinander liegende Schleifen**, und die innere fängt
  jedes Mal wieder von vorne an.
- Zwei benachbarte Durchläufe der äusseren Schleife rechnen **fast dasselbe** —
  sie unterscheiden sich nur an einem Ende.
- Du könntest die Antwort für Position i leicht angeben, **wenn du die Antwort
  für Position i−1 kennen würdest**.

Der letzte Punkt ist der zuverlässigste Test. Wenn du diesen Satz formulieren
kannst, ist die Lösung meist schon da.

### Typische Fallen

- **Zu wenig mitführen.** Bei der Ausdauer sind es zwei Zahlen. Wer nur eine
  mitführt, verliert entweder das laufende Stück oder das beste.
- **Am Ende nicht vergleichen.** Der klassische Fehler, wenn man nur beim Loch
  vergleicht und die Strasse ohne Loch endet.
- **Zu früh optimieren.** In M2 war O(N²) richtig. Weitergeben lohnt sich erst,
  wenn die Schranke es verlangt — und das sagt dir die Rechnung von oben.

---

## Versteckte Schleifen

### Worum es geht

Nicht jede Schleife sieht aus wie eine Schleife. Manche stecken in einer Zeile,
die harmlos aussieht — und kippen die Komplexität, ohne dass du eine zweite
Schleife tippst.

### Die Idee

> **Kernsatz:** Eine Zeile ist nicht deshalb billig, weil sie kurz ist. Frag bei
> jeder Operation, wie viele Elemente sie anfassen muss.

### An einem Beispiel

```python
liste.pop(0)
```

Das entfernt das **erste** Element. Dabei müssen alle übrigen um einen Platz
nach vorne rücken — das ist selbst eine Schleife über die ganze Liste.

| | Schritte pro Aufruf | eine Liste ganz leeren | |
|---|---|---|---|
| `pop(0)` (vorne) | bis zu N | rund N² / 2 | O(N²) |
| `pop()` (hinten) | 1 | N | O(N) |

Beim ersten Aufruf rücken N−1 Elemente nach, beim zweiten N−2, und so weiter.
Diese Summe ist ungefähr N²/2.

Die zweite häufige Falle:

```python
if zahl not in gesehen:      # gesehen ist eine Liste
```

Python kennt den Inhalt einer Liste nicht auswendig. Um `in` zu beantworten,
geht es sie **von vorne bis hinten durch**. Steht die Zahl nicht drin, wurde die
ganze Liste angeschaut. In einer Schleife über N Zahlen ergibt das wieder O(N²).

### Wann du es brauchst

Beim Schleifenzählen aus dem ersten Konzept. Wenn du O(N) herausbekommst, dein
Programm aber deutlich langsamer ist als erwartet, steckt fast immer eine
versteckte Schleife drin.

Woran du sie findest: Geh deinen Schleifenrumpf Zeile für Zeile durch und frag
bei jeder, wie viele Elemente sie berührt. Verdächtig sind alle Operationen auf
Listen und Zeichenketten, bei denen kein Index dabeisteht.

**Die Signatur beim Messen:** Bei O(N²) brauchen doppelt so viele Elemente rund
**viermal** so lange, bei O(N) doppelt so lange. Achte nicht auf die Sekunden,
sondern auf den Faktor. In den Übungen misst du das selbst.

### Typische Fallen

- **`pop(0)` statt `pop()`.** Wenn du die Reihenfolge nicht brauchst, nimm das
  letzte Element.
- **`x in liste` in einer Schleife.** Der Ausweg ist das nächste Konzept.
- **Das Einlesen vergessen.** Bei N = 10⁵ und T = 100 stehen **zehn Millionen
  Zahlen** in der Eingabedatei. Jede muss gelesen und umgewandelt werden, das ist
  O(N · T) — dieselbe Grössenordnung wie ein guter Algorithmus.

    > **Dein Programm kann nie schneller sein als das Einlesen.**

    Bei der Ausdauer ziehen beide gleich, das ist ein gutes Zeichen. Gefährlich
    wird es bei N ≤ 10⁶ und T = 100: Das sind hundert Millionen Zahlen, allein
    fürs Einlesen 10⁸ Schritte, und die Datei ist mehrere hundert Megabyte
    gross. Die Grösse der Eingabe ist Teil der Laufzeit.

---

## Mengen und Wörterbücher

### Worum es geht

Du willst wiederholt wissen: **Habe ich diesen Wert schon gesehen?** Mit einer
Liste kostet jede solche Frage O(N) — das ist die versteckte Schleife von eben.

Python hat für genau diese Frage einen eigenen Behälter.

### Die Idee

> **Kernsatz:** Wenn du oft fragst, *ob* ein Wert dabei ist, nimm ein `set`
> statt einer Liste. Die Frage kostet dann einen Schritt statt N.

Ein **set** (eine Menge) merkt sich, welche Werte enthalten sind, und beantwortet
`in` ohne alles durchzugehen. Ein **dict** (ein Wörterbuch) tut dasselbe und
speichert zu jedem Wert zusätzlich etwas ab — etwa, wie oft er vorkam.

### An einem Beispiel

Zählen, wie viele **verschiedene** Zahlen in einer Liste vorkommen:

```python
gesehen = []                      # langsam: O(N²)
for zahl in zahlen:
    if zahl not in gesehen:
        gesehen.append(zahl)
```

```python
gesehen = set()                   # schnell: O(N)
for zahl in zahlen:
    gesehen.add(zahl)

anzahl = len(gesehen)
```

Statt `append` heisst es `add`, sonst ist alles gleich. Ein set speichert jeden
Wert ohnehin nur einmal, die Abfrage `if` kann also ganz entfallen.

Ein `dict`, wenn du zusätzlich zählen willst:

```python
anzahl = {}
for zahl in zahlen:
    if zahl in anzahl:
        anzahl[zahl] = anzahl[zahl] + 1
    else:
        anzahl[zahl] = 1
```

### Laufzeit

| | eine Frage | N Fragen | |
|---|---|---|---|
| Liste, `in` durchsucht alles | O(N) | rund N² / 2 | O(N²) |
| set oder dict, `in` fragt direkt | O(1) | N | O(N) |

Bei 20 000 Zahlen ist der Unterschied schon ein Faktor in der Grössenordnung von
hundert, und er wächst mit N weiter.

### Woran du es erkennst

- In deiner Schleife steht `in` auf einer **Liste**, die selbst mitwächst.
- Die Aufgabe fragt nach **verschiedenen**, **doppelten** oder **schon
  gesehenen** Werten.
- Du willst zu einem Wert etwas nachschlagen — dann ein `dict`.

### Typische Fallen

- **Ein set hat keine Reihenfolge.** Wer die Reihenfolge braucht, nimmt eine
  Liste — oder beides nebeneinander.
- **Ein set speichert jeden Wert nur einmal.** Beim Zählen von Duplikaten ist
  ein `dict` der richtige Behälter.
- **`in` auf einer Liste sieht genauso aus wie `in` auf einem set.** Der
  Unterschied steht nirgends im Code, nur im Typ. Genau deshalb ist die Falle so
  gemein.

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
    musst, wird es knapp.

    Genau hier lohnt sich das Messen — nicht als Ersatz für die Schätzung,
    sondern als Kontrolle: einmal mit einem grossen selbstgebauten Testfall
    laufen lassen, hochrechnen, und **dann** herunterladen. Nicht umgekehrt.

??? success "Vergleiche deine Antwort — Frage 3"
    **Warum ist `while liste: liste.pop(0)` langsam, `while liste: liste.pop()`
    aber nicht?**

    Weil `pop(0)` alle übrigen Elemente um einen Platz nach vorne schiebt. Bei
    einer Liste mit N Elementen ist dieser eine Aufruf also selbst N Schritte
    wert, und N solche Aufrufe ergeben O(N²).

    `pop()` nimmt das letzte Element. Dahinter steht nichts, was verschoben
    werden müsste — ein Schritt, unabhängig von der Länge.

??? success "Vergleiche deine Antwort — Frage 4"
    **Du liest eine neue Aufgabe. Teilaufgabe 1 hat N ≤ 100, Teilaufgabe 2 hat
    N ≤ 100 000. Was weisst du, bevor du die Aufgabe überhaupt verstanden hast?**

    Dass für Teilaufgabe 2 eine grundsätzlich andere Idee nötig ist.

    Ein Sprung von 100 auf 100 000 lässt sich nicht mit sauberer Programmierung
    überbrücken. Der Faktor 1000 in N bedeutet Faktor 1 000 000 bei O(N²). Die
    Aufgabenstellenden trennen mit dieser Schranke absichtlich zwei Lösungswege.

    Umgekehrt gilt genauso: Wenn eine Teilaufgabe N ≤ 100 erlaubt, ist Brute
    Force dort nicht nur geduldet, sondern **beabsichtigt**.

??? success "Vergleiche deine Antwort — Frage 5"
    **Dein Programm hat eine einzige Schleife über N Elemente und ist trotzdem
    viel langsamer, als O(N) erwarten lässt. Wo suchst du?**

    Im Schleifenrumpf, Zeile für Zeile: Welche davon fasst mehr als ein Element
    an?

    Die üblichen Verdächtigen sind `x in liste`, `liste.pop(0)`,
    `liste.insert(0, x)` und das Zusammenkleben von Zeichenketten mit `+` in
    einer Schleife. Alle vier sehen aus wie ein Schritt und sind N.

    Die Gegenprobe ist eine Messung: Verdopple die Eingabe. Braucht es viermal
    so lange, ist irgendwo eine versteckte Schleife.

---

## Übungen

Weiter geht es mit [den Übungen zu M3](uebungen.md): Treppenlauf, wo dich deine
alte Lösung weiter trägt als gedacht, eine versteckte Bremse zum Selbermessen
und eine Schätzrunde über echte Aufgabenschranken.

---

## Weiter zu M4

Wenn du Ausdauer Teilaufgabe 3 gelöst hast, kannst du aus einer Schranke
ablesen, welche Lösung überhaupt in Frage kommt — und du hast einmal erlebt, wie
aus O(N²) ein einzelner Durchgang wird.

In [M4 — Felder und lineare Techniken](../m04-lineare-techniken/index.md) wird
daraus ein Werkzeug. „Weitergeben statt neu berechnen" hat zwei feste Formen:
Präfixsummen und Zweizeiger. Damit fallen Teilaufgabe 4 und 5 der Ausdauer — und
Treppenlauf Teilaufgabe 4, die du hier nur diagnostiziert hast.
