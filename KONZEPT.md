# SOI-Vorbereitungskurs — Konzept

Stand: 10. August 2026

Dieses Dokument hält den Stand der Konzeptarbeit fest. Es ist die Grundlage für
die weitere Ausarbeitung der einzelnen Module und für die technische Umsetzung.

---

## 1. Zielsetzung und Abgrenzung

Interaktiver Vorbereitungskurs für die Schweizer Informatik-Olympiade (SOI) mit
starkem Übungs- und Entdeckungscharakter.

**Im Umfang:**

- Vorrunde (Pre-Round) — Programmieraufgaben
- Erste Runde — Online-Quiz, algorithmisches Denken ohne Code

**Nicht im Umfang:** Zweite Runde und alles Weiterführende. Wer die Zweite Runde
erreicht, wird von der ETH in speziellen Workshops betreut.

**Daraus folgt die Streichung** von Graphen, dynamischer Programmierung,
fortgeschrittenen Datenstrukturen und weitgehend auch Rekursion. Das ist
Zweitrunden- und Camp-Stoff.

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

> Problem → eigene Lösungsversuche → gezielte Hinweise → Konzept entdecken →
> systematische Erklärung → weitere Übungen → Transfer auf schwierigere Probleme

### Hinweisleiter (fünf Stufen)

1. **Perspektivfrage** — „Was ändert sich, wenn du die Daten sortierst?"
2. **Beobachtung erzwingen** — kleines Beispiel, das die Struktur sichtbar macht.
   *Hier sitzt die Alltagsanalogie.*
3. **Teilstrategie** — „Kannst du für ein festes linkes Ende die Antwort schnell
   bestimmen?"
4. **Kernidee benennen** — „Das linke Ende muss nie zurückwandern."
5. **Umsetzungsdetail** — nur bei Implementierungsblockade

**Regeln:** nie mehr als eine Stufe pro Anfrage; nie Code als Hinweis; ein
Hinweis darf die nächste Stufe nicht vorwegnehmen.

### Beispiel-Durchlauf (Zweizeiger, Modul 4)

`endurance` ST4 → eigener Versuch: O(N²), alle Startpunkte durchprobieren,
funktioniert bei N ≤ 100 → Hinweisstufe 3 → Entdeckung: beim Verschieben des
rechten Endes muss das linke nie zurück → systematische Erklärung: Zweizeiger,
amortisiert O(N), Invariante formulieren → Übungen → Transfer: ST5 mit N = 10⁵.

---

## 5. Adaptivität: drei Spuren, keine Gruppentrennung

Alle arbeiten am **selben Problem**, aber unterschiedlich tief. Keine A-/B-Gruppen,
keine „Zusatzblätter für die Schnellen" — das erzeugt Stigma und doppelte
Materialpflege.

| Spur | Umfang |
|---|---|
| **Basis** | Subtask 1–2 (kleine Schranken, Brute Force ist erlaubt und *richtig*) |
| **Kern** | Subtask 3–4, das eigentliche Konzept |
| **Vertiefung** | Subtask 5 + eine Verkleidungsaufgabe, oder Laufzeitbeweis / Gegenbeispielsuche |

**Wichtig:** Brute Force in der Basisspur darf nicht als „Notlösung" markiert
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

### Aufgabenrollen

Jede Konzepteinheit braucht alle vier:

- **Anker** — das Problem, an dem das Konzept entsteht
- **Variation** — gleiche Struktur, andere Einkleidung
- **Verschärfung** — höhere Schranke, erzwingt saubere Umsetzung
- **Verkleidung** — Konzept nötig, aber nicht sichtbar (echter Transfer)

Plus zwei Sondertypen: **Laufzeit-Schätzaufgaben** und **Widerlegungsaufgaben**.

### Spoiler-Management

Musterlösungen und Foren sind teilweise zugänglich. Die Hinweisleiter muss
attraktiver sein als der Blick in die Lösung: Hinweise sofort verfügbar, Lösung
erst nach dokumentiertem eigenem Versuch.

---

## 7. Modulplan (22 Lektionen, 5 davon komprimierbar)

