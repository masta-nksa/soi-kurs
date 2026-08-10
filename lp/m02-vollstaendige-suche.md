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

## Vorbereitung

- Endurance Teilaufgabe 1 und 2 selbst lösen. Achte darauf, wie stark der Reiz
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

**Basisspur:** Endurance Teilaufgabe 1 und 2. Das sind 40 Punkte und reicht für
den Baustein.

**Kernspur:** dazu Treppenlauf Teilaufgabe 2 und die allgemeine Umsetzung. Der
Gewinn ist nicht die Punktzahl, sondern die Einsicht, dass dieselbe Denkfigur
zwei völlig verschiedene Aufgaben löst.

**Vertiefung:** die Schätzaufgabe und die Verkleidung schriftlich, mit sauber
formulierter Invariante. Wer damit fertig ist, kann versuchen, Endurance
Teilaufgabe 3 zu knacken — das ist M3 und darf ruhig vorgegriffen werden.

---

## Hinweis zum Aufgabenmaterial

Der Modulplan in `KONZEPT.md` nennt als zweiten Anker `wagashi` Teilaufgabe 1 aus
der Runde 2018. Die Aufgabenseite ist unter diesem Namen nicht abrufbar; die
Übung wurde durch Treppenlauf Teilaufgabe 2 ersetzt, das M0 ohnehin schon als
Selbsttest vormerkt. Falls `wagashi` erreichbar wird, passt es als zusätzliche
Variation.

---

## Zeitbedarf

Zwei Lektionen. Endurance samt Auswertung füllt die erste, Treppenlauf und die
Schätzaufgabe die zweite. Bei knapper Zeit fällt die Verkleidung weg, nicht die
Schätzaufgabe — sie trägt den Übergang nach M3.
