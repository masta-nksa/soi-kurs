# SOI-Vorbereitungskurs — Konzept

Stand: 23. August 2026

Dieses Dokument hält den Stand der Konzeptarbeit fest. Es ist die Grundlage für
die weitere Ausarbeitung der einzelnen Module und für die technische Umsetzung.

---

## 1. Zielsetzung und Abgrenzung

Vorbereitungskurs für die Schweizer Informatik-Olympiade (SOI). Die
grundlegenden Informatikkonzepte werden **theoretisch an konkreten Beispielen
erklärt** und danach an echten SOI-Aufgaben aus vergangenen Runden angewendet.

Der Kurs ist zugleich ein **Nachschlagewerk**: Wer mitten in einer Aufgabe
steckt und ein Werkzeug sucht, soll die passende Seite finden, ohne den Kurs von
vorne durchzuarbeiten. Deshalb hat jedes Konzept eine eigene, verlinkbare Stelle
und einen Abschnitt „Woran du es erkennst".

### Zwei Ausbaustufen

**Ausbaustufe 1 — Vorrunde und Erste Runde.** Das ist der aktuelle Auftrag.
Alle Konzepte, die in diesen beiden Runden vorkommen, werden theoretisch und
praktisch eingeführt. Modulliste in Abschnitt 7.

**Ausbaustufe 2 — Zweite Runde.** Graphen, Tiefen- und Breitensuche, kürzeste
Wege, Bäume, dynamische Programmierung, Union-Find, Prioritätswarteschlange,
Bitmasken, Rekursion und Backtracking, Geometrie. Rund zehn bis zwölf Konzepte,
also nochmals die Grösse von Ausbaustufe 1.

Ausbaustufe 2 ist geplant, aber **nicht zu bauen, solange Ausbaustufe 1 offen
ist** — und nicht anzukündigen. Wer heute anfängt, soll nicht auf eine Seite mit
dreissig Konzepten schauen und nicht wissen, wo er beginnt.

**Warum Runde 2 überhaupt dazukommt.** Die frühere Fassung dieses Dokuments hat
Graphen und DP mit dem Argument gestrichen, die ETH decke die Zweite Runde in
eigenen Workshops ab. Für einen *Kurs* gilt das weiterhin. Für ein
*Nachschlagewerk* nicht: Graphen sind in `lp/kuratierung.md` bei 10 von 55
gesichteten Aufgaben der Ausschlussgrund — der mit Abstand grösste ausgelassene
Block. Ein Werk, das Vollständigkeit beansprucht, kann ihn nicht weglassen.

**C++ kommt nicht vor**, in keiner Ausbaustufe.

---

## 2. Faktenlage SOI

### Rundenstruktur (seit 2025 geändert — Begriffe sind irreführend)

| Ebene | Was es ist | Rolle im Kurs |
|---|---|---|
| **Vorrunde / Pre-Round** | 5 Aufgaben, ganzjährig geöffnet, freie Sprache, Grader | Ziel + Ankeraufgaben |
| **Erste Runde** (neu seit 2025) | Online-Quiz ca. 35–40 Min, Multiple Choice, keine Programmierkenntnisse nötig, für den Einsatz im Klassenverband gedacht | Ziel |
| **Zweite Runde** | 5 Aufgaben, Okt–Nov, Kategorien junior / regular | ausserhalb des Kurses |

Die alten Runden hiessen anders: Was heute „Zweite Runde" ist, hiess früher
„Erste Runde" (z. B. „First Round SOI 2018"). Beim Sichten des Archivs beachten.

### Aufgaben der aktuellen Vorrunde

`addition`, `books`, `cheeseparty`, `directions`, `endurance`

Niveau von „zwei Zahlen addieren" bis Sliding Window (`endurance` Subtask 5:
längster Abschnitt mit höchstens K reparierten Löchern, N ≤ 10⁵).

### Subtask-Leiter als didaktisches Rückgrat

SOI-Aufgaben haben eingebaute Didaktik. `endurance` etwa:

| Subtask | Schranke | Was erzwungen wird |
|---|---|---|
| ST1 | N = 3 | jede Lösung, auch Fallunterscheidung von Hand |
| ST2 | N ≤ 100 | O(N²)/O(N³) reicht |
| ST3 | N ≤ 10⁵ | erzwingt O(N) |
| ST4 | K Löcher reparierbar, N ≤ 100 | neue Variante, wieder Brute Force |
| ST5 | N ≤ 10⁵, K ≤ 100 | erzwingt Zweizeiger |

Das ist exakt das didaktische Muster in Aufgabenform. Die Subtask-Leiter trägt
gleichzeitig die Binnendifferenzierung (siehe Abschnitt 5).

### Einreichung und Grader

- Nur C++ kann direkt auf der Website eingereicht werden. Für alle anderen
  Sprachen gilt: **„Eingabedaten herunterladen"** erzeugt eine `input.txt` mit
  den Testfällen. Diese lokal durch das eigene Programm laufen lassen und die
  **Ausgabedatei** hochladen. Der Quellcode wird nicht hochgeladen. Das ist
  unser Weg.
- **Nach dem Download bleiben 5 Minuten für den Upload.** Danach muss eine neue
  Eingabedatei erzeugt werden — jeder Download liefert frische Testfälle.
- Alte Runden bleiben dauerhaft „upsolvable" — derselbe Workflow.
- `Case #i:` ist **nullbasiert**. Der erste Testfall ist `Case #0`.
- SOI hat eine eigene Hilfeseite zu Zeilenumbruch-Problemen — das Ausgabeformat
  ist die grössere Fehlerquelle als das Einlesen.

### Zu prüfen

- Genaue Daten der Ersten Runde 2026/27 auf soi.ch (Drittquelle nannte
  1.–25. September 2026, also sehr bald — für dieses Jahr wäre nur Strang B
  realistisch, der volle Kurs zielt auf 2027/28)
- Ob Sammel-Logins für eine Klasse möglich sind (LP regelt das mit den SuS)

---

## 3. Rahmenbedingungen

| | |
|---|---|
| **Sprache** | Python |
| **Umgebung** | VS Code |
| **Prüfung** | manueller Datei-Upload auf soi.ch |
| **Externe Plattformen** | keine — der Kurs ist in sich geschlossen |
| **Zeitbudget** | 15–25 Lektionen |
| **Takt** | keiner — Material ohne festen Rhythmus |
| **Einstiegsniveau** | gemischt, adaptives Vorgehen nötig |
| **Format** | primär begleiteter Kurs mit LP; zusätzlich solo nutzbar, falls LP verhindert |
| **Hosting** | GitHub Pages |

### Konsequenz aus „ohne festen Takt"

