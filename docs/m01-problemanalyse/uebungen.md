# M1 — Übungen

Drei Aufgaben und eine Trockenübung. Die ersten drei stehen auf soi.ch und geben
echte Punkte.

!!! note "Auch alte Runden zählen"
    Für jede archivierte Aufgabe lassen sich weiterhin Eingabedaten erzeugen und
    Ausgabedateien prüfen. Der Ablauf ist derselbe wie in M0: lokal testen,
    herunterladen, `EINGABE` umstellen, hochladen. Auch die fünf Minuten gelten.

    Was fehlt, ist nur die Rangliste. Das Feedback bekommst du.

---

## Variation — Directions

**[Directions, Teilaufgaben 1 und 2](https://soi.ch/contests/2025/preround/directions/)**
aus derselben Vorrunde.

Binna hat eine Wegbeschreibung aus lauter `l` und `r`. Stofl hat sich nur den
Anfang gemerkt. Stimmt das, woran Stofl sich erinnert, mit dem Anfang von Binnas
Beschreibung überein?

Dieselbe Denkarbeit wie bei Cheeseparty, andere Oberfläche: Statt Zahlen zu
zählen, vergleichst du Zeichenketten. Stell dir zuerst die drei Fragen — was ist
gegeben, was ist gesucht, welche Beziehung verbindet beides — und schreib die
Antworten auf, bevor du VS Code öffnest.

Teilaufgabe 1 hat gleich lange Beschreibungen, Teilaufgabe 2 nur ein einziges
gemerktes Zeichen. Beide sind Spezialfälle. Es lohnt sich, kurz zu überlegen, ob
du sie wirklich getrennt lösen musst.

!!! danger "Achtung, das Format wechselt"
    Anders als Cheeseparty hat Directions eine Anzahl Testfälle T, und jede
    Ausgabezeile beginnt mit `Case #0:`, `Case #1:` und so weiter. Nullbasiert.

---

## Verschärfung — Directions, Teilaufgabe 3

**Teilaufgabe 3** derselben Aufgabe, 60 der 100 Punkte. Jetzt sind beide
Beschreibungen beliebig lang, in beide Richtungen.

Die Schranken bleiben klein (höchstens 100 Zeichen), es geht also nicht um
Geschwindigkeit. Verschärft wird auf einer anderen Achse: **vom Spezialfall zum
allgemeinen Fall.** Teilaufgabe 1 und 2 haben dir je eine Annahme geschenkt —
gleich lang, beziehungsweise nur ein Zeichen. Jetzt fällt beides weg, und es
zeigt sich, ob dein Modell den allgemeinen Fall trifft oder nur die
Sonderfälle.

Ein Fall, den viele übersehen: Was, wenn Stofl sich an *mehr* erinnert, als
Binna überhaupt aufgeschrieben hat?

---

## Verkleidung — Sushi

**[Sushi, Teilaufgaben 1 und 3](https://soi.ch/contests/2018/round1/sushi/)** aus
dem Archiv.

Stofl bestellt Sushi. Es gibt ein Angebot: Wer eine Flasche Sake dazu bestellt,
bekommt ein zweites Sushi geschenkt — bezahlt werden das teurere der beiden
Sushi und die Flasche. Gesucht ist der kleinstmögliche Gesamtpreis.

Beschränke dich auf **Teilaufgabe 1** (zwei Sushi, Sake gratis) und
**Teilaufgabe 3** (zwei Sushi, Sake kostet etwas). Teilaufgabe 2 und 4 brauchen
ein Werkzeug, das du erst in M5 bekommst.

Die Aufgabe klingt nach Optimierung, nach Ausprobieren, nach etwas Grösserem. Ist
sie nicht. Bei zwei Sushi gibt es genau zwei Möglichkeiten, zu bestellen — mehr
nicht. Schreib beide hin und vergleiche sie. Das ist wieder Modellieren, nur gut
versteckt.

??? tip "Die Runde 2018 heisst „First Round" — bin ich hier richtig?"
    Ja. Die SOI hat 2025 die Namen geändert. Was damals „First Round" hiess, ist
    nach heutiger Zählung die **Zweite Runde** — also eigentlich zu schwer für
    diesen Kurs.

    Die ersten Teilaufgaben sind trotzdem gut lösbar. Genau darum picken wir
    einzelne heraus und nicht ganze Runden. Lass dich vom Namen nicht
    einschüchtern.

---

## Widerlegung — Stimmt diese Formel?

Eine Trockenübung ohne Programm. Papier reicht.

Zwei Mitschülerinnen haben Cheeseparty gelöst und kommen auf verschiedene
Formeln:

```
Anna:  Käse = (N · K + 1) · S
Bea:   Käse = (N · (K + 2)) · S
```

Beide sind falsch.

1. Sag bei jeder Formel, **wen** sie vergisst.
2. Beide liefern beim Beispiel `4 3 6` etwas anderes als 126, fallen also sofort
   auf. Finde für **jede** Formel Eingaben, bei denen sie trotzdem das richtige
   Ergebnis liefert.
3. Was sagt dir das über das Testen mit dem mitgelieferten Beispiel?

Die dritte Frage ist die eigentliche. Nimm dir dafür einen Moment.

---

## Lösungen

Erst wenn du es wirklich versucht hast: [Musterlösungen zu M1](loesung.md).
