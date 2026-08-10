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

Das Terminal brauchst du nur zum Nachschauen. Gestartet wird jedes Programm in
diesem Kurs mit dem **Play-Knopf** oben rechts im Editor — dem Dreieck. Was dein
Programm ausgibt, erscheint dann unten im Terminal.

!!! success "Kontrollpunkt"
    Tipp im VS-Code-Terminal denselben Versionsbefehl wie oben. Wenn hier
    dieselbe Versionsnummer erscheint, ist alles verbunden.

!!! tip "Der Unterschied Windows / Mac"
    Beim Versionsbefehl heisst es auf dem Mac `python3` statt `python`. Für den
    Play-Knopf spielt das keine Rolle — VS Code weiss selbst, wie Python auf
    deinem Gerät heisst.

---

## Schritt 3 — Ordner und Vorlage einrichten

Leg einen Ordner für die Aufgabe an, zum Beispiel `treppenlauf/`. Kopier den
gesamten Inhalt des Ordners `vorlagen/` hinein und benenne `vorlage.py` in
`loesung.py` um.

Du kopierst damit drei Dinge: `loesung.py` bearbeitest du gleich selbst,
`pruefe.py` ist ein Helfer und muss nur danebenliegen, und der Ordner `.vscode`
enthält eine Einstellung, die dafür sorgt, dass dein Programm seine Dateien
findet.

### Falls du `.vscode` gar nicht siehst

Namen, die mit einem Punkt beginnen, gelten als versteckt.

=== "Windows"

    Der Explorer zeigt den Ordner normalerweise an. Falls nicht: oben im Reiter
    *Ansicht* das Häkchen bei *Ausgeblendete Elemente* setzen.

=== "macOS"

    Der Finder blendet solche Namen aus. Drück **Cmd + Shift + Punkt** — dann
    erscheint `.vscode`, etwas blasser als die übrigen Ordner. Dieselbe
    Tastenkombination blendet ihn wieder aus. Kopieren kannst du ihn nur,
    solange er sichtbar ist.

Ohne `.vscode` funktioniert trotzdem alles, solange du im nächsten Absatz den
Ordner öffnest und nicht nur die Datei. Der Ordner ist die Absicherung für den
Fall, dass du das einmal vergisst.

Öffne den Aufgabenordner in VS Code über *Datei → Ordner öffnen*. **Nicht nur die
Datei öffnen, sondern den Ordner** — sonst sucht dein Programm später an der
falschen Stelle.

!!! success "Kontrollpunkt"
    Links in der Seitenleiste siehst du `loesung.py` und `pruefe.py`, und zwar
    unterhalb des Ordnernamens `TREPPENLAUF`.

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

Öffne `loesung.py`. Ganz oben steht, mit welchen Dateien das Programm arbeitet:

```python
EINGABE = "bsp_ein.txt"
AUSGABE = "output.txt"
```

Solange dort `bsp_ein.txt` steht, rechnest du mit dem Beispiel. Das Ergebnis
landet in `output.txt`.

Der Teil darunter liest die Eingabe — daran musst du nichts ändern. Deine Aufgabe
ist die Funktion in der Mitte:

```python
def loese(n, werte):
    # TODO: berechne das Ergebnis fuer einen Testfall
    return 0
```

Bei Teilaufgabe 1 besteht ein Testfall aus `N`, dann `a`, dann `b`. Passe den
Hauptteil so an, dass er genau diese drei Zahlen liest, und gib die Summe der
beiden Höhen zurück.

Dann klick den **Play-Knopf** oben rechts. Unten im Terminal steht, was passiert
ist:

```
output.txt geschrieben (2 Zeilen).
Alles richtig (2 Zeilen).
Du kannst jetzt die echte Eingabe herunterladen.
```

Dein Programm hat `bsp_ein.txt` gelesen, gerechnet, `output.txt` geschrieben und
das Ergebnis anschliessend mit `bsp_aus.txt` verglichen. Stimmt etwas nicht,
zeigt es dir die erste abweichende Zeile.

!!! tip "print ist zum Suchen da"
    Deine Ergebnisse landen in der Datei, nicht im Terminal. Du kannst also
    jederzeit `print` einbauen, um nachzusehen, was dein Programm gerade rechnet
    — die Ausgabedatei bleibt davon unberührt.