Die Einheit ist nicht die Doppellektion, sondern der **Lernbaustein**: in sich
abgeschlossen, ca. 45–90 Minuten, mit expliziten Vorbedingungen. Statt einer
linearen Liste braucht das Material einen Abhängigkeitsgraphen.

Pro Baustein zwei Zusatzmarkierungen:

- **Freischaltkriterium** — was gekonnt sein muss, nicht was abgesessen wurde
- **LP-Wert (hoch/mittel/niedrig)** — Bausteine, deren Kern die Diskussion ist,
  werden anders markiert als solche, die solo gut funktionieren. Bei Ausfall der
  LP weiss man, welche vorzuziehen sind.

### Konsequenz aus „mit und ohne LP"

Das Hinweissystem muss **ausformuliert im Material stehen**, nicht im Kopf der
Lehrperson. Die LP wird dadurch nicht überflüssig, sondern wechselt die Rolle:

| | Material trägt | Lehrperson trägt |
|---|---|---|
| **Mit LP** | Aufgaben, Hinweisstufen, Lösungen | Diagnose, Tempo, Diskussion |
| **Ohne LP** | alles davon + Selbstkontrolle | ersetzt durch Selbstcheck-Fragen |

---

## 4. Didaktisches Muster

Pro Konzept:

> Erklärung am kleinen Beispiel → verstanden → Anwendung an einer SOI-Aufgabe →
> Transfer auf eine Aufgabe, die das Konzept nicht beim Namen nennt

### Warum nicht mehr die Entdeckung zuerst

Bis M4 lief das Material umgekehrt: Problem → eigene Versuche → fünf
Hinweisstufen → Konzept als Entdeckung. Das war gut für den Zweizeiger, den man
in 35 Minuten wirklich finden kann. Umgestellt wurde aus drei Gründen:

- **Der Stoff wächst über das Entdeckbare hinaus.** Dynamische Programmierung,
  Dijkstra oder Union-Find findet niemand in einer Lektion. Spätestens in
  Ausbaustufe 2 bricht das Entdeckungsmodell nicht aus didaktischer Mode,
  sondern weil der Stoff es nicht hergibt.
- **Eine Entdeckungsseite ist nicht nachschlagbar.** Wer mitten in der Vorrunde
  denkt „hier müsste man sortieren", braucht eine Seite, die das kurz und
  vollständig sagt.
- **Konzepte fielen durch die Maschen.** Wenn die Ankeraufgabe bestimmt, was
  drankommt, fehlt alles, was keine Aufgabe erzwungen hat. Belegbarer Fall:
  `set` wurde bis August 2026 ausschliesslich auf einer Lösungsseite in M3
  eingeführt — wer die Übung selbst löste, erfuhr nie, dass es den Typ gibt.

### Der Preis und die zwei Gegenmittel

Gelesenes fühlt sich nach Verstandenem an. Wer die Erklärung durchgelesen hat,
glaubt die Aufgabe zu können und scheitert dann am Einlesen oder daran, dass die
nächste Aufgabe anders aussieht. Dagegen zwei feste Regeln:

1. **Das durchgerechnete Beispiel im Konzeptblock ist nie die erste
   Übungsaufgabe.**
2. **Mindestens eine Aufgabe pro Modul nennt das Konzept nicht beim Namen.** Die
   eigentliche Prüfungsleistung ist zu erkennen, *welches* Konzept passt — und
   genau diesen Hinweis verrät ein Katalog schon in der Überschrift.

Sobald mehrere Module umgestellt sind, kommt als drittes Gegenmittel eine Seite
**gemischte Aufgaben ohne Konzeptangabe** dazu. Sie ist der Gegenpol zur
Nachschlagefunktion und billig zu bauen, ergibt aber erst ab etwa vier Konzepten
Sinn.

### Hinweisleiter — drei Stufen, pro Aufgabe

Die Hinweise sind geblieben, aber sie führen nicht mehr zum Konzept, sondern
helfen beim Anwenden. Sie hängen deshalb an der einzelnen Aufgabe, nicht am
Modul:

1. **Perspektivfrage** — „Dreh die Frage um: Was bekommst du geschenkt?"
2. **Beobachtung erzwingen** — kleines Beispiel, von Hand durchspielen
3. **Kernidee benennen** — der Satz, auf den es ankommt

Die früheren Stufen 2 und 5 entfallen: Die Alltagsanalogie steht jetzt im
Konzeptblock unter `Die Idee`, das Umsetzungsdetail unter `Im Code`.

**Regeln:** nie Code als Hinweis; ein Hinweis nimmt die nächste Stufe nicht
vorweg.

### Beispiel-Durchlauf (Sortieren, Modul 5)

Konzeptblock „Sortieren als Vorverarbeitung": Kernsatz, Kartenblatt-Analogie
samt Bruchstelle, sechs Sushi-Preise von Hand gepaart, `sort()` im Code,
O(N log N) mit Faktor T, fünf Erkennungssignale, vier Fallen → `sushi` ST2
anwenden (30 Punkte) → `sushi` ST4 als Verschärfung, wo O(N²) kippt (50 Punkte)
→ `Thermalquellen` ST1 als Transfer, wo das Wort Sortieren nicht vorkommt.

---

## 5. Adaptivität: drei Spuren, keine Gruppentrennung

Alle arbeiten am **selben Problem**, aber unterschiedlich tief. Keine A-/B-Gruppen,
keine „Zusatzblätter für die Schnellen" — das erzeugt Stigma und doppelte
Materialpflege.

| Spur | Umfang |
|---|---|
| **Einstieg** | Subtask 1–2 (kleine Schranken, Brute Force ist erlaubt und *richtig*) |
| **Kern** | Subtask 3–4, das eigentliche Konzept |
| **Vertiefung** | Subtask 5 + eine Verkleidungsaufgabe, oder Laufzeitbeweis / Gegenbeispielsuche |

Diese drei Wörter sind zugleich die **Zwischenüberschriften auf `uebungen.md`**.
Die Spur ist damit nicht etwas, das die LP zuteilt, sondern etwas, das man auf
der Seite sieht und selbst wählt.

**Wichtig:** Brute Force in der Einstiegsspur darf nicht als „Notlösung" markiert
sein. In der SOI-Wertung gibt sie echte Punkte.

Für die Einstiegsheterogenität zusätzlich ein **Selbsttest vor Modul 0**: Wer
`books` (Summe von N Zahlen einlesen) sicher löst, springt direkt zu Modul 1.

---

## 6. Aufgabenarchitektur

### Drei Schichten

