# Kuratierungsliste — Archivaufgaben

Gesichtet am 10. August 2026: sieben Runden, 55 Aufgaben. Grundlage sind die
Aufgabentexte auf soi.ch (Anriss der Aufgabenstellung und die Schrankenblöcke
aller Teilaufgaben).

Diese Liste ersetzt das Durchsuchen des Archivs pro Modul. Sie ist eine
Vorauswahl, keine Freigabe — siehe „Vorbehalt" am Schluss.

## Bewertungsschlüssel

| | Bedeutung |
|---|---|
| **A** | Sofort einsetzbar, erste Teilaufgabe ist ein sicherer Erfolg (winzige Schranke wie N = 2, N = 3, zwei Objekte) |
| **B** | Brauchbar für ein bestimmtes Modul, aber nicht als Einstieg |
| **C** | Nur einzelne Teilaufgaben, mit Vorbehalt oder Zusatzaufwand |
| **D** | Nicht verwendbar — Graphen, DP, Spielstrategie, interaktiv oder nicht übersetzt |

---

## Vier Befunde, die für alles gelten

### 1. T = 100 ist der eigentliche Flaschenhals

**In praktisch jeder Aufgabe dieser Runden gibt es 100 Testfälle pro Durchlauf.**
Das ändert die Laufzeitrechnung grundlegend: Eine Teilaufgabe mit N ≤ 1000 klingt
nach „O(N²) reicht", ergibt aber 10⁶ Schritte pro Testfall und damit **10⁸
insgesamt** — in Python aussichtslos.

Faustregel für die Auswahl, nicht die N-Schranke allein lesen:

| Schranke | O(N²) pro Testfall | mit T = 100 | Python |
|---|---|---|---|
| N ≤ 100 | 10⁴ | 10⁶ | geht |
| N ≤ 300 | 10⁵ | 10⁷ | knapp |
| N ≤ 1000 | 10⁶ | 10⁸ | nein |

Für die Basisspur sind also nur Teilaufgaben mit **N ≤ 100** oder fester
Kleinstschranke (N = 2, 3, 5) wirklich brauchbar. Das halbiert die Ernte
gegenüber einer Auswahl, die nur auf N schaut.

### 2. `marathon` (2020) ist dieselbe Aufgabe wie `endurance` in der Vorrunde

Identische Teilaufgabenleiter: N = 3, N ≤ 100, N ≤ 10⁵, K = 3, K ≤ 100. Die
Aufgabe wurde für die Vorrunde neu aufgelegt.

**Konsequenz:** `marathon` nicht zusätzlich verwenden. Wer im Archiv nach
Lösungen sucht, findet dort die Lösung unseres M2-Ankers. Das ist auch ein
Argument, in M2 auf die Hinweisleiter zu verweisen statt aufs Archiv.

### 3. Das Archiv liegt über unserem Niveau — die Namen täuschen

Was auf soi.ch als „Erste Runde" archiviert ist, entspricht der heutigen
**Zweiten Runde**. Diese Aufgaben zielen auf ein Publikum, das den Kurs bereits
hinter sich hätte. Verwertbar sind fast ausschliesslich die **ersten ein bis zwei
Teilaufgaben**.

Die Ausnahme ist die **Qualifikationsrunde 2024/2025**: Sie hat eine
Junior-Kategorie mit eigenen, leichteren Aufgaben (`cheesemachine`, `rotation`).
Diese Runde ist die erste Adresse für die frühen Module.

### 4. Sechs Theorie-Teilaufgaben für Strang B

Mehrere Runden enthalten Teilaufgaben, die **ohne Code** gelöst werden —
Lösungsidee beschreiben und Korrektheit begründen. Genau das Material, das
`KONZEPT.md` Abschnitt 6 für Strang B vorsieht, und es war bisher nirgends
erfasst:

| Runde | Aufgabe | Teilaufgabe | Punkte |
|---|---|---|---|
| 2023 | Palatinusgruft | 4 (Theoretisch) | 50 |
| 2023 | Dada | 5 (Theoretisch) | 40 |
| 2022 | Zinnabbau | 5 (Theoretisch) | 10 + 30 |
| 2021 | Sate | 4 (theoretisch) | 50 |
| 2020 | Reversi | 4 (In der Theorie…) | 50 |
| 2020 | Regenwurm-Chirurgie | 3 (Theoretisch) | 60 |

Damit ist M7 materiell abgedeckt, ohne eine einzige eigene Aufgabe zu schreiben.

