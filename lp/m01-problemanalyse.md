# M1 — Problemanalyse und Modellierung (Lehrperson)

**LP-Wert: mittel.** Der Baustein funktioniert solo, gewinnt aber deutlich durch
eine kurze gemeinsame Auswertung. Die drei Einsichten — „zähle, bevor du
rechnest", „prüf am Extremfall" und „prüfen ist rechnen plus vergleichen" —
sitzen erfahrungsgemäss erst, wenn sie einmal ausgesprochen wurden.

**Freischaltkriterium:** Die SuS schreiben zu einem unbekannten Aufgabentext ohne
Hilfe auf, was gegeben ist, was gesucht ist und welche Beziehung beides
verbindet — und prüfen ihr Modell an einem Extremfall, bevor sie programmieren.

**Voraussetzung:** M0. Der Ablauf mit Play-Knopf, `EINGABE` und Upload muss
sitzen, sonst geht die Lektion für Werkzeugfragen drauf.

---

## Neu an diesem Modul

**Umgestellt auf das Konzept-zuerst-Format** (August 2026). Die Modulseite
erklärt die drei Konzepte vorne; die Aufgaben stehen auf `uebungen.md`, mit je
drei Hinweisstufen. Was früher „Probier es selbst" war, ist jetzt die Zeitangabe
bei der einzelnen Aufgabe.

Die drei Konzepte sind hier **Gewohnheiten, keine Techniken**: Man erkennt nicht
an Signalen im Text, dass sie anzuwenden sind — sie gelten immer. Deshalb heisst
der entsprechende Abschnitt auf der Modulseite `Wann du es brauchst` und nennt
statt Erkennungssignalen die Anzeichen dafür, dass man den Schritt
übersprungen hat.

**Das ändert die Rolle der LP.** Im alten Format war die Hürde, überhaupt auf
Stofl zu kommen. Jetzt steht er auf der Seite. Die neue Hürde: Wer die Erklärung
gelesen hat, glaubt zu können und überspringt genau die Gewohnheit, um die es
geht. Nicht fragen „habt ihr das verstanden", sondern eine Aufgabe geben und
zusehen, ob jemand vor dem Tippen etwas aufschreibt.

**Aufgabennamen.** Das Material verwendet ab jetzt durchgehend die deutschen
Namen von soi.ch: **Käsefest** (`cheeseparty`), **Wegbeschreibung**
(`directions`), **Ausdauer** (`endurance`). Vorher standen dort die englischen
Kürzel aus der Adresszeile — wer den Link anklickte, sah einen anderen Namen als
auf der Kursseite.

---

## Vorbereitung

- Das Käsefest selbst lösen, beide Teilaufgaben. Dauert fünf Minuten und du
  kennst danach die Stolperstellen.
- Klären, ob die SuS ihre soi.ch-Accounts noch haben. Die Übungen geben Punkte,
  das motiviert — aber nur, wenn der Login funktioniert.
- Die Namensverwirrung im Archiv kennen: Die Übung *Sushi* liegt in der Runde
  2018 unter „First Round", das ist nach heutiger Zählung die Zweite Runde. Auf
  der Übungsseite steht ein Hinweis dazu, trotzdem fragen erfahrungsgemäss
  einige nach.

---

## Ablauf-Empfehlung

Die 20 Minuten „Probier es selbst" wirklich abwarten. Das Käsefest sieht so
einfach aus, dass die Versuchung gross ist, sofort die Formel an die Tafel zu
schreiben — dann ist der Baustein wertlos.

Produktiv ist das Gegenteil: **die falschen Ergebnisse einsammeln.** Wer 120
herausbekommt, hat Stofl vergessen; wer 78 herausbekommt, die Eltern. Beide
Fehler an die Tafel, dann die Frage: „Woran hätte man das merken können, ohne
das Beispiel zu kennen?" Von dort führt der Weg direkt zur Probe am Extremfall.

Teilaufgabe 2 erst freigeben, wenn Teilaufgabe 1 bei den meisten läuft. Der
Aha-Effekt hängt daran, dass die Rechnung schon dasteht.

---

## Typische Fehlvorstellungen

**„Stofl gehört nicht dazu, er ist ja der Gastgeber."**
Die häufigste Variante, und sie ist nicht dumm — im Aufgabentext steht es
beiläufig. Genau darum eignet sich die Aufgabe: Der Fehler liegt im Lesen, nicht
im Rechnen.

**„Eine Familie sind K Mäuse."**
Die zweite Zählfalle. Wer beide Fehler macht, kommt bei `4 3 6` auf 72 und ist
weit weg — das ist immerhin auffällig.

**„Teilaufgabe 2 ist eine ganz neue Aufgabe."**
Der eigentliche Denkfehler des Moduls. Die SuS suchen nach einer Umkehrung der
Rechnung, statt vorwärts zu rechnen und zu vergleichen. Wenn du einen Satz aus
dieser Lektion wiederholst, dann diesen: Prüfen ist rechnen und vergleichen.

**„Mein Programm hat das Beispiel geschafft, also stimmt es."**
Die Widerlegungsaufgabe zielt genau darauf. Sie lohnt sich auch als
Fünf-Minuten-Diskussion im Plenum, wenn die Zeit für die schriftliche Bearbeitung
fehlt.

**„Das Ausgabeformat ist immer `Case #i:`."**
Das Käsefest hat keines, die Wegbeschreibung schon. Wer M0 verinnerlicht
hat, überträgt es falsch. Das ist ein produktiver Fehler — er zeigt, dass
Formate gelesen und nicht gewohnheitsmässig übernommen werden.

---

## Diagnosefragen

- „Wie viele Mäuse sind an der Party, wenn N = 0 ist?"
- „Du hast Teilaufgabe 1. Wie viel Arbeit ist Teilaufgabe 2 noch?"
- „Dein Programm liefert beim Beispiel das Richtige. Warum ist es trotzdem
  möglich, dass du null Punkte bekommst?"
- „Woher weisst du, ob deine Ausgabe mit `Case #0:` beginnen muss?"
- Bei der Wegbeschreibung: „Was passiert, wenn Stofl sich an mehr erinnert,
  als Binna aufgeschrieben hat?"

---

## Differenzierung

**Einstiegsspur:** Käsefest Teilaufgabe 1 und 2, das sind bereits volle 100
Punkte. Wer nur das schafft, hat den Baustein bestanden.

**Kernspur:** dazu die Wegbeschreibung, alle drei Teilaufgaben. Der Hinweis,
dass ein einziges Programm alle drei löst, ist hier der Lerngewinn — nicht
die Punkte.

**Vertiefung:** Sushi Teilaufgabe 1 und 3 plus die Widerlegungsaufgabe
schriftlich. Wer Sushi schnell hat, kann versuchen, Teilaufgabe 2 zu knacken —
sie führt auf das Sortieren und damit auf M5. Ein Vorgriff ist unproblematisch,
solange klar ist, dass die Lösung dort systematisch kommt.

---

## Zeitbedarf

Zwei Lektionen. Das Käsefest samt Auswertung füllt die erste, die Übungen die
zweite. Bei knapper Zeit fällt Sushi weg, nicht die Widerlegungsaufgabe.