!!! success "Kontrollpunkt"
    Im Terminal steht „Alles richtig (2 Zeilen)." Erst dann geht es weiter.

---

## Schritt 6 — Die Fünf-Minuten-Runde

Jetzt zählt es. Öffne die Aufgabenseite, scroll zu Teilaufgabe 1 und mach dir
klar, wo der Knopf ist, **bevor** du klickst. Du brauchst einen Account auf
soi.ch und musst eingeloggt sein.

1. **Eingabedaten herunterladen** — du bekommst eine `input.txt` mit frischen
   Testfällen. Die Uhr läuft. Auf der Seite erscheint jetzt der Upload-Bereich.
2. Speicher die Datei in deinen Aufgabenordner, neben `loesung.py`.
3. Ändere in `loesung.py` die oberste Zeile auf die echte Eingabe:

    ```python
    EINGABE = "input.txt"
    ```

4. Play-Knopf. Im Terminal steht `output.txt geschrieben`.
5. Lade `output.txt` auf der Aufgabenseite hoch.

Nur die Ausgabedatei — dein Python-Code bleibt bei dir.

Übe den Wechsel in Schritt 3 einmal vorher. Es ist eine einzige Zeile, aber unter
Zeitdruck ist sie leicht zu vergessen — und dann lädst du das Ergebnis des
Beispiels hoch.

!!! tip "Danach wieder zurückstellen"
    Für den nächsten Test setzt du `EINGABE` wieder auf `"bsp_ein.txt"`. Sonst
    rechnet dein Programm weiter mit einer Eingabedatei, deren Lösung du gar
    nicht kennst.

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

??? tip "`FileNotFoundError: bsp_ein.txt`"
    Dein Programm findet die Eingabedatei nicht. Drei mögliche Ursachen:

    - Die Datei liegt nicht im selben Ordner wie `loesung.py`.
    - Sie heisst anders, als oben in `EINGABE` steht. Windows blendet Endungen
      manchmal aus — aus `bsp_ein.txt` wird dann heimlich `bsp_ein.txt.txt`.
    - Du hast in VS Code nur die Datei geöffnet, nicht den Ordner. Mach
      *Datei → Ordner öffnen* und wähle den Aufgabenordner.

??? tip "`ModuleNotFoundError: No module named 'pruefe'`"
    `pruefe.py` fehlt im Aufgabenordner. Kopier sie aus `vorlagen/` daneben.

??? tip "Die Zeilenzahl stimmt nicht"
    Meist schreibst du eine Zeile zu viel oder zu wenig. Prüfe: genau ein
    `zeilen.append(...)` pro Testfall.

    Achtung, das ist etwas anderes als `print`. Was du mit `print` ausgibst,
    erscheint nur im Terminal und landet nie in der Ausgabedatei.

??? tip "Alle Zeilen sind um eins verschoben"
    Klassiker: `Case #1` als erste Zeile statt `Case #0`. Die Schleife muss bei
    null anfangen.

??? tip "Das Programm wartet und tut nichts"
    Du hast irgendwo `input()` benutzt. Damit wartet Python auf eine Eingabe über
    die Tastatur. Die Vorlage liest aus der Datei — `input()` brauchst du in
    diesem Kurs nie.

??? tip "Der Play-Knopf fehlt oder startet etwas anderes"
    Die Python-Erweiterung von Microsoft ist nicht installiert (Schritt 2). Zur
    Not geht es auch über *Rechtsklick im Editor → Python-Datei im Terminal
    ausführen*.

---

## Geschafft

Du kannst jetzt eine SOI-Aufgabe von der Aufgabenstellung bis zu den Punkten
durchspielen. Alles Weitere baut darauf auf — der Ablauf bleibt in jedem Modul
derselbe, nur die Aufgabe wird interessanter.

Wenn du magst: **Teilaufgabe 2** von Treppenlauf ist ein guter Selbsttest. Zwei
Wolkenkratzer pro Seite, vier mögliche Kombinationen. Mehr als Ausprobieren
braucht es nicht — und du übst den Ablauf ein zweites Mal.

Weiter geht es mit [M1 — Problemanalyse und Modellierung](../m01-problemanalyse/index.md).