---

## Qualifikationsrunde 2024/2025

Die zugänglichste Runde. Junior-Aufgaben sind für weniger erfahrene
Teilnehmende gebaut.

| Aufgabe | Erste Teilaufgaben | Thema | Modul | |
|---|---|---|---|---|
| **Käsemaschine** *(junior)* | ST1: N = 2 · ST2/3: N = 3 | Messreihe auf Auffälligkeiten prüfen | M1–M2 | **A** |
| **Trampolin** | ST1 „Von Anfang an" · ST2 „Vom optimalen Trampolin" | Sprungfolge simulieren, dann alle Startpunkte | M2, M7 | **A** |
| **Zug** | ST1: N ≤ 50, M ≤ 50 | Haltebedingungen prüfen | M2 | **B** |
| **Rotation** *(junior)* | ST2: N, Q ≤ 100 | Rad drehen und Buchstaben tauschen | M2, M6 | **B** |
| **Landschaftsgestaltung** | ST1: N ≤ 1000, h ≤ 100 | Höhen zu Pyramide formen | M4, M6 | **C** |
| **Schaltkreis** | ST1 (20 P) | Ausdrücke auswerten, Parsing | M6 | **C** |
| **Wanderschilder** | — | Strassennetz = Graph | — | **D** |
| **Kuchenglasur** | — | Spiel gegeneinander, Turnier | — | **D** |
| **QRH** | — | Meta-Aufgabe zum Grader, keine Aufgabe | — | **D** |

