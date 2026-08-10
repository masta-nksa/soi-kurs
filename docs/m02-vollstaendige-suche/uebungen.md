# M2 — Übungen

Eine Aufgabe mit Grader, dazu drei Übungen auf Papier. Die Papierübungen sind
kein Ersatz — sie üben genau das, was beim blossen Einreichen wegfällt.

---

## Variation — Treppenlauf, Teilaufgabe 2

**[Treppenlauf, Teilaufgabe 2](https://soi.ch/contests/2021/round1/stairracing/)**
aus der Runde 2021. Teilaufgabe 1 kennst du schon aus M0.

Auf jeder Seite der Strasse steht jetzt nicht mehr ein Wolkenkratzer, sondern
**zwei**. Binna läuft auf einem Dach los, hinunter, ein Stück die Strasse
entlang und auf einem Dach der anderen Seite wieder hinauf. Gesucht ist die
**längstmögliche** Strecke.

Dieselbe Denkfigur wie bei Endurance, andere Oberfläche: Statt Abschnitten zählst
du Kombinationen auf. Stell dir die drei Fragen aus dem Konzept, bevor du
programmierst — vor allem die erste: Was ist hier eine Möglichkeit?

!!! tip "Lies das Eingabeformat genau"
    Pro Testfall kommt zuerst N, dann die Höhen der einen Strassenseite, dann die
    der anderen. Die Strecke entlang der Strasse hängt davon ab, wie weit die
    beiden gewählten Wolkenkratzer auseinanderstehen.

??? tip "Eine Abkürzung, die nicht funktioniert"
    Naheliegend wäre: den höchsten Wolkenkratzer links nehmen, den höchsten
    rechts, fertig.

    Bevor du das programmierst, such ein Gegenbeispiel auf Papier. Mit zwei
    Wolkenkratzern pro Seite wirst du keines finden — nimm drei. Denk daran, dass
    zur Höhe noch etwas dazukommt.

    Dass eine Abkürzung bei kleinen Beispielen hält und trotzdem falsch ist, ist
    kein Zufall, sondern der Normalfall. Deshalb sucht man das Gegenbeispiel,
    bevor man programmiert.

---

## Verschärfung — dieselbe Lösung, aber allgemein

Für Teilaufgabe 2 könntest du die vier Kombinationen von Hand hinschreiben. Tu
es nicht.

Schreib dein Programm so, dass es für **beliebiges N** funktioniert: zwei
Schleifen über beide Strassenseiten, kein fest eingebautes „vier Fälle".

Prüf es lokal mit einem selbst gebauten Beispiel, bei dem N = 5 ist. Die Antwort
musst du dafür von Hand ausrechnen — das ist Teil der Übung. Hochladen brauchst
du nichts mehr, die Punkte hast du schon.

Der Aufwand lohnt sich zweimal: Eine allgemeine Lösung ist meist kürzer als die
Fallunterscheidung, und sie ist der Ausgangspunkt für die nächste Übung.

---

## Laufzeit-Schätzung — wo hört das auf?

Papier und Bleistift. Kein Programm, kein Upload.

Du hast jetzt zwei allgemeine Lösungen: eine für Endurance mit zwei Schleifen
über die Strasse, eine für Treppenlauf mit zwei Schleifen über die
Strassenseiten. Beide haben mehr Teilaufgaben, als du gelöst hast.

Schätze für jede der folgenden Teilaufgaben, wie viele Schritte deine Lösung
ungefähr braucht, und entscheide dann, ob das in Python durchläuft. Denk daran:
**T = 100 Testfälle**, und Python schafft 10⁶ bis 10⁷ Schritte pro Sekunde.

| Aufgabe | Teilaufgabe | Schranke |
|---|---|---|
| Endurance | 3 | N ≤ 100 000 |
| Treppenlauf | 3 | N ≤ 1 000 |
| Treppenlauf | 4 | N ≤ 100 000 |

Schreib zu jeder Zeile eine Zahl und ein Urteil hin. Erst danach vergleichst du
mit der Lösung.

Diese Schätzung ist keine Trockenübung im abwertenden Sinn. Sie ist die
Entscheidung, die du in der Prüfungssituation als Erstes treffen musst — bevor du
eine halbe Stunde in eine Lösung steckst, die nicht durchlaufen kann.

---

## Verkleidung — wo steckt hier eine Suche?

Papier. Kein Programm.

Stofl hat **N Käsestücke** mit bekannten Gewichten. Er möchte wissen, ob sich
**genau zwei** davon zusammen auf exakt **W Gramm** bringen lassen.

Die Frage sieht aus wie eine Ja-oder-Nein-Frage und nicht nach einer Suche. Sie
ist aber eine.

1. Was ist hier **eine Möglichkeit**?
2. Wie viele Möglichkeiten gibt es bei N = 100? Gib eine Formel an, nicht nur
   eine Zahl.
3. Formuliere die Invariante deiner Suche — den Satz, der nach jedem
   Schleifendurchlauf stimmt. Achtung: Er sieht anders aus als bei Endurance,
   weil du nicht das Beste suchst, sondern nur wissen willst, ob es überhaupt
   etwas gibt.
4. Was ändert sich an deiner Antwort auf Frage 2, wenn Stofl dasselbe Käsestück
   zweimal nehmen dürfte?

---

## Lösungen

Erst wenn du es wirklich versucht hast: [Musterlösungen zu M2](loesung.md).
