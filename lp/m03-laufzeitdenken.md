# M3 — Laufzeitdenken (Lehrperson)

**LP-Wert: hoch.** Anders als in M1 und M2 ist der Kern hier keine Einsicht,
sondern eine **Gewohnheit**: erst schätzen, dann programmieren. Gewohnheiten
entstehen nicht durch Lesen. Ohne jemanden, der bei jeder Aufgabe „wie lange
dauert das?" fragt, fällt die Klasse in „ausprobieren und schauen" zurück.

**Freischaltkriterium:** Die SuS rechnen zu einer ihnen unbekannten Teilaufgabe
aus Schranke, Komplexität und Testfallzahl eine Dauer aus und entscheiden
begründet, ob sie damit einreichen — **bevor** sie programmieren.

**Voraussetzung:** M2. Die O(N²)-Lösung von Endurance muss stehen, sonst gibt es
nichts zu verbessern.

---

## Vorbereitung

- Endurance Teilaufgabe 3 selbst lösen und dabei die Zeit stoppen.
- **Die Zahlen kennen**, sie kommen in jeder Lektion vor: Python schafft rund
  10⁷ Schritte pro Sekunde; 10⁸ sind zwölf Sekunden; ab 10⁹ wird es unmöglich.
- Eine grosse Eingabedatei vorbereiten, um sie zeigen zu können. Der Härtefall
  von Endurance ST3 sind 20 MB und 10 Millionen Zahlen — das beeindruckt mehr
  als jede Tabelle.
- Gerüststufe 2 ab hier: `vorlage-stufe2.py`. Das Einlesen eines Testfalls
  schreiben die SuS erstmals selbst. Bei Endurance ist das Format dasselbe wie in
  M2, der Umstieg ist also bewusst sanft gelegt.

---

## Das Wichtigste: unser Zeitbudget ist ungewöhnlich

Dieser Punkt verdient Vorbereitung, weil er allem widerspricht, was die SuS
finden, wenn sie nachschlagen.

In der Wettbewerbsprogrammierung gilt üblicherweise ein Zeitlimit von ein bis
zwei Sekunden, und der Grader bricht ab. **Bei uns nicht.** Wir laden eine
Ausgabedatei hoch; niemand misst die Laufzeit. Die einzige Uhr sind die fünf
Minuten zwischen Download und Upload.

Daraus folgt die Leitlinie des Moduls:

> Kleine Unterschiede sind egal. Grosse sind tödlich.

Konkret: Zwölf Sekunden Rechenzeit sind bei uns völlig in Ordnung und geben
volle Punkte. Zwischen 10⁶ und 10⁸ Schritten liegt didaktisch nichts, zwischen
10⁸ und 10¹² liegt alles.

Das ist auch der Grund, warum Treppenlauf Teilaufgabe 3 in den Übungen steht: Die
SuS erwarten dort ein Scheitern und bekommen 25 Punkte. Diese Überraschung ist
beabsichtigt und trägt die Botschaft besser als jede Ermahnung.

---

## Ablauf-Empfehlung

Drei Lektionen.

**Erste Lektion — schätzen, dann lösen.** Die 30 Minuten „Probier es selbst"
haben zwei Aufträge, und der erste ist der wichtige. Sammle die Schätzungen ein,
**bevor** jemand programmiert. Erfahrungsgemäss vergisst die Hälfte den Faktor
T = 100; das an der Tafel zu korrigieren ist wirksamer als jeder Hinweis im
Material.

**Zweite Lektion — Treppenlauf.** Schätzen lassen, dann Teilaufgabe 3 einreichen.
Die zwölf Sekunden gemeinsam abwarten, das prägt sich ein. Teilaufgabe 4 nur
diagnostizieren, nicht lösen — die Technik gehört zu M4.

**Dritte Lektion — versteckte Bremsen.** Die Messübung läuft am Rechner und
funktioniert auch in Zweiergruppen. Danach die Schätzrunde, gerne im Plenum.