| Schicht | Quelle | Feedback | Rolle |
|---|---|---|---|
| **Grader-Aufgaben** | Vorrunde + Archiv auf soi.ch | automatisch, Teilpunkte | Anker & Transfer |
| **Trockenübungen** | selbst erstellt | Selbstcheck / LP | Konzeptbildung |
| **Lokale Mini-Aufgaben** | selbst erstellt, mit Testdateien + `pruefe.py` | lokal | Lückenfüller |

Die Trockenübungen sind kein Notbehelf, sondern tragen das didaktische Muster:
Laufzeit schätzen, Algorithmus von Hand auf einem Mini-Beispiel ausführen,
Invariante formulieren, Gegenbeispiel zu einer Strategie finden. Genau diese
Schritte fallen weg, wenn man nur einreicht und auf grün wartet.

### Das Erntemodell

Eigene Aufgaben können nicht bewertet werden — der Grader kennt nur SOI-Aufgaben.
Wir kuratieren also vorhandene Aufgaben.

Die Vorrunde deckt Modul 0–4 gut ab. Darüber hinaus **ernten wir die ersten
Subtasks alter Runden**: pro archivierter Runde etwa 8–12 verwertbare
Subtask-Einheiten. Drei bis vier gesichtete Runden reichen für den ganzen Kurs.

Stichprobe Runde 2018:

| Aufgabe | brauchbar | Niveau |
|---|---|---|
| `wagashi` ST1 | ja | Array einlesen, Σ aᵢ·cᵢ — Einstieg |
| `sushi` ST1, ST3 | ja | N = 2, Minimum zweier Optionen |
| `sushi` ST2, ST4 | ja | Sortieren als Werkzeug — Kernspur |
| `mahjong` ST1 | ja | konstruktives Verfahren, keine Theorie nötig |
| `cheesepatrol` | nein | Graphen |
| `hanabi` | nein | kürzeste Wege + DP |
| `samurai` | nein | interaktiv, Spielstrategie |

