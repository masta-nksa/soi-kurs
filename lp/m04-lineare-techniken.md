# M4 — Felder und lineare Techniken (Lehrperson)

**LP-Wert: mittel.** Die Entdeckung „das linke Ende muss nie zurück" trägt die
Hinweisleiter gut. Begleitung braucht der Laufzeitbeweis: dass zwei
verschachtelte Schleifen O(N) sein können, glaubt kaum jemand beim ersten Hören,
und im Material steht es zwar, überzeugt aber erst im Gespräch.

**Freischaltkriterium:** Die SuS lösen ein Fensterproblem mit zwei Zeigern und
können begründen, **warum** das linke Ende nie zurückwandern muss.

**Voraussetzung:** M3. Ohne Laufzeitdenken ist der Sprung von Teilaufgabe 4 auf 5
nicht motivierbar — bei N ≤ 100 wäre der Zweizeiger unnötig.

---

## Neu an diesem Modul

**Umgestellt auf das Konzept-zuerst-Format** (August 2026). Zwei Konzeptblöcke,
**Präfixsummen** und **Zweizeiger und Fenster**, beide mit eigener Analogie:
Kilometerzähler beziehungsweise Klassenbuch.

Die Umformulierung „bis zu K Löcher reparieren" = „höchstens K Löcher" ist
kein eigener Block mehr, sondern steht im Abschnitt „Worum es geht" des
Zweizeigers. Sie ist eine Anwendung von M1, kein neues Konzept — trotzdem bleibt
sie der wichtigste Moment der ersten Lektion.

**Die Ablauftabelle des Zweizeigers ist neu und nachgerechnet.** Sie zeigt für
`0 1 0 0 1 1 0 1 0 0 1 0` mit K = 3 den Zustand am Ende jedes Durchlaufs. Zwei
Dinge werden daran sichtbar, die im Fliesstext untergingen: dass das linke Ende
nur vorwärts geht (0 → 2 → 5, insgesamt fünf Schritte), und dass die
Löcherzahl nie über K steigt — die Invariante zum Anfassen.

Eignet sich gut fürs Plenum: mit zwei Fingern auf der Zahlenreihe mitwandern
und die Tabelle Zeile für Zeile füllen lassen.

**Neue Selbstcheck-Frage 5** zur Monotonie: Der Zweizeiger funktioniert *nicht*,
wenn negative Werte erlaubt sind. Diese Voraussetzung wurde vorher nur nebenbei
erwähnt und ist der häufigste Grund, warum das Verfahren später falsch
angewendet wird.

**Trockenübung 1 hat eine fünfte Frage** — ab wie vielen Fragen sich die
Vorbereitung lohnt. Antwort: schon ab zwei. Das ist ein guter Vergleichspunkt zu
M5, wo dieselbe Schwelle beim Sortieren bei rund zwanzig liegt.

---

## Vorbereitung

- Ausdauer Teilaufgabe 4 und 5 selbst lösen. Der Zweizeiger ist kurz, aber die
  Reihenfolge im Schleifenrumpf ist heikel; schreib ihn einmal von Hand.
- Treppenlauf Teilaufgabe 4 durchrechnen. Die Umformung
  `a[i] + b[j] + |i−j|` in zwei Fälle ist der anspruchsvollste Schritt des
  Moduls und lohnt eigene Vorbereitung.
- Gerüststufe 2 weiterhin. **Das Eingabeformat ändert sich**: pro Testfall stehen
  jetzt zwei Zahlen vor der Liste. Genau daran zeigt sich, ob der Umstieg in M3
  sass.

---

## Ablauf-Empfehlung

Drei Lektionen.

**Erste Lektion — die Umformulierung.** Der wichtigste Moment kommt vor dem
Programmieren: „Bis zu K Löcher reparieren" heisst „ein Abschnitt mit höchstens K
Löchern". Wer das ausspricht, hat die Aufgabe auf die bekannte zurückgeführt.

Lass den Satz an der Tafel formulieren, bevor jemand tippt. Erfahrungsgemäss
suchen sonst mehrere danach, **welche** Löcher zu reparieren wären — eine
Entscheidung, die es gar nicht gibt.

Danach Teilaufgabe 4 lösen, mit welcher Methode auch immer. Brute Force ist hier
richtig und gibt 20 Punkte.

