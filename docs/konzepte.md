# Konzepte von A bis Z

Diese Seite ist zum Nachschlagen. Wenn du mitten in einer Aufgabe steckst und
ein Werkzeug suchst, findest du es hier — ohne den Kurs von vorne durchzuarbeiten.

Wenn du den Kurs **lernen** willst statt nachzuschlagen, fang beim
[Lernpfad](lernpfad.md) an.

---

## Ich suche etwas für ...

**... einen Aufgabentext, den ich nicht in ein Programm übersetzt kriege**

- [Vom Text zum Modell](m01-problemanalyse/index.md#vom-text-zum-modell) — was ist
  gegeben, was gesucht, welche Beziehung verbindet beides
- [Die Probe am Extremfall](m01-problemanalyse/index.md#die-probe-am-extremfall) —
  das Modell prüfen, bevor eine Zeile Code steht

**... eine Aufgabe, für die es keine Formel gibt**

- [Vollständige Suche](m02-vollstaendige-suche/index.md#vollstandige-suche) — alle
  Möglichkeiten aufzählen und die beste behalten
- [Die Invariante](m02-vollstaendige-suche/index.md#die-invariante) — dem Ergebnis
  einer Schleife trauen können

**... ein Programm, das zu langsam ist**

- [Komplexität und Faktor T](m03-laufzeitdenken/index.md#komplexitat-und-faktor-t) —
  ausrechnen, ob es überhaupt durchläuft
- [Versteckte Schleifen](m03-laufzeitdenken/index.md#versteckte-schleifen) —
  wenn eine kurze Zeile teuer ist
- [Weitergeben statt neu berechnen](m03-laufzeitdenken/index.md#weitergeben-statt-neu-berechnen) —
  aus O(N²) einen einzigen Durchgang machen

**... eine Frage, die sehr oft gestellt wird**

- [Präfixsummen](m04-lineare-techniken/index.md#prafixsummen) — Summen und
  Anzahlen über Bereiche, jede in einem Schritt
- [Mengen und Wörterbücher](m03-laufzeitdenken/index.md#mengen-und-worterbucher) —
  „habe ich das schon gesehen?" in einem Schritt
- [Binäre Suche](m05-sortieren-und-suchen/index.md#binare-suche) — in sortierten
  Daten nachschlagen

**... den längsten oder kürzesten Abschnitt mit einer Eigenschaft**

- [Zweizeiger und Fenster](m04-lineare-techniken/index.md#zweizeiger-und-fenster) —
  ein Fenster, dessen linkes Ende nie zurückgeht

**... eine Aufgabe, bei der die Reihenfolge der Eingabe egal ist**

- [Sortieren als Vorverarbeitung](m05-sortieren-und-suchen/index.md#sortieren-als-vorverarbeitung) —
  umordnen, damit jede Entscheidung lokal wird

**... die Frage, ob ich schon einreichen soll**

- [Teilpunkte mitnehmen](m02-vollstaendige-suche/index.md#teilpunkte-mitnehmen) —
  jede Teilaufgabe zählt einzeln

---

## Alle Konzepte alphabetisch

| Konzept | Modul | Woran du es erkennst |
|---|---|---|
| [Binäre Suche](m05-sortieren-und-suchen/index.md#binare-suche) | M5 | sortierte Daten, viele Anfragen — oder eine Antwort, die sich raten und prüfen lässt |
| [Die Invariante](m02-vollstaendige-suche/index.md#die-invariante) | M2 | eine Schleife, deren Ergebnis du nicht von Hand nachrechnen kannst |
| [Die Probe am Extremfall](m01-problemanalyse/index.md#die-probe-am-extremfall) | M1 | immer, direkt nach dem Modellieren |
| [Komplexität und Faktor T](m03-laufzeitdenken/index.md#komplexitat-und-faktor-t) | M3 | immer, vor der ersten Zeile Code |
| [Mengen und Wörterbücher](m03-laufzeitdenken/index.md#mengen-und-worterbucher) | M3 | `in` auf einer Liste, die mitwächst; Fragen nach verschiedenen oder doppelten Werten |
| [Präfixsummen](m04-lineare-techniken/index.md#prafixsummen) | M4 | viele Fragen nach Summen oder Anzahlen über Bereiche |
| [Prüfen statt Rechnen](m01-problemanalyse/index.md#prufen-statt-rechnen) | M1 | die Aufgabe gibt einen Wert und fragt, ob er stimmt |
| [Sortieren als Vorverarbeitung](m05-sortieren-und-suchen/index.md#sortieren-als-vorverarbeitung) | M5 | die Reihenfolge der Eingabe ist egal; du suchst wiederholt Grösstes oder Kleinstes |
| [Teilpunkte mitnehmen](m02-vollstaendige-suche/index.md#teilpunkte-mitnehmen) | M2 | sobald irgendeine Teilaufgabe läuft |
| [Versteckte Schleifen](m03-laufzeitdenken/index.md#versteckte-schleifen) | M3 | O(N) gerechnet, aber viel langsamer als erwartet |
| [Vollständige Suche](m02-vollstaendige-suche/index.md#vollstandige-suche) | M2 | kleine Schranken; Frage nach dem Besten ohne Formel |
| [Vom Text zum Modell](m01-problemanalyse/index.md#vom-text-zum-modell) | M1 | immer, vor der ersten Zeile Code |
| [Weitergeben statt neu berechnen](m03-laufzeitdenken/index.md#weitergeben-statt-neu-berechnen) | M3 | zwei verschachtelte Schleifen, die fast dasselbe rechnen |
| [Zweizeiger und Fenster](m04-lineare-techniken/index.md#zweizeiger-und-fenster) | M4 | längster oder kürzester Abschnitt mit einer monotonen Bedingung |

---

## Werkzeuge und Hintergrund

Kein Konzept zum Lösen von Aufgaben, aber gut zu wissen.

| Seite | Inhalt |
|---|---|
| [M0 — Werkzeugkasten](m00-werkzeugkasten/index.md) | VS Code, Play-Knopf, Ein- und Ausgabedatei, die 5-Minuten-Regel |
| [Sortierverfahren](hintergrund/sortierverfahren.md) | wie Bubble, Insertion, Merge, Quick und Timsort innen funktionieren |

---

## Noch nicht gebaut

Diese Konzepte gehören in den Kurs, es gibt sie aber noch nicht:

- **Zeichenketten, zweidimensionale Felder, Nachbarschaft im Gitter** — M6
- **Gierige Verfahren, Zustandsdenken** — M7
- **Abläufe von Hand durchspielen, Quiz-Strategie** — Strang B

Was danach kommt — Graphen, dynamische Programmierung, kürzeste Wege — ist Stoff
der Zweiten Runde und ausdrücklich nicht Teil dieses Kurses.