**Trampolin ST1 ist der stärkste Fund dieser Runde.** Eine Sprungfolge von Hand
und dann im Programm nachvollziehen ist genau Strang B, und ST2 („welcher
Startpunkt ist der beste?") ist die vollständige Suche in Reinform.

---

## Erste Runde 2023/2024

| Aufgabe | Erste Teilaufgaben | Thema | Modul | |
|---|---|---|---|---|
| **Erntetag** | ST1 „Ist es überhaupt möglich?", n ≤ 1000 | Verteilbarkeit prüfen | M1 | **B** |
| **Kalender** | ST1: n, m ≤ 1000, k = 0 | Intervalle auf einer Zeitachse | M4 | **B** |
| **Ausstellung** | ST1: K = 1, N ≤ 1000 | Auswahl mit Bedingung pro Maler | M5 | **C** |
| **Pyramiden** | ST2: N ≤ 10, K = 3 | Konstruktives Verfahren mit Schrittlimit | M6 | **C** |
| **Kreuzfahrt** | ST1: M = 2, aber N ≤ 10⁶ | schon in ST1 grosse Schranke | M3 | **C** |
| **Labyrinth** | ST4: N ≤ 1000 | Fallen im Gang, wirkt graphartig | — | **D** |
| **Bewässerung** | — | ausdrücklich ungerichteter Graph | — | **D** |
| **Eselskarawane** | — | nicht auf Deutsch übersetzt | — | **D** |

Die schwächste Runde für uns. `Erntetag` ST1 ist eine saubere
Modellierungsaufgabe, sonst wenig.

---

## Erste Runde 2022/2023

| Aufgabe | Erste Teilaufgaben | Thema | Modul | |
|---|---|---|---|---|
| **Gleitschirmfliegen** | ST1: N = 2 · ST2: N ≤ 3000, Höhen fallend | von Punkt zu Punkt gleiten | M1–M2 | **A** |
| **Thermalquellen** | ST1: N ≤ 300, vier Eigenschaften | auswählen und vergleichen | M5 | **B** |
| **Rubiks Knauf** | ST1 „Anzahl Aufzieh-Schritte" (17 P) | Rechenvorschrift, Modulo | M1 | **C** |
| **Felsbrocken** | ST1 (10 P), Schranken nicht ausgewiesen | Muster auf Gitter legen | M6 | **C** |
| **Palatinusgruft** | ST1: N·M ≤ 1000 | Gitter, Ausgabe begrenzt | M6, **M7** | **C** |
| **Kartenspiel** | ST1: N ≤ 1000 → mit T = 100 zu langsam | Karten gegeneinander ausspielen | M5 | **C** |
| **Dada** | — | N−1 Durchgänge, zusammenhängend = Baum | **M7** | **D** |
| **Bäume** | — | Kreativitätsturnier | — | **D** |

`Gleitschirmfliegen` ST1 mit N = 2 ist ein guter erster Erfolg, und ST2 mit
fallenden Höhen ist eine echte Verschärfung, die trotzdem im Rahmen bleibt.

---

## Erste Runde 2021/2022

| Aufgabe | Erste Teilaufgaben | Thema | Modul | |
|---|---|---|---|---|
| **Gipfel** | ST1: N = 3 · ST2: N = 5 · ST3: N ≤ 10⁶ | Gipfelmuster in Höhen finden | M1–M2, M3 | **A** |
| **Greifer-Sortierung** | ST1 „Simuliere den Roboter", N ≤ 200 · ST2: N = 3 | Roboterbefehle ausführen, dann sortieren | **M7**, M2, M5 | **A** |
| **T-Shirts** | ST1 „Eine Maus" (5 P), Werte ≤ 100 · ST2: N ≤ 100 | Grösse in Intervall passend wählen | M1 | **A** |
| **Mäusetanz** | ST1: N = 3, T = 30 · ST2: alle gleich | Paare im Kreis bilden | M6 | **B** |
| **Zinnabbau** | ST1: N ≤ 100 · ST3: N ≤ 100 | Plattformen über Vorkommen | M2, **M7** | **B** |
| **Seilbahnen** | ST1 schon N ≤ 10⁶ | Höhenprofil, Sprünge | M3 | **C** |
| **Fährenumleitung** | — | Inseln und Verbindungen = Graph | — | **D** |

**Die ergiebigste Runde.** Drei A-Aufgaben, und `Gipfel` hat mit N = 3 → N = 5 →
N ≤ 10⁶ die didaktisch sauberste Leiter des ganzen Archivs — der Sprung in ST3
ist dieselbe Lektion wie bei `endurance`, nur an anderem Material.

---

## Erste Runde 2020/2021

| Aufgabe | Erste Teilaufgaben | Thema | Modul | |
|---|---|---|---|---|
| **Treppenlauf** | ST1: N = 1 · ST2: N = 2 · ST3: N ≤ 1000 | Dach zu Dach über die Strasse | M0, M2 · ST3/4 für M3 | **A** *(im Einsatz)* |
| **Bambus** | ST1: N = 3 · ST3: N ≤ 1000 | Stöcke auf Höhenmuster schneiden | M2 | **A** |
| **Geheimcode** | ST1: L ≤ 1000 Buchstaben | Wort entschlüsseln, Zeichenketten | M1–M2 | **B** |
| **Changifälle** | ST2: N ≤ 1000, Kreise | Geometrie, Wasserfallterrassen | M5 | **C** |
| **Muffins** | Schranken nicht ausgewiesen | Backvorgang planen | M6 | **C** |
| **Batterie flicken** | Schranken nicht ausgewiesen | unklar | ? | **C** |
| **Seerosen** | — | Sprünge zwischen Blättern, Suche im Graph | — | **D** |
| **Sate** | ST1: N ≤ 100, aber Kanten a→b | Spiesse und Teller = Graph | **M7** | **D** |

`Bambus` ST1 mit N = 3 ist ein weiterer sicherer Einstieg.

---

## Erste Runde 2019/2020

| Aufgabe | Erste Teilaufgaben | Thema | Modul | |
|---|---|---|---|---|
| **Schnäppchen** | ST1: genau zwei Angebote, Werte ≤ 100 | günstiger einkaufen | M1 | **A** |
| **Stickers** | ST1: N = 3, K = 1 · ST2: N ≤ 1000, K = 1 | möglichst wenige Kategorien sammeln | M2 | **A** |
| **Arc Match** | ST1: N ≤ 100 · ST3: N ≤ 10 | Bögen über einer Strasse, Kreuzungen zählen | M2 | **A** |
| **Regenwurm-Chirurgie** | ST1: N, M ≤ 100 · ST2: N, M ≤ 100 | Muster in einer Segmentfolge | M2, **M7** | **A** |
| **Reversi** | ST1: eine Runde · ST3: N ≤ 1000 | Steine umdrehen, Simulation | M2, **M7** | **B** |
| **Marathon** | — | **identisch mit `endurance`**, siehe Befund 2 | — | **D** |
| **Stofls Bergbahnen** | — | Schienennetz, kürzeste Wege | — | **D** |
| **SOIway** | — | U-Bahn-Netz = Graph | — | **D** |

Nach 2022 die zweitbeste Runde. Vier A-Aufgaben mit sehr kleinen ersten
Schranken.

---

## Erste Runde 2018

Nicht in der ursprünglichen Sichtungsliste, aber hier bereits im Einsatz: `sushi`
ST1/ST3 sind die Verkleidung in M1.

| Aufgabe | Erste Teilaufgaben | Thema | Modul | |
|---|---|---|---|---|
| **Sushi** | ST1: N = 2, S = 0 · ST3: N = 2, S ≤ 10³ | zwei Bestellarten vergleichen | M1 · ST2/4 für M5 | **A** *(im Einsatz)* |
| **Wagashi** | ST1: N ≤ 1000, eine Schleife | Summe aller aᵢ·cᵢ | M1 | **A** |
| **Mahjong** | ST1: N ≤ 100, Ausgabe M ≤ 100 000 | konstruktives Verfahren | M6 | **B** |
| **Käsepatrollie** | Schranken nicht ausgewiesen | Detektive auf Strassen = Graph | — | **D** |
| **Hanabi** | ST1 „Zwei Städte" | kürzeste Wege und DP | — | **D** |
| **Samurai** | ST2 = Kreativitätswettbewerb | Spielstrategie | — | **D** |

**Korrektur zum Modulplan.** `KONZEPT.md` führt `wagashi` ST1 als zweiten
M2-Anker. Das ist falsch einsortiert: Die Aufgabe ist eine einzelne Schleife über
alle Paare aᵢ, cᵢ — Modellierung, keine vollständige Suche. Sie gehört als
zusätzliche Übung nach **M1**. Mit T ≤ 100 und N ≤ 1000 sind es 10⁵ Schritte,
also völlig unkritisch.

---

## Empfehlung nach Modul

| Modul | Erste Wahl | Reserve |
|---|---|---|
| M1 Problemanalyse | `Schnäppchen` ST1 (2020), `T-Shirts` ST1 (2022) | `Wagashi` ST1 (2018), `Käsemaschine` ST1/2, `Erntetag` ST1 |
| M2 Vollständige Suche | `Gipfel` ST1/2 (2022), `Stickers` ST1/2 (2020) | `Bambus` ST1, `Arc Match` ST1, `Trampolin` ST2 |
| M3 Laufzeitdenken | `Gipfel` ST2 → ST3 (N = 5 → 10⁶) | `Treppenlauf` ST3/4, `Seilbahnen` |
| M4 Felder & lineare Technik | `Kalender` ST1 (2024) | `Landschaftsgestaltung` |
| M5 Sortieren & Suchen | `Thermalquellen` ST1 (2023) | `Ausstellung` ST1, `Kartenspiel` |
| M6 Konstruktive Verfahren | `Mahjong` ST1 (2018), `Mäusetanz` ST1/2 (2022) | `Greifer-Sortierung` ST2, `Pyramiden` ST2 |
| M7 Pseudocode & Simulation | `Greifer-Sortierung` ST1 (2022), `Trampolin` ST1 | die sechs Theorie-Teilaufgaben aus Befund 4 |

Für **M3** ist `Gipfel` der Glücksfall: Dieselbe Aufgabe geht von N = 5 auf
N ≤ 10⁶, ohne dass sich die Frage ändert. Das ist der Sprung, den `KONZEPT.md`
für M3 beschreibt, an einem zweiten Material — brauchbar als Verschärfung neben
`endurance` ST2 → ST3.

---

## Vorbehalt

Die Einstufungen beruhen auf dem Anriss der Aufgabenstellung und den
Schrankenblöcken, **nicht auf den vollständigen Aufgabentexten**. Sie taugen zur
Vorauswahl, nicht als Freigabe.

Bevor eine Aufgabe Anker oder Übung wird, gilt weiterhin: vollständigen Text
lesen, Modell aufstellen, Musterlösung gegen das offizielle Beispiel laufen
lassen. Genau so sind `cheeseparty`, `directions`, `sushi`, `endurance` und
`stairracing` in M1 und M2 gekommen.

Bei fünf Aufgaben liessen sich die Schranken nicht auswerten, weil die Seite sie
anders auszeichnet (`Batterie flicken`, `Muffins`, `Felsbrocken`,
`Wanderschilder`, `Käsepatrollie`). Diese sind konservativ eingestuft.

Technischer Hinweis für die Nachprüfung: Auf soi.ch liefert **jede Aufgaben-URL
einer Runde dieselbe Seite** mit allen Aufgaben. Der Aufgabenname im Pfad ist nur
ein Sprungziel. Wer eine einzelne Aufgabe abrufen will, bekommt sonst
unbemerkt den Text einer anderen.
