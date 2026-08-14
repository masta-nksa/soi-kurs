# Baukonventionen — SOI-Vorbereitungskurs

Das inhaltliche Konzept steht in `KONZEPT.md`. Diese Datei enthält nur die
Regeln für die Umsetzung. Bei Widerspruch gilt `KONZEPT.md`.

## Kontext in einem Satz

Lernmaterial für Schweizer Gymnasiastinnen und Gymnasiasten zur Vorbereitung auf
Vorrunde und Erste Runde der Informatik-Olympiade. Python, VS Code, statische
Website auf GitHub Pages.

## Sprache und Ton

- Alles auf Deutsch, Schweizer Rechtschreibung (**ss statt ß**)
- Anrede: Du
- Kurze Sätze. Fachbegriffe werden bei erster Verwendung erklärt.
- Keine Emojis im Lernmaterial

## Dateien pro Modul

```
docs/mNN-name/
├─ index.md      Lernbaustein
├─ uebungen.md   Variation, Verschärfung, Verkleidung
└─ loesung.md    Musterlösungen
```

## Seitenstruktur — verbindlich

`index.md` folgt genau dieser Reihenfolge:

1. `## Das Problem` — offen
2. `## Probier es selbst` — offen, mit Zeitangabe; ein `??? tip`
   „Kommst du nicht weiter?"
3. `## Hinweise` — fünf `??? tip`, Stufen laut `KONZEPT.md` Abschnitt 4
4. `## Das Konzept` — offen; Kernsatz, Invariante, Laufzeit, Analogie entfaltet
   samt Bruchstelle
5. `## Prüfe dich selbst` — 3–4 Fragen, Antworten in `??? success`
6. `## Übungen` — Verweis auf `uebungen.md`
7. `## Weiter zu ...`

## Ankeraufgabe im Modul

Jedes Modul hängt an einer SOI-Aufgabe. Drei Regeln, entstanden beim Bau von M1
bis M4:

**Leitertabelle in `## Das Problem`.** Alle Teilaufgaben der Ankeraufgabe mit
Schranke, Punkten und Markierung: `erledigt in M2`, `**dieses Modul**`, `M4`.
Damit sieht man, wo man in der Aufgabe steht, ohne nachzuschlagen.

Künftige Teilaufgaben stehen als Zeile da, **ihr Inhalt aber nicht** — statt der
Schranke dort „mit einer zusätzlichen Regel". Sonst nimmt die Tabelle die
Entdeckung eines späteren Moduls vorweg.

**Aufgaben-Links tragen den Anker ihrer Teilaufgabe.** Jede Aufgaben-URL auf
soi.ch liefert dieselbe Seite mit *allen* Aufgaben der Runde; ohne Anker landet
man ganz oben und scrollt an bereits gelösten Teilaufgaben vorbei. Die Anker
sehen so aus:

```
https://soi.ch/contests/2025/preround/endurance/#teilaufgabe-4-strasse-flicken-20-punkte
```

Kleingeschrieben, Umlaute aufgelöst, Punktzahl am Schluss. Vor dem Verlinken auf
der Aufgabenseite nachschauen, nicht raten.

**Der Link zum Einreichen steht am Ende von `## Probier es selbst`**, nicht in
`## Das Problem`. Oben stehen nur der Aufgabenname und ein `!!! note`, dass alles
Nötige auf der Kursseite steht. Andernfalls liest sich das Modul als
Aufforderung nachzuschlagen — und widerspricht M0, wo der Download ans Ende der
Lektion gehört.

## Ausnahme: Werkzeug-Bausteine

M0 und ähnliche Einrichtungs-Module folgen der Seitenstruktur oben **nicht**.
Sie haben kein Problem zum Selbstlösen, keine Hinweisstufen und keine Analogie.
Stattdessen:

1. `## Worum es geht`
2. nummerierte `## Schritt N — ...` Abschnitte, jeder mit einem sichtbaren
   Kontrollpunkt („Du bist fertig, wenn …")
3. `## Wenn etwas nicht klappt` — häufige Fehler als `??? tip`
4. `## Weiter zu ...`

Der didaktische Zyklus gilt hier nicht — Werkzeuge entdeckt man nicht, man
richtet sie ein.

## Aufklappbares

Nur die Standardtypen von Material verwenden, **kein eigenes CSS**:

- Hinweis: `??? tip "Hinweis 2 — erst selbst versuchen"` (orange)
- Selbstcheck: `??? success "Vergleiche deine Antwort"` (grün)

**Musterlösungen kommen nie in ein Aufklappelement**, sondern auf `loesung.md`.
Der Seitenwechsel ist die Hürde — ein Klick auf ein zugeklapptes Element passiert
reflexhaft und zerstört die Aufgabe endgültig.

Auf `uebungen.md` steht der Link zur Lösung **am Seitenende**, nie neben der
Aufgabe. `loesung.md` beginnt mit einer Zeile: „Diese Seite verrät die Lösung.
Hast du es wirklich selbst versucht?"

## Harte Regeln für Inhalte

- **Kein Code als Hinweis.** Hinweise sind Fragen und Beobachtungen.
- **Ein Hinweis nimmt die nächste Stufe nicht vorweg.**
- **Die Analogie steht auf Hinweisstufe 2**, nie am Seitenanfang.
- **Jede Analogie nennt ihre Bruchstelle.**
- **Brute Force nie als Notlösung darstellen** — sie gibt in der SOI echte Punkte.
- **`Case #i` ist nullbasiert.** Der erste Testfall ist `Case #0`.
- **Auf soi.ch wird nur die Ausgabedatei hochgeladen**, nie der Quellcode.
  Nach dem Download der Eingabedaten bleiben 5 Minuten.
- Selbstcheck-Fragen sind Anwendung, nicht Reproduktion.

## Python im Material

- Nur Standardbibliothek
- Bezeichner auf Deutsch (`zahl`, `zahlen`, `loese`)
- Gerüststufe pro Modul beachten: M0–M2 `vorlage.py` (fertige Leser), M3–M4
  `vorlage-stufe2.py` (Einlesen eines Testfalls als Lücke), ab M5 nur noch das
  Grundgerüst
- Datenstrukturen kommen dort, wo ein Problem sie erzwingt, nie als eigenes
  Thema. `set` wird deshalb erst in M3 eingeführt, weil dort `if x in liste` zu
  langsam wird.

### Laufzeit über Komplexität, nie über Messwerte

- Immer über O(N), O(N²) rechnen und in **Grössenordnungen** antworten —
  „Sekundenbruchteil", „Sekunden", „Minuten", „Tage". Nie gemessene
  Sekundenwerte ins Material schreiben: Sie hängen vom Gerät ab und täuschen
  eine Genauigkeit vor, die die Rechnung nicht hergibt.
- Faustregel: rund **10⁷ Schritte pro Sekunde** in Python, nie die C++-Zahlen.
- **Der Faktor T gehört in jede Rechnung.** Fast alle SOI-Aufgaben haben T = 100
  Testfälle — der am häufigsten vergessene Faktor 100.
- **Vereinfachungen werden als solche benannt.** Dass jeder Schritt gleich teuer
  sei, stimmt nicht; Geräte unterscheiden sich; grosse Listen werden langsamer.
  Zusammen leicht eine Grössenordnung. Die Näherung trägt trotzdem, weil die
  Unterschiede, um die es geht, Faktoren von tausend und mehr sind.
- Unser Zeitbudget sind die **fünf Minuten** zwischen Download und Upload, nicht
  ein Grader-Zeitlimit. Kleine Unterschiede sind deshalb egal, grosse tödlich.
- Gemessen wird nur, um den **Faktor beim Verdoppeln** zu zeigen (die Signatur
  der Komplexität), nie um Sekunden vorherzusagen.

### Start über den Play-Knopf, nicht über die Konsole

Die SuS starten ihr Programm mit dem Play-Knopf in VS Code. Daraus folgt:

- **Keine Umleitung mit `<` und `>`.** Ein- und Ausgabedatei stehen als
  Konstanten im Kopf der Datei (`EINGABE`, `AUSGABE`) und liegen im
  Aufgabenordner.
- Einlesen mit `open(EINGABE)`, nie `sys.stdin` und nie `input()`
- Die Ergebniszeilen werden gesammelt und am Schluss über `pruefe.schreibe`
  geschrieben. Diese Zeile in Gerüststufe 1 und 2 immer mitliefern.
- `print` ist damit frei für Debug-Ausgaben — im Material auch so benennen.
- Nie behaupten, `print` schreibe das Ergebnis.

### Keine Kurzformen

Die SuS bringen sehr unterschiedliche Programmiererfahrung mit. Code im Material
verwendet nur Konstrukte, die auch in einem ersten Kurs vorkommen:

- Keine List Comprehensions — `for`-Schleife mit `append`
- Keine einzeiligen `if/else`-Ausdrücke — normales `if/else`
- Keine f-Strings — `"Case #" + str(i) + ": " + str(ergebnis)`
- Kein `_` als Wegwerf-Variable
- `+=` ist in Ordnung, ebenso `with open(...)`

## Externe Links

Links auf fremde Seiten öffnen immer in einem neuen Tab. Das erledigt der Hook
`hooks/externe_links.py` beim Bauen automatisch für jede Adresse mit `http://`
oder `https://` — im Markdown ist nichts zu tun.

## Nicht bauen

Graphen, dynamische Programmierung, fortgeschrittene Datenstrukturen, C++.
Das ist Zweitrunden-Stoff und wird von der ETH abgedeckt.

## Aufgaben

Ankeraufgaben kommen ausschliesslich von soi.ch (Vorrunde und Archiv). Eigene
Aufgaben nur als Trockenübung oder lokale Mini-Aufgabe mit mitgelieferten
Testdateien. Keine Verlinkung auf externe Plattformen.

## Arbeitsweise

Ein Modul pro Durchgang. Nach jedem Modul stoppen und zur Durchsicht vorlegen,
nicht mehrere Module am Stück generieren.
