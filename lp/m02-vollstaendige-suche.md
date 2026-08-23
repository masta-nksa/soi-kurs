# M2 — Vollständige Suche (Lehrperson)

**LP-Wert: mittel.** Das Programmieren läuft solo. Was Begleitung braucht, ist
die Haltung zur Brute Force — dass sie richtig ist und nicht geduldet wird. Diese
Botschaft kommt aus dem Material heraus schwächer an als von dir.

**Freischaltkriterium:** Die SuS beantworten zu einem neuen Problem selbständig
die drei Fragen — was ist eine Möglichkeit, wie zähle ich alle auf, woran erkenne
ich die beste — und schätzen ab, ob die Aufzählung in Python durchläuft.

**Voraussetzung:** M1. Wer noch kein Modell aus einem Text ziehen kann, scheitert
hier an der ersten Frage, nicht an der Suche.

---

## Neu an diesem Modul

**Umgestellt auf das Konzept-zuerst-Format** (August 2026). Drei Konzeptblöcke
statt einer durchlaufenden Erklärung:

- **Vollständige Suche** — die drei Fragen, die Analogie, die Erkennungssignale
- **Die Invariante** — vorher ein Unterabschnitt, jetzt eigenständig. Sie wird
  in M3 gebraucht und in den Übungen an einem zweiten Problem eingefordert.
- **Teilpunkte mitnehmen** — die Haltung zur Brute Force, jetzt als benanntes
  Konzept mit eigener Rechnung statt als Randbemerkung.

Der dritte Block ist der wichtigste für die Punktzahl der Klasse und derjenige,
der aus dem Material heraus am schwächsten wirkt. Sag ihn laut.

**Neue dritte Trockenübung.** Die Abkürzung „höchster links, höchster rechts"
wird jetzt systematisch widerlegt. Die Zahlen dazu sind nachgerechnet: Bei N = 2
scheitert die naive Fassung nur bei Gleichständen — und genau so ein Fall ist
Testfall 0 der Aufgabenstellung. Mit lauter verschiedenen Höhen fällt sie bei
N = 2 **nie** auf, bei N = 3 dagegen schon.

Das ist der beste Aufhänger des Moduls für die Frage, was ein Test eigentlich
beweist. Die ältere Fassung des Materials behauptete, bei N = 2 lasse sich die
Abkürzung „kaum widerlegen" — das war zu schwach formuliert.

**Musterlösungen sind jetzt vollständige Programme.** Vorher standen dort
Fragmente ohne Leser mit dem Hinweis „Kopf wie in M1". Wer sie kopierte, bekam
einen NameError.

**Aufgabennamen.** `endurance` heisst auf soi.ch **Ausdauer**. Das Material
verwendet ab jetzt durchgehend die deutschen Namen.

---

## Vorbereitung

- Ausdauer Teilaufgabe 1 und 2 selbst lösen. Achte darauf, wie stark der Reiz
  ist, bei N = 3 eine Fallunterscheidung zu schreiben — genau daran hängt die
  Lektion.
- Treppenlauf kennen die SuS aus M0. Teilaufgabe 2 setzt dort direkt an.
- Für die Schätzaufgabe die Zahl 10⁶ bis 10⁷ Schritte pro Sekunde parat haben.
  Sie kommt ab hier in jedem Modul vor.

---

## Ablauf-Empfehlung

**Teilaufgabe 1 nicht überspringen, auch wenn sie trivial wirkt.** Der Sinn ist
der Bruch danach: Wer bei N = 3 von Hand unterscheidet, steht bei N ≤ 100 vor
einem Neuanfang. Wer allgemein programmiert, hat beide Teilaufgaben auf einmal.

Beides an der Tafel nebeneinanderstellen, sobald die ersten fertig sind. Die
Frage dazu: „Wer von euch musste für Teilaufgabe 2 noch einmal von vorn
anfangen?" Das sitzt besser als jede Vorabwarnung.

Die Schätzaufgabe aus den Übungen eignet sich gut fürs Plenum, wenn die Zeit für
Einzelarbeit knapp wird. Sie dauert fünf Minuten und ist die Brücke zu M3 — ohne
sie wirkt M3 wie ein Themenwechsel statt wie eine Antwort.

---

## Typische Fehlvorstellungen

**„Brute Force ist die Lösung für Leute, die es nicht besser können."**
Die wichtigste Korrektur dieses Moduls. Teilaufgabe 1 und 2 sind 40 von 100
Punkten, und sie zählen genauso wie die schweren. Wer auf die perfekte Lösung
wartet, reicht am Ende gar nichts ein. Sag das explizit — im Material steht es,
aber geglaubt wird es erst, wenn es jemand ausspricht.

**„Ich probiere halt alles durch" ohne System.**
Der Unterschied zwischen Ausprobieren und vollständiger Suche ist, dass Letztere
jede Möglichkeit **genau einmal** betrachtet. Wer ohne Schema sucht, vergisst
Fälle oder zählt doppelt und merkt es nicht. Die Frage „woher weisst du, dass du
keinen vergessen hast?" bringt das schnell an die Oberfläche.