Wenn die Zeit knapp wird, fällt die dritte Lektion weg. Dann aber wenigstens
`pop(0)` und `in liste` kurz zeigen — beide tauchen in späteren Modulen wieder
auf.

---

## Typische Fehlvorstellungen

**„Der Faktor 100 für die Testfälle ist doch egal."**
Die häufigste Rechenlücke. Er entscheidet zwischen 10⁶ und 10⁸ und damit
zwischen einer Zehntelsekunde und zwölf Sekunden. Am Ende der Lektion sollte
niemand mehr eine Laufzeit ohne T angeben.

**„Zwölf Sekunden sind zu langsam."**
Der Reflex aus jedem Tutorial im Netz, und bei uns falsch. Wer ihn hat, sucht
nach besseren Lösungen, wo längst Punkte zu holen wären.

**„Zu langsam heisst, meine Lösung ist falsch."**
Nein. Sie ist korrekt und passt nur nicht zu dieser Schranke. Dieselbe Lösung
holt in der Teilaufgabe darunter volle Punkte. Das ist die Fortsetzung der
Brute-Force-Botschaft aus M2.

**„O(N) ist immer gut."**
Nicht, wenn N Zahlen einzulesen schon zu lange dauert. Zeile d der Schätzrunde
zielt genau darauf. Bei Endurance ST3 gehen 72 % der Zeit ins Einlesen — das
lässt sich am Rechner vorführen und überrascht regelmässig.

**„Eine kurze Zeile ist eine billige Zeile."**
`liste.pop(0)` und `if x in liste` sehen aus wie ein Schritt und sind N. Wer das
einmal gemessen hat, fragt künftig nach.

---

## Diagnosefragen

- „Wie viele Schritte macht dein Programm insgesamt? Mit Testfällen."
- „Wie lange dauert das? Sag mir eine Zahl in Sekunden."
- „Deine Lösung braucht zwölf Sekunden. Was tust du?"
- „Woran erkennst du an den Limits, dass eine Teilaufgabe eine neue Idee
  braucht?"
- „Wo steckt in diesem Programm eine Schleife, die man nicht sieht?"
- Nach dem Download: „Wie gross ist die Eingabedatei?"

---

## Differenzierung

**Basisspur:** Endurance Teilaufgabe 3. Zusammen mit M2 sind das 60 Punkte auf
dieser Aufgabe.

**Kernspur:** dazu Treppenlauf Teilaufgabe 3 einreichen und Teilaufgabe 4
diagnostizieren. Der Lerngewinn ist die Entscheidung „einreichen oder
weiterdenken", nicht die Punktzahl.

**Vertiefung:** die Messübung mit eigenen Zahlen erweitern — etwa
`liste.insert(0, x)` oder das Zusammenbauen langer Zeichenketten mit `+` in einer
Schleife. Beide haben dasselbe Problem und tauchen in eigenem Code der SuS auf.
Wer schnell fertig ist, kann Treppenlauf Teilaufgabe 4 angehen; das greift auf M4
vor und ist unproblematisch.

---

## Zum set

Die Musterlösung führt `set` ein — das erste Mal im Kurs, dass eine
Datenstruktur vorkommt. Das ist beabsichtigt: Sie wird nicht als Thema
eingeführt, sondern weil ein Problem sie erzwingt. Genau so sind Datenstrukturen
im Konzept vorgesehen.

Halte es knapp. Nötig ist nur: `set()` statt `[]`, `add` statt `append`, und
`in` ist darauf schnell. Alles Weitere kommt, wenn es gebraucht wird.

---

## Zeitbedarf

Drei Lektionen, komprimierbar auf zwei. Bei 15 Lektionen insgesamt bleibt M3
trotzdem vollständig — es ist die Voraussetzung dafür, dass die Subtask-Sprünge
in M4 und M5 überhaupt erklärbar sind.
