# M3 — Musterlösungen

Diese Seite verrät die Lösung. Hast du es wirklich selbst versucht?

---

## Endurance, Teilaufgabe 3

**Die Schätzung zuerst.** Die Lösung aus M2 hat zwei Schleifen, also O(N²). Mit
N = 100 000 sind das 10¹⁰ Schritte pro Testfall und mal T = 100 insgesamt 10¹².
Grössenordnung: Tage. Die alte Lösung scheidet aus, und das weisst du in zwei
Minuten auf Papier — ohne sie je gestartet zu haben.

**Der Durchgang.** Eine Schleife über die Strasse, zwei Zahlen im Gepäck:

```python
T = zahl()

zeilen = []
for i in range(T):
    N = zahl()
    p = zahlen(N)

    bestes = 0
    laenge = 0
    for wert in p:
        if wert == 1:
            laenge = 0
        else:
            laenge = laenge + 1
            if laenge > bestes:
                bestes = laenge

    zeilen.append("Case #" + str(i) + ": " + str(bestes))

pruefe.schreibe(AUSGABE, zeilen)
```

Der Unterschied zu M2 ist eine einzige gestrichene Schleife. Statt für jeden
Startpunkt neu zu zählen, wird `laenge` weitergereicht und nur bei einem Loch
zurückgesetzt.

**Dieses Programm löst Teilaufgabe 1, 2 und 3** — zusammen 60 Punkte. Wenn du in
M2 schon eingereicht hast, kommen jetzt 20 dazu.

Zum Testen dasselbe Beispiel wie in M2, `bsp_ein.txt`:

```
2
3
1 0 0
3
0 1 0
```

und `bsp_aus.txt`:

```
Case #0: 2
Case #1: 1
```

Prüf zusätzlich `1 1 1` (Antwort 0) und eine Strasse ganz ohne Löcher.

??? tip "Wo die Zeit hingeht"
    Mit der grösstmöglichen Eingabe — 100 Testfälle zu je 100 000 Zahlen —
    stehen zehn Millionen Zahlen in der Datei. Zwei Teile kosten Zeit, und beide
    sind O(N · T), also 10⁷ Schritte:

    - die zehn Millionen Zahlen lesen und umwandeln
    - der Durchgang deines Algorithmus

    Der Algorithmus ist damit nicht mehr der teuerste Teil, sondern
    gleichauf — beim Messen liegt das Einlesen sogar vorn. Das ist ein gutes
    Zeichen: Wenn das Einlesen mithält, ist bei der Rechnung nichts mehr zu
    holen.

    Insgesamt bleibt es bei der Grössenordnung von Sekunden.

---

## Treppenlauf, Teilaufgabe 3 und 4

**Die Schätzung.** Beide Male dieselbe Lösung mit zwei Schleifen, O(N²):

| | N | pro Testfall | mal T = 100 | Grössenordnung | |
|---|---|---|---|---|---|
| ST3 | 1 000 | 10⁶ | 10⁸ | Sekunden | **läuft** |
| ST4 | 100 000 | 10¹⁰ | 10¹² | Tage | ausgeschlossen |

**Teilaufgabe 3 kannst du mit deiner alten Lösung einreichen.** Ein paar Sekunden
sind lang genug, dass du dich fragst, ob etwas hängt — und kurz genug, dass es
innerhalb der fünf Minuten völlig unproblematisch ist. 25 Punkte, ohne eine Zeile
neuen Code.

Das ist die praktische Seite des Moduls: Laufzeitdenken sagt dir nicht nur, wann
du aufhören musst, sondern auch, wann du **weitermachen darfst**. Wer bei 10⁸
Schritten reflexhaft nach einer besseren Lösung sucht, verschenkt Zeit.

**Teilaufgabe 4 braucht eine andere Idee.** Nötig wäre O(N) oder O(N log N).

Die Diagnose reicht für dieses Modul. Falls du wissen willst, wohin es geht: Die
gesuchte Grösse ist das Maximum von `a[i] + b[j] + Abstand` über alle Paare. Man
kann die Summe so umformen, dass sich die beiden Seiten trennen lassen — dann
genügt ein Durchgang, der unterwegs das beste bisher gesehene Teilstück
mitführt. Das ist genau die Technik aus M4.

---

## Die versteckte Bremse

**1. und 2. Die Messung.** Deine Sekundenwerte sind andere als die deiner
Nachbarin — darauf kommt es nicht an. Entscheidend ist der **Faktor** zwischen
den beiden Läufen.

Bei doppelt so vielen Zahlen wirst du ungefähr das **Vierfache** an Zeit sehen,
oft auch mehr. Doppelt so lange wäre O(N), viermal so lange ist O(N²). Also
verhält sich das Programm quadratisch, obwohl nur eine Schleife dasteht.