**Die dritte Schleife.**
Sehr häufig: erst beide Enden festlegen, dann den Abschnitt noch einmal auf
Löcher prüfen. Das ist O(N³) und bei T = 100 zu langsam. Didaktisch wertvoll,
weil der Fehler nicht im Denken liegt, sondern in einer weggeworfenen
Information — die kürzere Prüfung war schon gemacht.

**Der Startwert der besten Länge.**
Wer mit 1 statt 0 startet oder den Fall „nur Löcher" nicht bedenkt, bekommt bei
`1 1 1` ein falsches Ergebnis. Kommt im Beispiel der Aufgabenstellung nicht vor —
guter Anlass, an die Probe am Extremfall aus M1 zu erinnern.

---

## Diagnosefragen

- „Was ist bei dieser Aufgabe eine Möglichkeit?"
- „Woher weisst du, dass du keine Möglichkeit doppelt gezählt hast?"
- „Wie viele Abschnitte hat eine Strasse der Länge 100? Und wie lange braucht
  dein Programm dafür?"
- „Deine Lösung schafft Teilaufgabe 2, aber nicht 3. Was lädst du hoch?"
- „Was ist die Antwort, wenn die ganze Strasse aus Löchern besteht?"

---

## Differenzierung

**Basisspur:** Ausdauer Teilaufgabe 1 und 2. Das sind 40 Punkte und reicht für
den Baustein.

**Kernspur:** dazu Treppenlauf Teilaufgabe 2 und die allgemeine Umsetzung. Der
Gewinn ist nicht die Punktzahl, sondern die Einsicht, dass dieselbe Denkfigur
zwei völlig verschiedene Aufgaben löst.

**Vertiefung:** die Schätzaufgabe und die Verkleidung schriftlich, mit sauber
formulierter Invariante. Wer damit fertig ist, kann versuchen, Ausdauer
Teilaufgabe 3 zu knacken — das ist M3 und darf ruhig vorgegriffen werden.

---

## Spoiler-Risiko: der Anker steht im Archiv

**`endurance` ist dieselbe Aufgabe wie `marathon` aus der Runde 2019/2020** —
identische Teilaufgabenleiter, für die Vorrunde neu aufgelegt. Wer im Archiv
stöbert oder nach „SOI marathon" sucht, findet Lösungen zu genau dem Problem, an
dem M2 seine Entdeckung aufhängt.

Das ist nicht zu verhindern, aber zu entschärfen: Verweise im Unterricht auf die
Hinweisleiter, nicht aufs Archiv, und gib die Übungsaufgaben erst frei, wenn der
Anker gelöst ist. Wer die Lösung nachschlägt, verliert nichts an Punkten und
alles an Übung — das ist ein Satz, den die SuS von dir hören sollten, nicht von
der Webseite.

---

## Laufzeit: unser Budget ist ungewöhnlich

Rechne damit, dass die Zahlen im Modul Widerspruch auslösen. Die vollständige
Suche läuft bei uns **viel weiter, als aus Wettbewerbsberichten bekannt ist**,
weil wir nur die Ausgabedatei hochladen und niemand die Laufzeit misst. Zwölf
Sekunden Rechenzeit sind bei uns völlig in Ordnung.

Die Zahl, die stattdessen zählt, sind die fünf Minuten zwischen Download und
Upload. Wer das verinnerlicht, trifft in M3 die richtigen Entscheidungen: Kleine
Unterschiede sind egal, grosse sind tödlich. Ein Zwischending gibt es kaum.

---

## Hinweis zum Aufgabenmaterial

Der Modulplan in `KONZEPT.md` nennt als zweiten Anker `wagashi` Teilaufgabe 1 aus
der Runde 2018. Verwendet wird stattdessen Treppenlauf Teilaufgabe 2, und zwar
aus einem inhaltlichen Grund: `wagashi` ST1 ist die Summe aller aᵢ·cᵢ, also eine
einzige Schleife. Das ist eine saubere Modellierungsaufgabe — welche Grössen
gehören paarweise zusammen? — aber keine vollständige Suche. Sie passt nach M1,
nicht nach M2.

Als zusätzliche Übung in M1 oder als Aufwärmaufgabe ist sie gut brauchbar. Die
Schranken (N ≤ 1000, T ≤ 100) sind für eine einzelne Schleife unkritisch.

Die vollständige Sichtung des Archivs steht in `lp/kuratierung.md`.

---

## Zeitbedarf

Zwei Lektionen. Ausdauer samt Auswertung füllt die erste, Treppenlauf und die
Schätzaufgabe die zweite. Bei knapper Zeit fällt die Verkleidung weg, nicht die
Schätzaufgabe — sie trägt den Übergang nach M3.