**Zweite Lektion — der Zweizeiger.** Erst wenn Teilaufgabe 5 auf dem Tisch liegt,
lohnt sich das Fenster. Die Hinweisleiter führt hin; Hinweis 3 ist der
Angelpunkt.

Ein Vorschlag fürs Plenum: Das Fenster von Hand an der Tafel wandern lassen, mit
zwei Fingern auf der Zahlenreihe `0 1 0 0 1 1 0 1 0 0 1 0` und K = 3. Nach zwei
Minuten sieht die Klasse, dass der linke Finger nie zurückgeht.

**Dritte Lektion — Treppenlauf und der Beweis.** Treppenlauf Teilaufgabe 4 ist
anspruchsvoll und schliesst die Klammer aus M3, wo die Aufgabe nur diagnostiziert
wurde. Der Laufzeitbeweis eignet sich gut fürs Plenum.

---

## Typische Fehlvorstellungen

**„Ich muss entscheiden, welche Löcher ich repariere."**
Die Fehlvorstellung, die den Einstieg blockiert. Sobald der Abschnitt feststeht,
ist die Auswahl erzwungen: alle Löcher darin. Ein Satz an der Tafel räumt das
aus.

**Das `+ 1` bei der Fensterlänge.**
`rechts - links` statt `rechts - links + 1`. Klassiker, und er fällt beim
mitgelieferten Beispiel sofort auf — ein Grund mehr, lokal zu testen.

**Falsche Reihenfolge im Schleifenrumpf.**
Erst aufnehmen, dann verkleinern, dann messen. Wer vor dem Verkleinern misst,
misst ein ungültiges Fenster. Der Fehler ist unauffällig, weil das Ergebnis oft
trotzdem fast stimmt.

**„Zwei verschachtelte Schleifen sind immer O(N²)."**
Der Kern der dritten Lektion. Die Antwort ist, über die Bewegungen der Zeiger zu
zählen statt über die Schleifen. Wer es einmal sauber aufgeschrieben hat, hat ein
Argument gewonnen, das in der Informatik oft wiederkommt.

**Verrutschen bei den Präfixsummen.**
`praefix[b] - praefix[a]` statt `praefix[b + 1] - praefix[a]`. Gegenmittel: immer
an einem Beispiel mit drei Elementen von Hand nachrechnen, nie im Kopf.

---

## Diagnosefragen

- „Welche Bedingung muss ein Abschnitt erfüllen? Sag es ohne das Wort
  ‚reparieren'."
- „Warum muss das linke Ende nie nach links?"
- „Deine Lösung hat zwei verschachtelte Schleifen. Warum ist sie trotzdem O(N)?"
- „Was liefert dein Programm bei K = 0? Und was sollte es liefern?"
- „Wie viele Schritte kostet eine Bereichsfrage mit Präfixsummen? Und wie viele
  ohne?"

---

## Differenzierung

**Basisspur:** Ausdauer Teilaufgabe 4 mit Brute Force. 20 Punkte, und die
Umformulierung ist trotzdem geübt.

**Kernspur:** der Zweizeiger und damit Teilaufgabe 4 und 5. Das ist das
eigentliche Modul.

**Vertiefung:** Treppenlauf Teilaufgabe 4 und der Laufzeitbeweis schriftlich. Wer
damit fertig ist, kann die beiden Lösungen gegeneinander testen lassen — die
alte aus M2 gegen die neue — und so das Vorgehen „zwei Programme vergleichen"
einüben. Das ist eine Technik, die später mehr wert ist als jede einzelne
Aufgabe.

---

## Was hier zusammenläuft

M4 schliesst den Bogen über die Vorrunde. Nach diesem Modul sind auf Ausdauer
alle 100 Punkte erreichbar und auf Treppenlauf ebenfalls — mit Lösungen, die die
SuS über vier Module hinweg selbst entwickelt haben.

Das ist ein guter Moment, um genau das sichtbar zu machen. Die Aufgabe hat sich
nie geändert; geändert haben sich die Schranken, und mit ihnen die Ideen.

---

## Zeitbedarf

Drei Lektionen. Bei 15 Lektionen insgesamt auf zwei kürzen: dann Treppenlauf
Teilaufgabe 4 streichen und den Laufzeitbeweis ins Plenum verlegen. Der
Zweizeiger selbst darf nicht wegfallen — er ist der Grund, warum die Vorrunde
vollständig lösbar wird.