Manche Subtasks sind reine **Theorieaufgaben** („beschreibe deine Lösungsidee und
begründe die Korrektheit", ohne Code) — direkt verwendbar für Strang B.

**Die Stichprobe oben ist inzwischen überholt.** Die vollständige Sichtung von
sieben Runden mit 55 Aufgaben, Bewertung A bis D und Zuordnung zu den Modulen
steht in `lp/kuratierung.md`. Dort auch die drei Befunde, die für jede Auswahl
gelten: der Faktor T = 100, dass `marathon` (2020) dieselbe Aufgabe ist wie
`endurance`, und dass sechs Theorie-Teilaufgaben für Strang B bereitstehen.

### Aufgabenrollen

Jede Konzepteinheit braucht alle vier:

- **Anker** — das Problem, an dem das Konzept entsteht
- **Variation** — gleiche Struktur, andere Einkleidung
- **Verschärfung** — dasselbe Problem, aber die bestehende Lösung muss besser
  oder vollständiger werden
- **Verkleidung** — Konzept nötig, aber nicht sichtbar (echter Transfer)

Plus zwei Sondertypen: **Laufzeit-Schätzaufgaben** und **Widerlegungsaufgaben**.

#### Die drei Achsen der Verschärfung

SOI verschärft nicht nur über Schranken. Im Archiv sind drei Achsen belegt:

| Achse | Was sie erzwingt | Beispiele |
|---|---|---|
| **Höhere Schranke** | bessere Komplexität | `endurance` ST2→ST3, `Gipfel` ST2→ST3 |
| **Spezialfall → allgemeiner Fall** | vollständigeres Modell | `directions` ST1/2→ST3, `sushi` ST1→ST3, `Stickers` K=1→K beliebig |
| **Zusätzliche Regel** | erweitertes Modell | `endurance` ST3→ST4 (K Löcher reparierbar), `cheeseparty` ST1→ST2 |

Die Abgrenzung zur Variation bleibt scharf: Bei der Verschärfung ist es **dasselbe
Problem**, deine Lösung muss wachsen. Bei der Variation ist es ein anderes Problem
mit gleicher Struktur.

**Die Schranken-Achse steht erst ab M3 zur Verfügung.** Bei T = 100 läuft
vollständige Suche in Python bis etwa N = 100 bequem. Die nächste Sprosse einer
SOI-Leiter liegt fast immer bei N ≤ 1000 oder darüber und verlangt damit gleich
eine andere Idee, nicht bloss eine sauberere Umsetzung. In M1 und M2 tragen
deshalb die beiden anderen Achsen.

#### Rollen dürfen in derselben Aufgabe liegen

Die vier Rollen verlangen **keine vier Aufgaben**. Anker und Verschärfung sitzen
häufig auf ST1 und ST2 derselben Aufgabe — das ist die Subtask-Leiter aus
Abschnitt 2, und sie ist der Normalfall, nicht die Ausnahme. Eine Rolle gilt als
abgedeckt, sobald sie irgendwo im Modul vorkommt.

### Spoiler-Management

Musterlösungen und Foren sind teilweise zugänglich. Der Weg über das Material
muss bequemer sein als der Blick in eine fremde Lösung: Konzept und Hinweise
sofort verfügbar, unsere Musterlösung erst nach eigenem Versuch.

**Mit Konzept-zuerst verschiebt sich das Problem.** Früher war die Versuchung,
die Lösung zu suchen, weil man nicht auf die Idee kam. Jetzt steht die Idee auf
der Seite — die Versuchung ist, sie zu lesen und sich das Umsetzen zu sparen.
Dagegen wirken die zwei Regeln aus Abschnitt 4 und die Trennung der Musterlösung
auf eine eigene Seite.

---

## 7. Modulplan Ausbaustufe 1 (24 Lektionen, 5 davon komprimierbar)

**Die Nummer gibt die Reihenfolge an, der Name das Thema, die Konzeptspalte den
Inhalt.** Wer beim Lesen der Konzeptspalte merkt, dass er das schon kann,
überspringt das Modul — dafür steht auf jeder Modulseite oben eine
Einstiegskarte mit dem Freischaltkriterium der Voraussetzung.

### Strang A — Programmieren (Vorrunde)

| | Modul | L | Konzepte | Ankeraufgaben |
|---|---|---|---|---|
| M0 | Werkzeugkasten | 2 | Werkzeug-Baustein, keine Konzepte | `stairracing` ST1 |
| M1 | Problemanalyse und Modellierung | 2 | Vom Text zum Modell · Die Probe am Extremfall · Prüfen statt Rechnen | `cheeseparty`, `directions`, `sushi` ST1/ST3 |
| M2 | Vollständige Suche | 2 | Vollständige Suche · Die Invariante · Teilpunkte mitnehmen | `endurance` ST1/ST2, `stairracing` ST2 |
| M3 | Laufzeitdenken | 3 | Komplexität und Faktor T · Weitergeben statt neu berechnen · Versteckte Schleifen · Mengen und Wörterbücher | `endurance` ST2→ST3, `stairracing` ST3/ST4 |
| M4 | Felder und lineare Techniken | 3 | Präfixsummen · Zweizeiger und Fenster | `endurance` ST4/ST5, `stairracing` ST4 |
| M5 | Sortieren und Suchen | 3 | Sortieren als Vorverarbeitung · Binäre Suche | `sushi` ST2/ST4, `Thermalquellen` ST1 |
| M6 | Zeichenketten und Gitter | 2 | Zeichenketten · Zweidimensionale Felder · Nachbarschaft | `Geheimcode` ST1, `Palatinusgruft` ST1 — **noch zu prüfen** |
| M7 | Konstruktive Verfahren | 2 | Gierige Verfahren · Invarianten · Zustandsdenken | `Mahjong` ST1, `Mäusetanz` ST1/ST2 — **noch zu prüfen** |

### Strang B — Denken ohne Code (Erste Runde)

| | Modul | L | Inhalt |
|---|---|---|---|
| B1 | Pseudocode und Simulation | 3 | Ablauf von Hand durchspielen, Theorie-Teilaufgaben aus dem Archiv |
| B2 | Quiz-Training | 2 | 40 Min unter Zeitdruck, MC-Strategie, wann raten |

**Strang B heisst B1/B2 und nicht M8/M9.** Die alten Nummern haben suggeriert,
der Strang komme zum Schluss — das Gegenteil ist gemeint.

### Ausserhalb des Kursfadens

Die Rubrik **Hintergrund** erklärt, wie ein Werkzeug innen funktioniert. Keine
Module, keine Voraussetzung, optional zu lesen, aus den Modulen verlinkt.

| Seite | Anschluss |
|---|---|
| Sortierverfahren | M5, und M3 als Komplexitätsvergleich |
| geplant: warum `liste.pop(0)` O(N) ist | M3 |
| geplant: wie eine Menge in O(1) nachschlägt | M3 |

**Strang B läuft parallel eingestreut, nicht am Schluss.** Die
Pseudocode-Übungen funktionieren ab M2 und sind der Rettungsanker für SuS, die
beim Programmieren hängen. Nebeneffekt: An der Ersten Runde kann die ganze Klasse
teilnehmen, auch wer kaum programmiert.

**Skalierung:** Bei 15 Lektionen M4 und M5 auf je 2 kürzen, M6 und M7 streichen.
Bei 25 Lektionen M3 und B1 ausbauen.

### Begründete Abweichungen von der ursprünglichen Themenliste

- **Laufzeitdenken vorgezogen** (M3 statt spät): Ohne Laufzeitdenken sind die
  Subtask-Sprünge unerklärlich.
- **Datenstrukturen nicht als eigenes Modul**: Sets, Dicts usw. werden dort
  eingeführt, wo ein Problem sie erzwingt. Ein isoliertes Datenstruktur-Modul
  ohne Problemdruck wäre Stoff ohne Anlass. Sie stehen aber **als benanntes
  Konzept in der Modulliste** — sonst gehen sie unter, wie `set` in M3.
- **Strang B neu**: Die Erste Runde testet eine andere Kompetenz als das
  Programmieren. Wer nur programmiert, ist darauf nicht vorbereitet.
- **M6 Zeichenketten und Gitter neu.** Beides kommt im Archiv regelmässig vor
  und hatte bisher keinen Ort, weil keine Ankeraufgabe es erzwungen hat. Genau
  die Lücke, die eine konzeptgetriebene Liste schliesst. Konstruktive Verfahren
  rutschen dafür von M6 auf M7.
- **Rekursion und Geometrie bleiben draussen.** Sie stünden auf einer
  Vollständigkeitsliste, aber im zugänglichen Archiv fordert sie keine einzige
  Teilaufgabe der Ausbaustufe 1 — Rekursion braucht man erst für DP, Geometrie
  kommt einmal vor (`Changifälle`, C-bewertet). Beides gehört in Ausbaustufe 2.
  Konzepte ohne Anlass aufzunehmen, nur damit die Liste voll aussieht,
  widerspricht dem empirischen Vorgehen von `lp/kuratierung.md`.
- **Binäre Suche ohne Ankeraufgabe.** Sie steht in M5, obwohl keine zugängliche
  SOI-Teilaufgabe sie fordert — weil sie zum Sortieren gehört und in der Ersten
  Runde als Quizfrage vorkommen kann. Solche Konzepte werden auf der Seite
  ausdrücklich gekennzeichnet.
- **Zwei geplante Konzepte gibt es in den Modulen gar nicht.** „Rechnen mit
  Resten" (M1) und „Einen Ablauf simulieren" (M2) standen hier als Kandidaten aus
  `Rubiks Knauf` und `Trampolin`, also aus der Kuratierungsliste und nicht aus
  den gebauten Modulen. Beim Umbau zeigte sich, dass die Module ihre Konzepte
  längst haben, nur andere: **die Probe am Extremfall** in M1, **die Invariante**
  und **Teilpunkte mitnehmen** in M2.

    Modulo und Simulation bleiben Kandidaten, brauchen aber je eine geprüfte
    Ankeraufgabe. `Trampolin` ST1 (Qualifikationsrunde 2024/25, A-bewertet) ist
    für die Simulation die erste Wahl und passt auch zu B1.

    **Lehre daraus:** Die Konzeptspalte der Modulliste wird aus dem gebauten
    Modul gefüllt, nicht aus der Kuratierung. Sonst behauptet der Plan Inhalte,
    die nirgends stehen.

---

## 8. Seitenstruktur pro Lernbaustein

Drei Dateien pro Modul: `index.md`, `uebungen.md`, `loesung.md`.

```
# M5 — Sortieren und Suchen                        (index.md)

!!! note Du kannst hier einsteigen, wenn ...    ← Selbsteinordnung
**In diesem Modul:** Konzept A · Konzept B      ← Sprungmarken
Vorspann, zwei bis vier Saetze

## Sortieren als Vorverarbeitung                ← Konzeptblock 1
   ### Worum es geht
   ### Die Idee                 Kernsatz, Analogie + Bruchstelle
   ### An einem Beispiel        von Hand durchgerechnet
   ### Im Code
   ### Laufzeit                 Komplexitaet, Faktor T, Groessenordnung
   ### Woran du es erkennst     die Signale im Aufgabentext
   ### Typische Fallen

## Binäre Suche                                 ← Konzeptblock 2
   dieselbe Gliederung

## Prüfe dich selbst
   ▸ Vergleiche deine Antwort   ← ??? success, 3–4 Fragen
## Übungen                      ← Verweis auf uebungen.md
## Weiter zu M6
```

```
# M5 — Übungen                                     (uebungen.md)

!!! note Du musst nichts nachschlagen
!!! tip  Gerüststufe

## Die Aufgabe: Sushi           Geschichte, Leitertabelle, Format
### Einstieg — Teilaufgabe 2    Schranken, Beispiel, Zeitangabe
    ▸ Hinweis 1 · 2 · 3         ← ??? tip
    !!! success Einreichen      ← Link mit Teilaufgaben-Anker
### Kern — Teilaufgabe 4
## Vertiefung — Thermalquellen  ← nennt das Konzept nicht beim Namen
## Trockenübungen
Link auf loesung.md             ← ganz am Seitenende
```

**Ein Modul hat ein bis drei Konzeptblöcke.** Mehr wird unübersichtlich; dann
lieber ein zweites Modul. Jeder Block hat eine eigene Sprungmarke und ist damit
einzeln verlinkbar — das ist die Nachschlagefunktion aus Abschnitt 1.

`Woran du es erkennst` ist der Abschnitt, den es im alten Format nicht gab und
der eine Konzeptseite überhaupt erst brauchbar macht. Er wird nie weggelassen.

### Reibung nach Inhalt abstufen

Aufklappen ist nur *eine* Stufe von Reibung. Der Unterschied, auf den es
ankommt: Einen Hinweis zu früh zu sehen ist ärgerlich, aber reparabel — der
nächste Hinweis kommt ja noch. Die Musterlösung zu früh zu sehen zerstört die
Aufgabe endgültig. Ein zugeklapptes Element mit der Beschriftung „Musterlösung"
ist eine ständige Versuchung, und ein Klick passiert reflexhaft.

| Inhalt | Mechanik | Reibung |
|---|---|---|
| Hinweise 1–5 | `??? tip` auf der Seite | niedrig |
| Selbstcheck | `??? success` auf der Seite | niedrig |
| Musterlösung | **eigene Seite** `loesung.md`, Link am Seitenende | hoch |

Die Standardtypen von MkDocs Material bringen die farbliche Unterscheidung
bereits mit (`tip` orange, `success` grün) — **kein eigenes CSS nötig**.

### Verworfene Alternativen

- **Tabs** für Hinweise: Alle Reiter sind gleichzeitig da, die Staffelung
  verschwindet.
- **Weichzeichnen / Spoiler-Effekt**: braucht JavaScript, mit Tastatur und
  Screenreader schlecht bedienbar, kein Gewinn gegenüber `<details>`.
- **Hinweise am Seitenende mit Ankerlinks**: reines Markdown, funktioniert auch
  auf Papier — aber der Rücksprung lässt die Stelle im Text verlieren. Nur
  sinnvoll, wenn Ausdrucken wichtig wird. Falls das kommt: Browser drucken
  zugeklappte `<details>` unterschiedlich, dann braucht es ein Druck-Stylesheet.

Selbstcheck-Fragen sind Anwendung, nicht Reproduktion. Nicht „Was ist ein
Zweizeiger?", sondern: *„N ≤ 200 000, du hast eine O(N²)-Lösung. Reicht das in
Python?"*

### Alltagsanalogie — Platzierung und Kriterien

**Die Analogie steht im Konzeptblock unter `Die Idee`**, direkt nach dem
Kernsatz, samt Bruchstelle.

Das war früher anders: Solange das Material mit dem Problem begann, hätte eine
Analogie am Seitenanfang die Entdeckung vorweggenommen, und sie sass deshalb auf
Hinweisstufe 2. Mit der Umstellung auf Konzept-zuerst entfällt dieser Grund —
die Erklärung *soll* jetzt vorne stehen, und die Analogie gehört zur Erklärung.

Drei Kriterien, unverändert — das dritte wird nach wie vor am häufigsten
vergessen:

1. **Gleiche Struktur, andere Oberfläche** — nicht bloss dasselbe Thema in
   anderen Worten
2. **Von Hand prüfbar in unter einer Minute** — sonst ist sie ein zweites Problem
3. **Bekannte Bruchstelle** — wo endet die Analogie? Ohne diese Angabe überdehnen
   SuS sie und schliessen falsch

Beispiel für M4:

> **Analogie:** Im Klassenbuch stehen die Absenzen eines Jahres. Du darfst drei
> Fehltage entschuldigen. Wie lang ist die längste Strecke ohne unentschuldigte
> Absenz?
>
> **Bruchstelle:** Die Analogie legt nahe, dass du für jeden Starttag neu
> durchzählst. Genau das ist die langsame Lösung — sie erklärt das Problem, nicht
> die Lösung.

Dass die Bruchstelle hier die naive Lösung ist, macht sie besonders brauchbar:
Sie motiviert den nächsten Schritt, statt ihn vorwegzunehmen.

---

## 9. Einlese-Gerüst mit Abbauplan

Bisherige Praxis (fertige Einlese-Funktionen) ist richtig — aber als **Gerüst mit
Abbauplan**, nicht als Dauerzustand. Im Wettbewerb ist das Einlesen Teil der
Aufgabe, und Formatfehler sind der häufigste Punkteverlust.

| Stufe | Module | Was die SuS bekommen |
|---|---|---|
| 1 | M0–M2 | `vorlage.py` — Leser und Hauptteil fertig, nur `loese` fehlt |
| 2 | M3–M4 | `vorlage-stufe2.py` — Leser fertig, das Einlesen eines Testfalls ist eine Lücke mit Muster |
| 3 | ab M5 | `vorlage-stufe3.py` — nur noch die Datei als Wortliste. Leser, Hauptteil und Ausgabezeilen komplett selbst, dazu eine Merkliste im Dateikopf |

### Dateien statt Umleitung

Gestartet wird über den **Play-Knopf in VS Code**, nicht über die Konsole. Die
SuS sollen sich auf die Aufgabe konzentrieren, nicht auf eine Shell, die sie
sonst nie benutzen. Ein- und Ausgabedatei stehen deshalb als Konstanten im Kopf
der Datei und liegen im Aufgabenordner.

Das ist nicht nur bequemer, sondern auch sicherer: `python loesung.py > output.txt`
schreibt in Windows PowerShell 5.1 eine **UTF-16-Datei**. Der Grader erwartet
UTF-8. Dieser Fehler ist von aussen nicht zu sehen und genau die Sorte, für die
SOI eine eigene Hilfeseite betreibt. Schreibt Python die Datei selbst, ist das
Problem weg — mitsamt der Zeilenumbruch-Frage, denn `newline="\n"` steht in der
Vorlage.

Zwei Nebeneffekte, beide erwünscht: `print` landet wieder im Terminal und ist
damit gefahrlos für Debug-Ausgaben, und die Vorlage braucht kein `import sys`
mehr.

Der Preis ist ein Handgriff: Vor dem echten Lauf muss `EINGABE` von
`"bsp_ein.txt"` auf `"input.txt"` umgestellt werden. Das ist der wahrscheinlichste
Fehler in M0 und gehört einmal gemeinsam durchgespielt.

### Der Token-Leser

Die SOI-Formate sind einheitlich genug, dass ein einziger Token-Leser fast alles
abdeckt:

```python
EINGABE = "bsp_ein.txt"
AUSGABE = "output.txt"

with open(EINGABE, encoding="utf-8") as datei:
    tokens = datei.read().split()

position = 0

def zahl():
    global position
    position = position + 1
    return int(tokens[position - 1])

def zahlen(anzahl):
    liste = []
    for i in range(anzahl):
        liste.append(zahl())
    return liste

def wort():
    global position
    position = position + 1
    return tokens[position - 1]
```

Damit wird `endurance` zu:

```python
zeilen = []

T = zahl()
for i in range(T):
    N = zahl()
    K = zahl()
    p = zahlen(N)
    ergebnis = loese(N, K, p)      # ← das ist die Aufgabe der SuS
    zeilen.append("Case #" + str(i) + ": " + str(ergebnis))

pruefe.schreibe(AUSGABE, zeilen)
```

**Die Zeilen für `append` und `schreibe` in Stufe 1 und 2 immer mitliefern**,
erst in Stufe 3 freigeben. `Case #i` ist nullbasiert — ein Zählfehler kostet
100 Punkte.

Der Code verzichtet bewusst auf List Comprehensions, f-Strings und
Mehrfachzuweisungen. Die Einstiegsniveaus sind zu verschieden; wer diese
Schreibweisen nicht kennt, liest sonst die halbe Vorlage nicht.

### Lokale Testroutine

Die Beispiel-Ein-/Ausgaben stehen bei jedem Subtask in der Aufgabenstellung.
Feste Konvention: abtippen als `bsp_ein.txt` / `bsp_aus.txt`. Ein Klick auf Play
rechnet, schreibt `output.txt` und vergleicht anschliessend selbst — der Vergleich
steht als letzte Zeile in der Vorlage und läuft nur, solange `EINGABE` auf
`bsp_ein.txt` steht.

Das nimmt der 5-Minuten-Regel den Schrecken: Wer hier grün sieht, lädt entspannt
herunter. **Der Download-Klick gehört ans Ende der Lektion, nicht an den Anfang.**

---

## 10. Python-Kalibrierung

### Laufzeit-Faustregel

### Das Modell im Kurs — vier Schritte

Die Laufzeitabschätzung läuft im ganzen Material über die Komplexität, nie über
Messwerte. Vier Schritte, mehr nicht:

1. **Schleifen zählen.** Ineinander liegende Schleifen über die Eingabe:
   eine → O(N), zwei → O(N²), drei → O(N³).
2. **Schranke einsetzen.** O(N²) mit N = 1000 ergibt 10⁶.
3. **Mal die Anzahl Testfälle T.**
4. **Grössenordnung nachschlagen.**

| Schritte | Grössenordnung der Dauer |
|---|---|
| 10⁶ | Sekundenbruchteil |
| 10⁷ | rund eine Sekunde |
| 10⁸ | rund zehn Sekunden |
| 10⁹ | Minuten |
| 10¹⁰ | halbe Stunde |
| 10¹² | Tage |

### Die vereinfachte Annahme — und was sie unterschlägt

Der Tabelle liegt eine grobe Annahme zugrunde: **Python schafft rund 10⁷
Schleifendurchläufe pro Sekunde, und jeder Durchlauf ist gleich teuer.** Beides
stimmt nicht genau.

Unterschlagen werden:

- **Konstanten.** Ein Durchlauf mit einer Multiplikation und einem Listenzugriff
  dauert länger als einer mit einem Vergleich — leicht ein Faktor 3.
- **Geräteunterschiede.** Ein anderes Notebook rechnet zwei- bis dreimal
  schneller oder langsamer.
- **Speichereffekte.** Sehr grosse Listen werden langsamer, als die Zählung
  vermuten lässt.

Zusammen können das leicht ein bis zwei Grössenordnungen sein. Die Näherung
trägt trotzdem, weil die Unterschiede, auf die es ankommt, **Faktoren von tausend
und mehr** sind: zwischen 10⁸ und 10¹² liegt der Unterschied zwischen Sekunden
und Tagen, und daran ändert ein Faktor 3 nichts.

**Im Material wird diese Vereinfachung immer mitgenannt.** Die SuS sollen die
Grössenordnung schätzen und nicht glauben, sie könnten Sekunden vorhersagen.

### Unser Zeitbudget ist nicht das übliche

**Entscheidend und leicht zu übersehen:** Wir reichen eine Ausgabedatei ein, kein
Programm. Der Grader misst keine Laufzeit. Die einzige Grenze sind die **fünf
Minuten** zwischen Download und Upload.

Das ist ein völlig anderes Budget als die ein bis zwei Sekunden, mit denen
Wettbewerbsaufgaben sonst kalkuliert werden. Praktische Faustregel für den Kurs:

| Schritte | Grössenordnung | Urteil |
|---|---|---|
| bis 10⁸ | Sekunden | unproblematisch |
| 10⁹ | Minuten | ohne Reserve für einen zweiten Versuch |
| ab 10¹⁰ | halbe Stunde und mehr | ausgeschlossen |

Didaktische Folge: Kleine Unterschiede sind bei uns **egal**, grosse sind
**tödlich**. Eine Lösung mit 10⁸ statt 10⁶ Schritten braucht Sekunden statt eines
Sekundenbruchteils und gibt trotzdem volle Punkte. Eine mit 10¹² Schritten läuft
nie durch. Das Laufzeitdenken in M3 zielt deshalb auf Grössenordnungen, nicht auf
Konstanten — und genau deshalb reicht die grobe Annahme oben.

### Die Anzahl Testfälle gehört in jede Rechnung

Fast alle SOI-Aufgaben haben **T = 100 Testfälle pro Durchlauf**. Eine Schranke
von N ≤ 1000 bedeutet bei O(N²) also nicht 10⁶, sondern **10⁸ Schritte**. Die
übliche Tabelle „N ≤ 3000 erlaubt O(N²)" gilt pro Testfall und ist ohne den
Faktor T irreführend.

Mit T = 100 und dem Budget oben:

| N ≤ | O(N²) gesamt | Urteil |
|---|---|---|
| 100 | 10⁶ | bequem |
| 1 000 | 10⁸ | läuft, Sekunden |
| 3 000 | 10⁹ | zu riskant |
| 10⁵ | 10¹² | ausgeschlossen |

### Fallen, die in bestimmte Module gehören

- **`liste.pop(0)` ist O(N)** — gehört als Anker-Beispiel in M3, weil es an
  echtem Code zeigt, wie eine harmlose Zeile die Komplexität kippt
- **`input()` ist langsam und blockiert** — die Vorlage liest die Datei in einem
  Zug mit `read().split()`
- **Nur Standardbibliothek** — damit lokal und beim Grader dasselbe läuft
- Rekursionstiefe (Standard 1000) ist im reduzierten Umfang kaum relevant, wäre
  aber bei M6 zu beachten

---

## 11. Repo-Struktur

```
soi-kurs/
├─ CLAUDE.md                  # Baukonventionen für Claude Code
├─ KONZEPT.md                 # dieses Dokument
├─ docs/
│  ├─ index.md                # Wegweiser + Selbsttest
│  ├─ lernpfad.md             # Abhängigkeitsgraph
│  ├─ m00-werkzeugkasten/     # nur index.md (Werkzeug-Baustein)
│  ├─ m01-problemanalyse/     # index.md, uebungen.md, loesung.md
│  ├─ m02-vollstaendige-suche/
│  ├─ m03-laufzeitdenken/
│  ├─ m04-lineare-techniken/
│  ├─ m05-sortieren-und-suchen/
│  ├─ ...
│  └─ hintergrund/            # ausserhalb des Kursfadens, eigene Menürubrik
├─ vorlagen/                  # vorlage.py, vorlage-stufe2.py,
│                            # vorlage-stufe3.py, pruefe.py,
│                            # .vscode/settings.json
├─ hooks/                     # MkDocs-Hooks (externe Links im neuen Tab)
├─ lp/                        # LP-Blätter (Diagnose, Fehlvorstellungen)
└─ mkdocs.yml
```

Reines Markdown mit `<details>` funktioniert überall — auf GitHub Pages, im Repo,
in jeder Vorschau. **MkDocs Material** bringt zusätzlich Volltextsuche, `??? tip`- und
`??? success`-Blöcke mit fertigem Farbcode und Content Tabs für die drei Spuren
auf derselben Seite. Deployment über GitHub Actions.

Das `lp/`-Verzeichnis bleibt im selben öffentlichen Repo, aber ausserhalb der
Navigation — sonst pflegt es niemand.

---

## 12. Modul-Steckbrief (Spezifikationsschema)

```
Modul N — Titel
├─ Lernziele (beobachtbar formuliert)
├─ Voraussetzungen — und ausdruecklich: welche Module NICHT noetig sind
├─ Einstiegskarte (Freischaltkriterium der Voraussetzung, in Du-Form)
├─ 1 bis 3 Konzepte, je mit
│   ├─ Kernsatz
│   ├─ Alltagsanalogie (+ Bruchstelle)
│   ├─ durchgerechnetes Kleinbeispiel  (nicht die erste Uebungsaufgabe!)
│   ├─ Codemuster
│   ├─ Laufzeit (Komplexitaet, Faktor T, Groessenordnung)
│   ├─ Erkennungssignale im Aufgabentext
│   └─ typische Fallen
│   └─ falls ohne Ankeraufgabe: Kennzeichnung
├─ Selbstcheck-Fragen (3–4, mit Antworten)
├─ Ankeraufgabe + Subtask-Leiter (ST1..ST5 mit Schranken), auf uebungen.md
├─ Aufgaben: Einstieg / Kern / Vertiefung, je mit 3 Hinweisstufen
│   └─ mindestens eine nennt das Konzept nicht beim Namen
├─ Musterlösungen (eigene Seite loesung.md)
├─ Python-Hinweise (Fallen, Gerüststufe)
├─ Typische Fehlvorstellungen (für LP-Blatt)
├─ LP-Wert: hoch / mittel / niedrig
└─ Freischaltkriterium: „Konzept sitzt, wenn ..."
```

Die Rollen aus Abschnitt 6 — Anker, Variation, Verschärfung, Verkleidung —
gelten weiter. Sie ordnen sich der Stufung unter: Der **Einstieg** ist meist der
Anker, der **Kern** die Verschärfung, die **Vertiefung** die Verkleidung.

---

## 13. Stand und nächste Schritte

### Erledigt

- **Technisches Gerüst** — Repo, MkDocs Material, GitHub Pages über Actions,
  Hook für externe Links
- **Vorlagendateien** `vorlage.py`, `pruefe.py`, `.vscode/settings.json` —
  Start über den Play-Knopf, Ein- und Ausgabedatei als Konstanten
- **Abhängigkeitsgraph** in `docs/lernpfad.md`
- **M0 Werkzeugkasten** — Werkzeug-Baustein nach der Ausnahmestruktur, Anker
  `stairracing` ST1 aus der Runde 2021
- **M1 Problemanalyse und Modellierung** — Anker `cheeseparty`, Übungen
  `directions` und `sushi` ST1/ST3 aus der Runde 2018
- **M2 Vollständige Suche** — Anker `endurance` ST1/ST2, Übung `stairracing`
  ST2 aus der Runde 2021, dazu Laufzeit-Schätzaufgabe als Brücke zu M3
- **M3 Laufzeitdenken** — Anker `endurance` ST2→ST3, Übung `stairracing`
  ST3/ST4, Messübung zu versteckten Schleifen, Schätzrunde. Erste Anwendung
  von Gerüststufe 2 (`vorlage-stufe2.py`)
- **M4 Felder und lineare Techniken** — Anker `endurance` ST4/ST5
  (Präfixsummen, Zweizeiger), Übung `stairracing` ST4. Damit sind auf beiden
  Aufgaben alle Punkte erreichbar
- **Kuratierungsliste** über sieben Archivrunden in `lp/kuratierung.md`
- **Zugang zu den Aufgaben** — alle Links springen direkt zur Teilaufgabe, der
  Link zum Einreichen steht am Ende der Aufgabe statt zuoberst, jedes Modul
  zeigt die Leiter seiner Ankeraufgabe, und `docs/lernpfad.md` hat neben dem
  Abhängigkeitsgraphen die Aufgabenachse
- **M5 Sortieren und Suchen** — Anker `sushi` ST2/ST4, Transferaufgabe
  `Thermalquellen` ST1 aus 2022/2023. Erste Anwendung von Gerüststufe 3
  (`vorlage-stufe3.py`) und **erstes Modul im neuen Seitenformat**
- **Hintergrundrubrik** — erste Seite `docs/hintergrund/sortierverfahren.md`

**Anmerkung zu `wagashi`.** Die Aufgabe war als zweiter M2-Anker vorgesehen
(Abschnitt 6 und 7), ist dort aber falsch einsortiert: ST1 ist die Summe aller
aᵢ·cᵢ, also eine einzige Schleife — Modellierung, keine vollständige Suche. Sie
gehört zu M1. M2 verwendet stattdessen `stairracing` ST2, das M0 ohnehin schon
als Selbsttest vormerkt.

### Die Umstellung auf Konzept-zuerst

M0 bis M4 sind im **alten Format** gebaut: Problem → eigener Versuch → fünf
Hinweisstufen → Konzept. M5 ist der Proof of Concept des neuen Formats und
abgenommen. Die Umstellung war eine bewusste Entscheidung, ihre Begründung steht
in Abschnitt 4.

**Der Proof of Concept hat fünf Dinge gezeigt**, die jetzt in `CLAUDE.md` stehen:

- `Woran du es erkennst` ist der wertvollste neue Abschnitt und wird verbindlich
- Die Leitertabelle der Ankeraufgabe muss von `index.md` nach `uebungen.md`
  wandern, weil `index.md` keinen Aufgabentext mehr enthält — dasselbe gilt für
  den Einreichen-Link
- Konzepte ohne Ankeraufgabe brauchen eine feste Kennzeichnung
- Die Hinweisleiter verliert nicht einfach zwei Stufen: Stufe 2 (Analogie) und
  Stufe 5 (Umsetzungsdetail) entfallen, weil beides in den Konzeptblock wandert
- Gegen die Illusion des Verstehens braucht es zwei harte Regeln (Abschnitt 4)

**Der Umbau ist durch.** M1 bis M5 stehen im neuen Format, die Startseite, der
Lernpfad und die neue Konzeptübersicht sind darauf abgestimmt. Alle
Musterlösungen wurden aus den Markdown-Dateien extrahiert und gegen die
offiziellen Beispiele laufen gelassen, die gierigen und umgeformten zusätzlich
gegen vollständige Suche auf Zufallsfällen.

Beim Umbau nachgezogen:

- **Aufgabennamen deutsch** wie auf soi.ch: Käsefest, Wegbeschreibung, Ausdauer,
  Treppenlauf, Sushi, Thermalquellen. Vorher standen dort die englischen Kürzel
  aus der Adresszeile.
- **Musterlösungen sind vollständige Programme.** In M2 bis M4 standen Fragmente
  ohne Leser („Kopf wie in M1"); wer sie kopierte, bekam einen `NameError`.
- **`set` steht jetzt auf der Modulseite von M3**, nicht mehr nur in der Lösung.
- **Wegbeschreibung Teilaufgabe 2** war nirgends verlinkt — 20 Punkte, die es im
  Material nicht gab.
- **Der Mermaid-Graph im Lernpfad hat nie gerendert.** Ersetzt durch ein
  eingebettetes SVG ohne JavaScript, das zusätzlich zeigt, welche Module schon
  gebaut sind.
- **Blättern am Seitenende** (`navigation.footer`) mit eindeutigen Beschriftungen
  — der rote Faden auch in der Bedienung.

### Offen

**Neue Module.**

1. **M6 Zeichenketten und Gitter** — `Geheimcode` ST1 (2020), `Palatinusgruft`
   ST1 (2023). Beide noch ungeprüft, siehe Prüfpflicht in `CLAUDE.md`.
2. **M7 Konstruktive Verfahren** — `Mahjong` ST1 (2018), `Mäusetanz` ST1/ST2
   (2022)
3. **Strang B** — B1 Pseudocode und Simulation, B2 Quiz-Training. Material steht
   bereit: `Greifer-Sortierung` ST1, `Trampolin` ST1 und sechs
   Theorie-Teilaufgaben, siehe `lp/kuratierung.md`

**Inhaltliche Lücken.**

4. **Seite „gemischte Aufgaben"** ohne Konzeptangabe, als Gegenpol zum Katalog
   (Abschnitt 4). Jetzt sinnvoll, da vierzehn Konzepte stehen.
5. **In M5 fehlt die Rolle „Variation"** — Anker, Verschärfung und Verkleidung
   sind abgedeckt, eine Aufgabe mit gleicher Struktur in anderer Einkleidung
   nicht. Die Kandidaten aus der Kuratierung sind alle C-bewertet.
6. **„Einen Ablauf simulieren" und „Rechnen mit Resten"** brauchen je eine
   geprüfte Ankeraufgabe, bevor sie in ein Modul kommen. Erste Wahl:
   `Trampolin` ST1 und `Rubiks Knauf` ST1.
7. **Gemessene Laufzeiten überprüfen** — die Zahlen in Abschnitt 10 und in M3
   stammen von einem Gerät. Auf Schulgeräten einmal nachmessen; die
   Grössenordnungen sollten stimmen, die Sekundenwerte können abweichen.

**Technisches.**

8. **MkDocs ist jetzt lokal installiert** (`mkdocs`, `mkdocs-material`), damit
   vor jedem Vorlegen ein `mkdocs build --strict` läuft. Zum Anschauen:
   `python -m mkdocs serve`, die Seite liegt dann unter
   `http://localhost:8000/soi-kurs/`. **Der Dateiwächter greift im
   OneDrive-Ordner nicht zuverlässig** — nach Änderungen den Server neu starten.

9. **GitHub Actions führt auf diesem Konto keine Jobs aus.** Seit dem
   12. August 2026 bleibt jeder Lauf in der Warteschlange stehen, ohne dass ein
   Runner anspringt; ältere Läufe wurden nach 46 und 228 Stunden abgebrochen.
   Actions ist aktiviert, der Workflow aktiv, das Repository öffentlich — die
   Ursache liegt auf Konto-Ebene und ist von aussen nicht zu beheben. **Das
   gehört geklärt**, denn ohne Actions gibt es keine automatische
   Veröffentlichung.

    Bis dahin läuft das Deployment von Hand, in zwei Schritten:

    ```
    python -m mkdocs gh-deploy
    gh api -X POST repos/masta-nksa/soi-kurs/pages/builds
    ```

    Der erste Befehl baut die Seite und schiebt sie auf den Branch `gh-pages`.
    Der zweite stösst den Pages-Build an — nötig, weil auch der automatische
    Branch-Build über Actions liefe.

    Die Pages-Quelle steht dafür auf **Branch `gh-pages`** statt auf „GitHub
    Actions". Solange das so ist, würde `.github/workflows/deploy.yml` beim
    Schritt `actions/deploy-pages` scheitern, falls Actions wieder anspringt.
    Dann entweder die Quelle zurückstellen oder den Workflow auf `gh-pages`
    umbauen.
