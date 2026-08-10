# M0 — Werkzeugkasten

## Worum es geht

Bevor du deine erste Olympiade-Aufgabe löst, richtest du deinen Arbeitsplatz ein.
Das klingt nach Vorgeplänkel, ist aber der Teil, an dem die meisten scheitern —
nicht am Algorithmus, sondern daran, dass die Ausgabe ein Leerzeichen zu viel hat
oder die Zeit abläuft.

Am Ende dieses Moduls hast du **echte Punkte** bei der SOI geholt. Die Aufgabe
dazu ist absichtlich einfach: Es geht um den Ablauf, nicht ums Knobeln.

!!! warning "Die wichtigste Regel dieses Moduls"
    Auf soi.ch lädst du die Eingabedaten herunter — danach hast du **fünf
    Minuten**, um die Ausgabe hochzuladen. Wer erst dann anfängt zu programmieren,
    schafft es nie.

    Deshalb: **erst lokal testen, dann herunterladen.** Der Download ist der
    letzte Schritt, nicht der erste.

---

## Schritt 1 — Python installieren

Du brauchst nur Python selbst. Keine Zusatzpakete, keine Bibliotheken — alles,
was wir verwenden, ist eingebaut.

=== "Windows"

    1. Geh auf [python.org/downloads](https://www.python.org/downloads/) und lade
       die aktuelle Version herunter.
    2. Starte die heruntergeladene Datei.
    3. **Setz unten das Häkchen bei „Add python.exe to PATH".** Erst danach auf
       *Install Now* klicken.

        Das ist der einzige Schritt, den man wirklich falsch machen kann. Ohne das
        Häkchen findet das Terminal Python später nicht.

    4. Öffne die *Eingabeaufforderung* oder *PowerShell* über das Startmenü und
       tippe:

        ```
        python --version
        ```

=== "macOS"

    1. Geh auf [python.org/downloads](https://www.python.org/downloads/) und lade
       die aktuelle Version für macOS herunter.
    2. Öffne die `.pkg`-Datei und klick dich durch den Installer.
    3. Öffne die App *Terminal* (über Spotlight: Cmd + Leertaste, dann
       „Terminal") und tippe:

        ```
        python3 --version
        ```

    Auf dem Mac heisst der Befehl **`python3`**, nicht `python`. Das gilt überall
    in diesem Kurs.

!!! success "Kontrollpunkt"
    Du siehst eine Versionsnummer wie `Python 3.13.1`. Alles ab 3.10 ist in
    Ordnung.

---

## Schritt 2 — VS Code einrichten

1. Lade [Visual Studio Code](https://code.visualstudio.com/) herunter und
   installiere es.
2. Starte VS Code und öffne links in der Seitenleiste die **Erweiterungen**
   (das Symbol mit den vier Quadraten).
3. Such nach **Python** und installiere die Erweiterung von Microsoft.
4. Öffne über *Terminal → Neues Terminal* das eingebaute Terminal. Es erscheint
   unten im Fenster.

!!! success "Kontrollpunkt"
    Tipp im VS-Code-Terminal denselben Versionsbefehl wie oben. Wenn hier
    dieselbe Versionsnummer erscheint, ist alles verbunden.

!!! tip "Ab jetzt gilt"
    In allen Befehlen unten steht `python`. **Auf dem Mac tippst du überall
    `python3`.**

---

## Schritt 3 — Ordner und Vorlage einrichten

Leg einen Ordner für die Aufgabe an, zum Beispiel `treppenlauf/`. Kopier
`vorlage.py` und `pruefe.py` aus dem Ordner `vorlagen/` hinein und benenne die
Vorlage in `loesung.py` um.

Öffne den Ordner in VS Code über *Datei → Ordner öffnen*. Das eingebaute Terminal
startet dann automatisch in diesem Ordner — wichtig, damit die Befehle die
richtigen Dateien finden.

!!! success "Kontrollpunkt"
    Links in der Seitenleiste siehst du `loesung.py` und `pruefe.py`.

---

## Schritt 4 — Die Aufgabe verstehen

Wir nehmen **[Treppenlauf, Teilaufgabe 1](https://soi.ch/contests/2021/round1/stairracing/)**
aus der Runde 2020/2021.

Eine Strasse hat auf jeder Seite genau einen Wolkenkratzer. Maus Binna startet auf
dem einen Dach, läuft hinunter, über die Strasse und auf dem anderen hinauf.
Gesucht ist die Gesamtlänge der Strecke.

Bei nur einem Wolkenkratzer pro Seite stehen sich beide direkt gegenüber — die
Strecke entlang der Strasse ist also 0.

### Das Eingabeformat

```
2        ← Anzahl Testfälle T
1        ← Testfall 0: N (Anzahl Wolkenkratzer pro Seite, hier immer 1)
2        ← Höhe a des Wolkenkratzers links
3        ← Höhe b des Wolkenkratzers rechts
1        ← Testfall 1: N
1336     ← Höhe a
1        ← Höhe b
```

### Das Ausgabeformat

```
Case #0: 5
Case #1: 1337
```

!!! danger "Hier verliert man Punkte"
    Die Nummerierung beginnt bei **null**, nicht bei eins. Ein Doppelpunkt und
    ein Leerzeichen nach der Nummer. Genau eine Zeile pro Testfall.

!!! success "Kontrollpunkt"
    Rechne den zweiten Testfall im Kopf nach und vergleiche mit `Case #1: 1337`.
    Wenn du verstehst, woher die Zahl kommt, hast du das Format verstanden.

---

## Schritt 5 — Beispiel lokal testen

Leg zwei Dateien im Aufgabenordner an und tipp die Beispiele aus der
Aufgabenstellung ab:

`bsp_ein.txt`

```
2
1
2
3
1
1336
1
```

`bsp_aus.txt`

```
Case #0: 5
Case #1: 1337
```

Öffne `loesung.py`. Der obere Teil liest die Eingabe — daran musst du nichts
ändern. Deine Aufgabe ist nur die Funktion in der Mitte:

```python
def loese(n, werte):
    # TODO: berechne das Ergebnis fuer einen Testfall
    return 0
```

Bei Teilaufgabe 1 besteht ein Testfall aus `N`, dann `a`, dann `b`. Passe den
Hauptteil so an, dass er genau diese drei Zahlen liest, und gib die Summe der
beiden Höhen zurück.

Dann im Terminal:

```
python loesung.py < bsp_ein.txt > mein_aus.txt
python pruefe.py bsp_aus.txt mein_aus.txt
```

Der erste Befehl schickt `bsp_ein.txt` als Eingabe in dein Programm und schreibt
alles, was du mit `print` ausgibst, nach `mein_aus.txt`. Der zweite vergleicht.

!!! tip "In VS Code geht das auf Tastendruck"
    Die mitgelieferte `tasks.json` führt beide Befehle zusammen aus. Menü
    *Terminal → Task ausführen → SOI: Beispiel testen*.

!!! success "Kontrollpunkt"
    `pruefe.py` meldet „Alles richtig (2 Zeilen)." Erst dann geht es weiter.

---

## Schritt 6 — Die Fünf-Minuten-Runde

Jetzt zählt es. Öffne die Aufgabenseite, scroll zu Teilaufgabe 1 und mach dir
klar, wo der Knopf ist, **bevor** du klickst. Du brauchst einen Account auf
soi.ch und musst eingeloggt sein.

1. **Eingabedaten herunterladen** — du bekommst eine `input.txt` mit frischen
   Testfällen. Die Uhr läuft. Auf der Seite erscheint jetzt der Upload-Bereich.
2. Speicher die Datei in deinen Aufgabenordner.
3. Im Terminal:

    ```
    python loesung.py < input.txt > output.txt
    ```

4. Lade `output.txt` auf der Aufgabenseite hoch.

Nur die Ausgabedatei — dein Python-Code bleibt bei dir.

!!! tip "Falls die Zeit abläuft"
    Kein Problem. Lade neue Eingabedaten herunter und fang von vorne an. Jeder
    Download erzeugt andere Testfälle, du kannst also keine alte Ausgabe
    wiederverwenden — aber beliebig oft neu antreten.

!!! success "Kontrollpunkt"
    Du hast 25 Punkte für Teilaufgabe 1.

---

## Wenn etwas nicht klappt

??? tip "Windows: „Python wurde nicht gefunden" oder es öffnet sich der Store"
    Zwei mögliche Ursachen. Entweder fehlte beim Installieren das Häkchen bei
    „Add python.exe to PATH" — dann den Installer nochmal starten, *Modify*
    wählen und es nachholen.

    Oder Windows fängt den Befehl ab: *Einstellungen → Apps → Erweiterte
    App-Einstellungen → App-Ausführungsaliase*, dort `python.exe` und
    `python3.exe` ausschalten.

??? tip "Mac: `python` kennt er nicht"
    Auf dem Mac heisst der Befehl `python3`. Das gilt in allen Befehlen dieses
    Kurses.

??? tip "`pruefe.py` meldet eine falsche Zeilenzahl"
    Meist gibst du eine Zeile zu viel oder zu wenig aus. Prüfe: genau ein `print`
    pro Testfall, keine zusätzliche Ausgabe wie „Bitte Zahl eingeben".

    Debug-Ausgaben landen in der Ausgabedatei und machen sie kaputt. Wenn du beim
    Suchen etwas ausgeben willst, nutze `print(..., file=sys.stderr)` — das
    erscheint im Terminal, nicht in der Datei.

??? tip "Alle Zeilen sind um eins verschoben"
    Klassiker: `Case #1` als erste Zeile statt `Case #0`. Die Schleife muss bei
    null anfangen.

??? tip "`mein_aus.txt` ist leer"
    Entweder ist dein Programm mit einem Fehler abgestürzt — dann steht die
    Meldung im Terminal — oder du hast `>` vergessen und die Ausgabe ist im
    Terminal gelandet.

??? tip "Das Programm wartet und tut nichts"
    Du hast irgendwo `input()` benutzt. Die Vorlage liest über `sys.stdin`;
    `input()` blockiert, wenn keine Datei umgeleitet wird.

??? tip "Das Terminal findet meine Dateien nicht"
    Du hast den Ordner nicht in VS Code geöffnet, sondern nur die Datei. Mach
    *Datei → Ordner öffnen* und wähle den Aufgabenordner.

---

## Geschafft

Du kannst jetzt eine SOI-Aufgabe von der Aufgabenstellung bis zu den Punkten
durchspielen. Alles Weitere baut darauf auf — der Ablauf bleibt in jedem Modul
derselbe, nur die Aufgabe wird interessanter.

Wenn du magst: **Teilaufgabe 2** von Treppenlauf ist ein guter Selbsttest. Zwei
Wolkenkratzer pro Seite, vier mögliche Kombinationen. Mehr als Ausprobieren
braucht es nicht — und du übst den Ablauf ein zweites Mal.

Weiter geht es mit Modul 1 — Problemanalyse. <!-- TODO Link setzen, sobald M1 existiert -->