### Strang A — Programmieren (Vorrunde)

| | Modul | L | Anker |
|---|---|---|---|
| M0 | Werkzeugkasten | 2 | `addition`, `books` — VS Code, stdin/stdout, 5-Minuten-Regel |
| M1 | Problemanalyse & Modellierung | 2 | `cheeseparty` (ST1→ST2 dreht das Problem um: prüfen statt rechnen), `directions` |
| M2 | Vollständige Suche | 2 | `endurance` ST1/2, `wagashi` ST1 |
| M3 | Laufzeitdenken | 3 | `endurance` ST2→ST3 — der Sprung N: 100 → 10⁵ *ist* die Lektion |
| M4 | Felder & lineare Techniken | 3 | `endurance` ST4/5 — Präfixsummen, Zweizeiger |
| M5 | Sortieren & Suchen | 3 | `sushi` ST2/ST4 — Sortieren als Vorverarbeitung, binäre Suche |
| M6 | Konstruktive Verfahren | 2 | `mahjong` ST1 — Invarianten, Zustandsdenken |

### Strang B — Denken ohne Code (Erste Runde)

| | Modul | L | Inhalt |
|---|---|---|---|
| M7 | Pseudocode & Simulation | 3 | Ablauf von Hand durchspielen, Theorie-Subtasks aus dem Archiv |
| M8 | Quiz-Training | 2 | 40 Min unter Zeitdruck, MC-Strategie, wann raten |

**Strang B läuft parallel eingestreut, nicht am Schluss.** Die
Pseudocode-Übungen funktionieren ab M2 und sind der Rettungsanker für SuS, die
beim Programmieren hängen. Nebeneffekt: An der Ersten Runde kann die ganze Klasse
teilnehmen, auch wer kaum programmiert.

**Skalierung:** Bei 15 Lektionen M4 und M5 auf je 2 kürzen, M6 streichen. Bei 25
Lektionen M3 und M7 ausbauen.

### Begründete Abweichungen von der ursprünglichen Themenliste

- **Laufzeitdenken vorgezogen** (M3 statt spät): Ohne Laufzeitdenken sind die
  Subtask-Sprünge unerklärlich.
- **Datenstrukturen nicht als eigenes Modul**: Sets, Dicts usw. werden dort
  eingeführt, wo ein Problem sie erzwingt. Ein isoliertes Datenstruktur-Modul
  ohne Problemdruck widerspricht dem didaktischen Muster.
- **Strang B neu**: Die Erste Runde testet eine andere Kompetenz als das
  Programmieren. Wer nur programmiert, ist darauf nicht vorbereitet.

---

## 8. Seitenstruktur pro Lernbaustein

Drei Dateien pro Modul: `index.md`, `uebungen.md`, `loesung.md`.

```
# M4 — Zweizeiger              (index.md)

## Das Problem                    ← offen
## Probier es selbst              ← offen, mit Zeitangabe
   ▸ Kommst du nicht weiter?      ← ??? tip
## Hinweise
   ▸ Hinweis 1 — erst selbst versuchen
   ▸ Hinweis 2 — erst selbst versuchen   (hier die Analogie)
   ▸ Hinweis 3 · 4 · 5
## Das Konzept                    ← offen: Kernsatz, Invariante, Laufzeit
                                    (Analogie voll entfaltet + Bruchstelle)
## Prüfe dich selbst
   ▸ Vergleiche deine Antwort     ← ??? success, 3–4 Fragen
## Übungen                        ← Verweis auf uebungen.md
## Weiter zu M5
```

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

**Die Analogie ist ein Hinweis, keine Einleitung.** Am Seitenanfang würde sie das
didaktische Muster kippen: Aus „Problem → eigener Versuch → Entdeckung" würde
„hier ist das Konzept, jetzt wende es an". Sie sitzt daher auf Hinweisstufe 2 und
wird in der systematischen Erklärung *nach* der Entdeckung voll entfaltet.

