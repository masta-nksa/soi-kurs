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

## Der didaktische Grundsatz

**Konzept zuerst, dann Anwendung.** Die SuS lesen die Erklärung, verstehen sie
an einem kleinen Beispiel und setzen sie danach an einer echten SOI-Aufgabe um.

Das war nicht immer so. Bis M4 lief das Material umgekehrt — erst das Problem,
dann eigene Versuche, dann das Konzept als Entdeckung. Umgestellt wurde aus zwei
Gründen: Der Stoff wächst über das hinaus, was man in einer Lektion entdecken
kann, und die Website soll auch nachschlagbar sein.

Die Umstellung hat einen Preis, und dagegen gibt es zwei feste Regeln (siehe
„Harte Regeln"): Gelesenes fühlt sich nach Verstandenem an. Deshalb ist das
durchgerechnete Beispiel nie die erste Übungsaufgabe, und mindestens eine
Aufgabe pro Modul nennt das Konzept nicht beim Namen.

## Dateien pro Modul

```
docs/mNN-name/
├─ index.md      Lernbaustein — die Konzepte
├─ uebungen.md   die Aufgaben dazu
└─ loesung.md    Musterlösungen
```

Dazu ausserhalb des Kursfadens:

```
docs/hintergrund/  Wie ein Werkzeug innen funktioniert. Optional zu lesen,
                   eigene Menürubrik, kein Modul.
lp/mNN-name.md     LP-Blatt, ausserhalb der Navigation
```

## Seitenstruktur `index.md` — verbindlich

1. **Einstiegskarte** `!!! note "Du kannst hier einsteigen, wenn ..."` — das
   Freischaltkriterium der Voraussetzung, in Du-Form umformuliert. Nennt
   ausdrücklich, welche Module **nicht** nötig sind. Das ist die
   Selbsteinordnung; ohne sie ist die Modulnummer eine Reihenfolge ohne Inhalt.
2. Zeile `**In diesem Modul:**` mit Links auf die Konzeptblöcke
3. Vorspann, zwei bis vier Sätze
4. **Pro Konzept ein `##`-Block** mit genau diesen `###`-Abschnitten, in dieser
   Reihenfolge:
   - `Worum es geht` — der Problemtyp, mit einem kleinen konkreten Beispiel
   - `Die Idee` — Kernsatz als Blockzitat, Analogie samt Bruchstelle
   - `An einem Beispiel` — von Hand durchgerechnet, klein genug zum Nachrechnen
   - `Im Code` — das Muster, minimal
   - `Laufzeit` — Komplexität, Faktor T, Grössenordnung
   - `Woran du es erkennst` — die Signale im Aufgabentext
   - `Typische Fallen`
5. `## Prüfe dich selbst` — 3–4 Fragen, Antworten in `??? success`
6. `## Übungen` — Verweis auf `uebungen.md`
7. `## Weiter zu ...`

**Ein Modul hat ein bis vier Konzeptblöcke**, in der Regel zwei oder drei. Mehr
als vier wird unübersichtlich; dann lieber ein zweites Modul. Die Zahl richtet
sich nach dem Umfang: Ein Modul mit drei Lektionen trägt vier Blöcke, eines mit
zwei selten mehr als zwei.

`Woran du es erkennst` ist der Abschnitt, der die Website nachschlagbar macht.
Er wird nie weggelassen — auch nicht, wenn er kurz ausfällt.

### Techniken und Gewohnheiten

Nicht jedes Konzept ist eine **Technik**, die man an Signalen im Aufgabentext
erkennt. Manche sind **Gewohnheiten**, die immer gelten — modellieren, am
Extremfall prüfen, vor dem Programmieren die Laufzeit schätzen.

Bei Gewohnheiten heisst der Abschnitt `Wann du es brauchst` statt
`Woran du es erkennst`. Er beantwortet eine andere Frage: nicht „woran merke
ich, dass das hier passt", sondern „an welcher Stelle im Ablauf mache ich das,
und woran merke ich, dass ich es übersprungen habe".

Der Test, welcher Fall vorliegt: Wenn die ehrliche Antwort auf „woran erkennst
du es" ein „immer" ist, dann ist es eine Gewohnheit.

### Die sieben Abschnitte sind eine Auswahlliste

Ein Block nimmt die Abschnitte, die zutreffen, **in der vorgegebenen
Reihenfolge**, und erfindet keine neuen.

Immer vorhanden: `Worum es geht`, `Die Idee`, `An einem Beispiel`, und je nach
Typ `Woran du es erkennst` oder `Wann du es brauchst`.

Weglassbar, wenn das Konzept sie nicht hat:

- `Im Code` — bei einer Gewohnheit, die auf Papier stattfindet
- `Laufzeit` — bei allem, was keine hat. Nie „O(1), nichts zu rechnen"
  hinschreiben, nur damit der Abschnitt dasteht.
- `Typische Fallen` — wenn es wirklich keine gibt. Selten.

Ein leerer Pflichtabschnitt ist schlechter als ein fehlender: Er lehrt die SuS,
Überschriften zu überspringen.

## Seitenstruktur `uebungen.md` — verbindlich

1. `!!! note "Du musst nichts nachschlagen"` und ein `!!! tip` zur Gerüststufe
2. **Beschreibung der Ankeraufgabe** mit der Leitertabelle (siehe unten), dem
   Eingabe- und Ausgabeformat
3. Pro Aufgabe: Schranken, Beispiel, Zeitangabe, drei `??? tip`-Hinweise, danach
   ein `!!! success` mit dem Link zum Einreichen
4. Trockenübungen, falls vorhanden
5. Link auf `loesung.md`, ganz am Seitenende

Die Aufgaben werden gestuft und in dieser Reihenfolge angeordnet: **Einstieg**,
**Kern**, **Vertiefung**. Das entspricht den drei Spuren aus `KONZEPT.md`
Abschnitt 5.

## Hinweisleiter — drei Stufen pro Aufgabe

Nicht mehr fünf pro Modul, sondern drei pro Aufgabe:

1. **Perspektivfrage** — „Dreh die Frage um: Was bekommst du geschenkt?"
2. **Beobachtung erzwingen** — kleines Beispiel, von Hand durchspielen
3. **Kernidee benennen** — der Satz, auf den es ankommt

Die früheren Stufen 2 und 5 entfallen: Die Analogie steht jetzt im Konzeptblock
unter `Die Idee`, das Umsetzungsdetail unter `Im Code`.

**Regeln:** nie Code als Hinweis — Hinweise sind Fragen und Beobachtungen. Ein
Hinweis nimmt die nächste Stufe nicht vorweg.

## Ankeraufgabe im Modul

**Leitertabelle in `uebungen.md`**, direkt unter der Aufgabenbeschreibung. Alle
Teilaufgaben der Ankeraufgabe mit Schranke, Punkten und Markierung:
`erledigt in M2`, `**dieses Modul**`, `M4`. Damit sieht man, wo man in der
Aufgabe steht, ohne nachzuschlagen.

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

Kleingeschrieben, Umlaute aufgelöst, Punktzahl am Schluss. **Vor dem Verlinken
auf der Aufgabenseite nachschauen, nicht raten** — die Anker-IDs stehen nicht auf
den Überschriften selbst, sie lassen sich aber im Browser aus dem DOM lesen.
Doppelte Leerschläge in einer Überschrift werden zu *einem* Bindestrich.

**Der Link zum Einreichen steht am Ende der jeweiligen Aufgabe**, in einem
`!!! success`. Nie in der Aufgabenbeschreibung oben — andernfalls liest sich das
Modul als Aufforderung nachzuschlagen.

## Konzepte ohne Ankeraufgabe

Nicht jedes Konzept hat eine passende SOI-Teilaufgabe. Das ist kein Mangel: Die
Konzeptliste richtet sich nach dem, was in den Runden vorkommt, und manches davon
wird abgefragt, ohne dass es eine Aufgabe im zugänglichen Archiv dazu gibt.

Solche Konzepte bekommen direkt unter der `##`-Überschrift:

```markdown
!!! note "Dieses Konzept hat keine Ankeraufgabe"
    In den zugänglichen Runden gibt es dafür keine passende SOI-Teilaufgabe. Es
    steht trotzdem hier, weil ... Die Übungen dazu sind Trockenübungen.
```

**Nie so tun, als gäbe es eine Aufgabe.** Und nie eine Aufgabe erfinden, die
nach SOI aussieht.

## Ausnahme: Werkzeug-Bausteine

M0 und ähnliche Einrichtungs-Module folgen der Seitenstruktur oben **nicht**.
Sie haben kein Konzept im obigen Sinn. Stattdessen:

1. `## Worum es geht`
2. nummerierte `## Schritt N — ...` Abschnitte, jeder mit einem sichtbaren
   Kontrollpunkt („Du bist fertig, wenn …")
3. `## Wenn etwas nicht klappt` — häufige Fehler als `??? tip`
4. `## Weiter zu ...`

## Hintergrundseiten

Eigene Rubrik `docs/hintergrund/`, ausserhalb des Kursfadens. Sie erklären, wie
ein Werkzeug innen funktioniert — nicht, wie man eine Aufgabe löst.

- Beginnen mit einer Warnung, falls das Wissen zum Nachbauen verleitet
  (`sortierverfahren.md` etwa warnt davor, selbst zu sortieren)
- Sagen im ersten Absatz, warum die Seite existiert
- Werden aus den Modulen verlinkt, sind aber nie Voraussetzung
- Dürfen ein `## Prüfe dich selbst` haben, brauchen aber keine Übungen

## Aufklappbares

Nur die Standardtypen von Material verwenden, **keine selbstgebauten Typen**:

- Hinweis: `??? tip "Hinweis 2 — erst selbst versuchen"` (orange)
- Selbstcheck: `??? success "Vergleiche deine Antwort — Frage 1"` (grün)

Die Farbcodierung orange/grün ist Teil der Orientierung und bleibt. Eine neue
Admonition-Art zu erfinden, weil eine Stelle „irgendwie anders" ist, macht das
Material unlesbar — dann lieber den Text ändern.

**Das ist keine Absage an Theming.** Farbpalette, Schrift, Logo und Abstände
dürfen gestaltet werden (siehe `KONZEPT.md` Abschnitt 13, Punkt 8). Verboten ist
nur, die Bedeutung der Standardtypen zu verwässern.

**Musterlösungen kommen nie in ein Aufklappelement**, sondern auf `loesung.md`.
Der Seitenwechsel ist die Hürde — ein Klick auf ein zugeklapptes Element passiert
reflexhaft und zerstört die Aufgabe endgültig.

Auf `uebungen.md` steht der Link zur Lösung **am Seitenende**, nie neben der
Aufgabe. `loesung.md` beginnt mit einer Zeile: „Diese Seite verrät die Lösung.
Hast du es wirklich selbst versucht?"

## Harte Regeln für Inhalte

- **Das durchgerechnete Beispiel im Konzeptblock ist nie die erste
  Übungsaufgabe.** Sonst wird aus Anwenden ein Abschreiben.
- **Mindestens eine Aufgabe pro Modul nennt das Konzept nicht beim Namen.** Die
  eigentliche Prüfungsleistung ist zu erkennen, *welches* Konzept passt — und
  genau das verrät ein Katalog in der Überschrift.
- **Kein Code als Hinweis.** Hinweise sind Fragen und Beobachtungen.
- **Ein Hinweis nimmt die nächste Stufe nicht vorweg.**
- **Jede Analogie nennt ihre Bruchstelle.**
- **Brute Force nie als Notlösung darstellen** — sie gibt in der SOI echte Punkte.
- **`Case #i` ist nullbasiert.** Der erste Testfall ist `Case #0`.
- **Auf soi.ch wird nur die Ausgabedatei hochgeladen**, nie der Quellcode.
  Nach dem Download der Eingabedaten bleiben 5 Minuten.
- Selbstcheck-Fragen sind Anwendung, nicht Reproduktion.

## Aufgaben prüfen, bevor sie ins Material kommen

Die Kuratierungsliste in `lp/kuratierung.md` ist eine Vorauswahl, keine Freigabe.
Vor der Aufnahme einer Aufgabe gilt ausnahmslos:

1. Vollständigen Aufgabentext auf soi.ch lesen, nicht die Zusammenfassung
2. Modell aufstellen und die Musterlösung **gegen alle offiziellen Beispiele**
   laufen lassen
3. Bei gierigen oder konstruktiven Lösungen zusätzlich gegen eine vollständige
   Suche auf Zufallsfällen prüfen — plausibel ist nicht dasselbe wie richtig
4. Den Code, der im Material steht, aus der Markdown-Datei extrahieren und
   ausführen. Nicht eine Nebenfassung testen.

## Python im Material

- Nur Standardbibliothek
- Bezeichner auf Deutsch (`zahl`, `zahlen`, `loese`)
- Gerüststufe pro Modul beachten: M0–M2 `vorlage.py` (fertige Leser), M3–M4
  `vorlage-stufe2.py` (Einlesen eines Testfalls als Lücke), ab M5
  `vorlage-stufe3.py` (nur noch die Wortliste, Parsing und Ausgabe selbst)
- Datenstrukturen kommen dort, wo ein Problem sie erzwingt, nie als eigenes
  Thema. **Sie gehören aber auf die Konzeptseite**, nicht nur in die
  Musterlösung — ein Typ, der nur in `loesung.md` vorkommt, wird von denen nie
  gesehen, die die Aufgabe selbst lösen.

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
  geschrieben. Diese Zeile in Gerüststufe 1 und 2 immer mitliefern, in Stufe 3
  schreiben die SuS sie selbst.
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
- **Tupel und `.join()` sind erlaubt** — beides ab M5 nötig, beides bei der
  ersten Verwendung mit einem Satz erklären

## Externe Links

Links auf fremde Seiten öffnen immer in einem neuen Tab. Das erledigt der Hook
`hooks/externe_links.py` beim Bauen automatisch für jede Adresse mit `http://`
oder `https://` — im Markdown ist nichts zu tun.

## Umfang

**Ausbaustufe 1** (Vorrunde und Erste Runde) ist das, was gebaut wird: M0 bis M7
plus Strang B. Die Modulliste steht in `KONZEPT.md` Abschnitt 7.

**Ausbaustufe 2** (Zweite Runde) — Graphen, dynamische Programmierung, Rekursion,
fortgeschrittene Datenstrukturen, Geometrie — ist geplant, aber **nicht zu
bauen, solange Ausbaustufe 1 offen ist**. Auch nicht anzukündigen.

C++ kommt gar nicht vor.

## Aufgaben

Ankeraufgaben kommen ausschliesslich von soi.ch (Vorrunde und Archiv). Eigene
Aufgaben nur als Trockenübung oder lokale Mini-Aufgabe mit mitgelieferten
Testdateien. Keine Verlinkung auf externe Plattformen.

## Arbeitsweise

Ein Modul pro Durchgang. Nach jedem Modul stoppen und zur Durchsicht vorlegen,
nicht mehrere Module am Stück generieren.

Vor dem Vorlegen prüfen: Musterlösungen laufen lassen (aus der Markdown-Datei
extrahiert), interne Links und Anker prüfen, `mkdocs.yml` ergänzen, und

```
python -m mkdocs build --strict
```

MkDocs ist lokal installiert. Zum Anschauen `python -m mkdocs serve`, die Seite
liegt dann unter `http://localhost:8000/soi-kurs/` — der Pfad gehört dazu, weil
`site_url` ihn enthält. **Der Dateiwächter greift im OneDrive-Ordner nicht
zuverlässig**: nach Änderungen den Server neu starten.

## Veröffentlichen

Jeder Push auf `main` veröffentlicht die Seite über
`.github/workflows/deploy.yml`. Ein Lauf dauert rund fünf Minuten, das Ergebnis
steht auf <https://masta-nksa.github.io/soi-kurs/>.

Von Hand anstossen: `gh workflow run deploy.yml --ref main`.

**Wenn ein Lauf „queued" bleibt, ohne dass ein Job erscheint**, liegt es fast
sicher an der Concurrency-Gruppe `pages`: Ein älterer hängender Lauf blockiert
alle folgenden, weil `cancel-in-progress: false` gesetzt ist. Den alten Lauf
suchen und abbrechen — Diagnosebefehl in `KONZEPT.md` Abschnitt 13, Punkt 10.