(Dass es oft mehr als das Vierfache wird, liegt an Speichereffekten bei grossen
Listen. Die Zählung sagt N²/2 Schritte voraus; die Wirklichkeit ist etwas
schlechter. Für das Urteil „quadratisch" spielt das keine Rolle.)

**3. Die versteckte Schleife** steht hier:

```python
    if zahl not in gesehen:
```

Python kennt den Inhalt der Liste nicht auswendig. Um `not in` zu beantworten,
geht es die Liste **von vorne bis hinten durch** und vergleicht jedes Element.
Ist die Antwort „nein, kommt nicht vor", wurde die ganze Liste angeschaut.

Diese eine Zeile ist also eine vollständige Schleife über `gesehen`. Da sie für
jede der N Zahlen ausgeführt wird und `gesehen` mitwächst, sind es insgesamt
rund N²/2 Vergleiche.

**4. Was das Programm bei jeder Zahl tut:** Es durchsucht alle bisher gefundenen
verschiedenen Zahlen, um festzustellen, ob die neue schon dabei war.

### Der Ausweg: eine Menge statt einer Liste

Python hat für genau diese Frage einen eigenen Typ. Ein **set** (eine Menge)
merkt sich, welche Werte enthalten sind, und kann `in` beantworten, ohne alles
durchzugehen:

```python
gesehen = set()
for zahl in zahlen:
    if zahl not in gesehen:
        gesehen.add(zahl)

print("Verschiedene:", len(gesehen))
```

Statt `append` heisst es `add`, sonst ist alles gleich.

Damit wird aus O(N²) ein O(N): Die Frage `in` kostet bei einem set einen Schritt
statt N. Miss es nach — der Unterschied liegt bei diesen Grössen im Bereich von
Faktor hundert und mehr, und er wächst mit N weiter.

| | Schritte insgesamt | |
|---|---|---|
| Liste, `in` durchsucht alles | rund N² / 2 | O(N²) |
| set, `in` fragt direkt | N | O(N) |

**Wann nimmst du was?** Eine Liste, wenn die Reihenfolge zählt oder du über alle
Elemente laufen willst. Ein set, wenn du nur wissen musst, **ob** etwas dabei
ist. Dieselbe Frage, ein anderer Behälter, eine andere Komplexität.

Ein set hat keine Reihenfolge und speichert jeden Wert nur einmal — hier stört
beides nicht, im Gegenteil.

---

## Schätzrunde

| | Schritte insgesamt | Grössenordnung | Urteil |
|---|---|---|---|
| a | 10³ · 10³ · 100 = 10⁸ | Sekunden | einreichen |
| b | 10⁵ · 10⁵ · 100 = 10¹² | Tage | ausgeschlossen |
| c | 10⁵ · 100 = 10⁷ | rund eine Sekunde | einreichen |
| d | 10⁶ · 100 = 10⁸ | Sekunden — **aber siehe unten** | prüfen! |
| e | 100³ · 100 = 10⁸ | Sekunden | einreichen |

**Zeile e ist die Überraschung.** Drei ineinander liegende Schleifen klingen nach
Katastrophe, aber bei N ≤ 100 sind es genau gleich viele Schritte wie in Zeile a.
Die Komplexität allein sagt nichts — erst zusammen mit der Schranke.

**Zeile d ist die Falle.** Die Komplexität ist in Ordnung: O(N) bei N = 10⁶ macht
10⁸ Schritte, also Sekunden. Das Problem steht woanders.

Bei N = 10⁶ und T = 100 stehen **hundert Millionen Zahlen** in der Eingabedatei.
Das sind mehrere hundert Megabyte. Deine Vorlage liest die ganze Datei ein und
zerlegt sie in Wörter — und diese Wortliste braucht ein Vielfaches der
Dateigrösse an Arbeitsspeicher. Zum Vergleich: Endurance Teilaufgabe 3 kommt auf
zehn Millionen Zahlen und rund 20 Megabyte, und das läuft problemlos.

Praktische Konsequenz, und sie kostet nichts: **Schau nach dem Download auf die
Dateigrösse.** Eine Eingabedatei von 200 MB ist ein Warnsignal, bevor du
überhaupt startest. Wenn die echten Testdaten kleiner ausfallen als der
schlimmste erlaubte Fall, ist alles gut — aber das siehst du erst an der Datei,
nicht an der Aufgabenstellung.

Die allgemeine Lehre aus dieser Zeile: **Die Grösse der Eingabe ist Teil der
Laufzeit.** Eine perfekte O(N)-Lösung hilft nicht, wenn N Zahlen einzulesen schon
zu lange dauert.

---

Zurück zu [den Übungen](uebungen.md) oder zum
[Lernbaustein](index.md).
