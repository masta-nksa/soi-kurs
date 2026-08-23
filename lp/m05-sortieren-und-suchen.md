# M5 — Sortieren und Suchen (Lehrperson)

**LP-Wert: mittel.** Das Konzept selbst ist leicht — `sort()` aufrufen kann
jede und jeder. Begleitung brauchen zwei andere Dinge: die Einsicht bei
Thermalquellen, dass es überhaupt nur *einen* Kandidaten gibt, und die
Laufzeitrechnung, die den Sprung von Teilaufgabe 2 auf 4 erklärt.

**Freischaltkriterium:** Die SuS erkennen an einem unbekannten Aufgabentext, dass
Sortieren hilft, und können begründen, **wonach** sortiert wird und warum die
Antwort danach lokal ablesbar ist.

**Voraussetzung:** M3. Ohne Laufzeitdenken ist der Sprung von Teilaufgabe 2 auf
Teilaufgabe 4 nicht motivierbar. **M4 wird nicht gebraucht** — wer dort hängt,
kann hier trotzdem weiterarbeiten. Das steht auch auf der Modulseite, damit die
SuS sich selbst einordnen können.

---

## Neu an diesem Modul

**Erstes Modul im neuen Seitenformat.** Das Konzept steht vorne und wird an
kleinen Beispielen erklärt; die SOI-Aufgaben kommen danach auf `uebungen.md`, mit
je drei Hinweisstufen pro Aufgabe statt fünf pro Modul.

Das ändert die Rolle der LP an einer Stelle wesentlich. Im alten Format war die
Hürde, überhaupt auf die Idee zu kommen. Jetzt ist die Hürde eine andere:
**Gelesenes fühlt sich nach Verstandenem an.** Wer die Erklärung zum Sushi
gelesen hat, glaubt, die Aufgabe zu können — und scheitert dann am Einlesen, am
Ausgabeformat oder daran, dass Thermalquellen anders aussieht.

Gegenmittel im Material: Das durchgerechnete Beispiel auf der Konzeptseite ist
bewusst *nicht* die erste Übungsaufgabe, und die Vertiefung nennt das Wort
Sortieren nicht. Gegenmittel im Unterricht: nicht fragen „habt ihr das
verstanden", sondern eine Aufgabe geben.

**Erstes Modul mit Gerüststufe 3.** `vorlage-stufe3.py` liefert nur noch die
Wortliste. Rechne damit, dass hier mehr Zeit draufgeht als am Konzept —
insbesondere bei Thermalquellen, wo die Anzahl Ausgabezeilen pro Testfall
variiert. Das ist gewollt, aber es ist der Punkt, an dem die Klasse
auseinanderläuft.

---

## Vorbereitung

- Sushi Teilaufgabe 2 und 4 selbst lösen. Die Lösung ist kurz; der Zeitaufwand
  steckt im Vertauschungsargument, warum benachbarte Paare optimal sind.
- Thermalquellen Teilaufgabe 1 selbst lösen, **inklusive Ausgabeformat**. Der
  `YES`-Fall mit zwei Zeilen ist die eigentliche Falle der Aufgabe.
- Entscheiden, ob die Hintergrundseite
  [Sortierverfahren](../docs/hintergrund/sortierverfahren.md) im Unterricht
  vorkommt oder als Lektüre bleibt. Sie ist nicht Teil des Kursfadens.

---

## Ablauf-Empfehlung

Drei Lektionen.

**Erste Lektion — Sortieren als Vorverarbeitung.** Einstieg über Sushi
Teilaufgabe 2. Die sechs Preise `16 42 42 42 16 42` an die Tafel und von Hand
paaren lassen, in Partnerarbeit, ohne Vorgabe. Erfahrungsgemäss kommen mehrere
Paarungen zusammen, und der Vergleich der Ergebnisse liefert die Frage von
selbst: Warum ist die eine besser?

Danach den Kernsatz festhalten und Teilaufgabe 2 einreichen lassen.