Drei Kriterien — das dritte wird meist vergessen:

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
| 1 | M0–M2 | fertige `lies_*`-Funktionen, direkt aufrufbar |
| 2 | M3–M4 | Vorlage mit Lücke — Parsing nach Muster ergänzen |
| 3 | ab M5 | nur noch das Grundgerüst, Parsing komplett selbst |

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

C++ schafft grob 10⁸ einfache Operationen pro Sekunde, CPython eher 10⁶–10⁷
Schleifeniterationen. Die Regel „N-Schranke lesen ⇒ Komplexität ableiten" braucht
daher eine eigene Tabelle:

| N ≤ | erlaubte Komplexität (Python) |
|---|---|
| 20 | O(2ᴺ) |
| 500 | O(N³) |
| 3 000 | O(N²) |
| 10⁵ – 10⁶ | O(N log N), O(N) |

Bei N ≤ 5000 und O(N²) wird es in Python grenzwertig, wo C++ noch bequem
durchläuft. Didaktisch nützlich: Der Druck zur besseren Komplexität setzt früher
ein.

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
│  ├─ m00-werkzeugkasten/
│  │   ├─ index.md
│  │   ├─ uebungen.md
│  │   └─ loesung.md
│  ├─ m03-laufzeit/
│  └─ ...
├─ vorlagen/                  # vorlage.py, pruefe.py, .vscode/settings.json
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
├─ Voraussetzungen (welche Module)
├─ Ankeraufgabe + Subtask-Leiter (ST1..ST5 mit Schranken)
├─ Hinweisleiter (5 Stufen, ausformuliert)
├─ Alltagsanalogie (+ Bruchstelle)
├─ Systematische Erklärung (Kernsatz + Invariante + Laufzeit)
├─ Selbstcheck-Fragen (3–4, mit Antworten)
├─ Übungen: Variation / Verschärfung / Verkleidung (eigene Seite)
├─ Musterlösungen (eigene Seite loesung.md)
├─ Python-Hinweise (Fallen, Gerüststufe)
├─ Typische Fehlvorstellungen (für LP-Blatt)
├─ LP-Wert: hoch / mittel / niedrig
└─ Freischaltkriterium: „Konzept sitzt, wenn ..."
```

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

### Abweichung von der ursprünglichen Planung

Vorgesehen war **Modul 4 als Prototyp**, um Analogie und Gerüstabbau früh zu
testen. Nach M0 ist die Reihenfolge stattdessen linear geworden. Zwei Gründe:

- M4 ankert auf `endurance` ST4/ST5 und setzt das Laufzeitdenken aus M3 voraus.
  Wer M4 zuerst schreibt, muss erfinden, was M3 etabliert hat, und es später
  nachziehen.
- Die Seitenstruktur aus Abschnitt 8 wird von M1 ebenso getestet. M0 prüft sie
  nicht, weil Werkzeug-Bausteine der Ausnahmestruktur folgen.

Der Prototyp-Gedanke ist damit eingelöst, aber nicht vollständig: **Gerüststufe 2
(Vorlage mit Lücke) und eine Analogie zu einem schweren Konzept sind weiterhin
ungetestet.** Beim Bau von M3 und M4 gezielt darauf achten — dort zeigt sich, ob
das Format auch unter Last trägt.

### Offen

1. **M2 Vollständige Suche**
2. **M3 Laufzeitdenken** — erstes Modul mit Gerüststufe 2, also der erste echte
   Test des Abbauplans aus Abschnitt 9
3. **M4 Felder und lineare Techniken**
4. **M5 Sortieren und Suchen**, **M6 Konstruktive Verfahren**
5. **Strang B** — M7 Pseudocode und Simulation, M8 Quiz-Training
6. **Kuratierungsliste** — welche Subtasks aus welchen Archivrunden geerntet
   werden. Bisher pro Modul einzeln gesucht, was mit jedem Modul teurer wird.
   Für archivierte Aufgaben lassen sich weiterhin Eingaben erzeugen und
   Ausgaben prüfen, sie sind also gleichwertig zur Vorrunde.
7. **Selbsttest vor Modul 0** — `docs/index.md` nennt ihn, verlinkt aber
   `books` nicht und sagt nicht, woran man „sicher gelöst" erkennt