**Zweite Lektion — die Schranke.** Teilaufgabe 4 bringt zwei Änderungen auf
einmal: Sake kostet Geld, und N wird zehnmal grösser. Beide getrennt behandeln.

Die Laufzeitrechnung eignet sich fürs Plenum: Wer Teilaufgabe 2 mit „immer das
teuerste suchen" gelöst hat, hat eine O(N²)-Lösung, die dort mit 10⁸ Schritten
durchging. Bei Teilaufgabe 4 sind es 10¹⁰. Dieselbe Lösung, dasselbe Programm,
und trotzdem unbrauchbar — das ist M3 in Anwendung.

Guter Moment für den Hinweis, dass diese naive Lösung Selection Sort ist. Wer
mag, geht von dort auf die Hintergrundseite.

**Dritte Lektion — Thermalquellen und das Ausgabeformat.** Die Aufgabe nennt
Sortieren nicht. Die Kernfrage — „was gilt entlang einer gültigen Reihenfolge für
die Temperaturen?" — lohnt sich als stille Einzelarbeit von fünf Minuten, bevor
irgendwer tippt.

Wer die Einsicht hat, ist in zehn Minuten fertig; der Rest der Lektion geht ans
Ausgabeformat. Das ist keine verlorene Zeit — Formatfehler sind der häufigste
Punkteverlust in der Vorrunde überhaupt.

---

## Typische Fehlvorstellungen

**„Sortieren kostet Zeit, also macht es die Lösung langsamer."**
Verbreitet und nachvollziehbar. Gegenrechnung: N log N gegen N². Bei N = 10⁴ sind
das 1,4 · 10⁵ gegen 10⁸ — Sortieren ist nicht der Preis, sondern die Ersparnis.
Die Trockenübung 1 auf der Übungsseite rechnet das durch und zeigt zugleich die
Grenze: Bei einer einzigen Anfrage lohnt es sich tatsächlich nicht.

**„Ich sollte eine Sortierung selbst schreiben können."**
Nein. Die Hintergrundseite beginnt genau deshalb mit einer Warnung. Wer
Bubble Sort einbaut, verschlechtert O(N log N) auf O(N²) und verliert dafür
Punkte.

**„Nach dem Sortieren stimmen meine Indizes noch."**
Der häufigste konkrete Fehler des Moduls, und er fällt bei Thermalquellen erst
auf, wenn die Ausgabe verglichen wird — die Werte sind richtig, die Nummern
falsch. Die ursprüngliche Nummer muss vor dem Sortieren ins Tupel.

**„Bei Thermalquellen muss ich verschiedene Reihenfolgen ausprobieren."**
Der teuerste Irrweg der Aufgabe, weil er direkt zu einem
Backtracking-Ansatz führt, der bei N = 300 nie durchläuft. Die Einsicht ist, dass
es genau einen Kandidaten gibt. Wer hier hängt, bekommt Hinweis 1 und sonst
nichts.

**„`sort()` und `sorted()` sind dasselbe."**
Bis zu dem Moment, in dem jemand die ursprüngliche Reihenfolge noch braucht.
Einmal explizit zeigen.

**„Binäre Suche geht immer, wenn ich etwas suche."**
Nur auf sortierten Daten. Der Fehler ist besonders unangenehm, weil das Programm
nicht abstürzt, sondern still falsche Antworten liefert.

---

## Wenn die Zeit knapp ist

Streichbar sind die beiden Trockenübungen und die Hintergrundseite. Sushi
Teilaufgabe 2 und 4 sind der Kern; Thermalquellen ist die einzige Aufgabe, an
der sich zeigt, ob das Konzept übertragbar sitzt, und sollte deshalb stehen
bleiben.

Bei 15 Lektionen (siehe `KONZEPT.md` Abschnitt 7) wird M5 auf zwei Lektionen
gekürzt: erste Lektion Sushi, zweite Lektion Thermalquellen. Die binäre Suche
fällt dann ganz weg — sie hat ohnehin keine Ankeraufgabe.
