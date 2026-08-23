# Lernpfad

Der Kurs hat zwei Stränge, die parallel laufen.

**Strang A — Programmieren** bereitet auf die Vorrunde vor.
**Strang B — Denken ohne Code** bereitet auf die Erste Runde vor. Er braucht
keine Programmierkenntnisse und läuft ab Modul 2 nebenher.

## Abhängigkeiten

<svg viewBox="0 0 900 470" role="img" aria-labelledby="pfad-titel pfad-text"
     style="width:100%;height:auto;color:inherit">
  <title id="pfad-titel">Abhängigkeiten der Module</title>
  <desc id="pfad-text">M0 führt zu M1, M1 zu M2, M2 zu M3. Aus M3 gehen M4, M5
  und M6 hervor, aus M4 geht M7 hervor. Aus M2 zweigt gestrichelt Strang B ab:
  B1, danach B2. M6, M7, B1 und B2 sind noch nicht gebaut.</desc>
  <defs>
    <marker id="pfeil" viewBox="0 0 10 10" refX="9" refY="5"
            markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/>
    </marker>
  </defs>
  <g fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#pfeil)">
    <path d="M 350 52  L 350 78"/>
    <path d="M 350 122 L 350 148"/>
    <path d="M 350 192 L 350 218"/>
    <path d="M 350 262 L 350 298"/>
    <path d="M 340 262 L 340 282 L 130 282 L 130 298"/>
    <path d="M 360 262 L 360 282 L 570 282 L 570 298"/>
    <path d="M 130 342 L 130 378"/>
    <path d="M 790 192 L 790 218"/>
  </g>
  <path d="M 450 171 L 698 171" fill="none" stroke="currentColor"
        stroke-width="1.6" stroke-dasharray="6 5" marker-end="url(#pfeil)"/>
  <g stroke="currentColor" stroke-width="1.6" fill="none">
    <rect x="250" y="10"  width="200" height="42" rx="6"/>
    <rect x="250" y="80"  width="200" height="42" rx="6"/>
    <rect x="250" y="150" width="200" height="42" rx="6"/>
    <rect x="250" y="220" width="200" height="42" rx="6"/>
    <rect x="30"  y="300" width="200" height="42" rx="6"/>
    <rect x="250" y="300" width="200" height="42" rx="6"/>
  </g>
  <g stroke="currentColor" stroke-width="1.6" fill="none" stroke-dasharray="5 4"
     opacity="0.55">
    <rect x="470" y="300" width="200" height="42" rx="6"/>
    <rect x="30"  y="380" width="200" height="42" rx="6"/>
    <rect x="700" y="150" width="180" height="42" rx="6"/>
    <rect x="700" y="220" width="180" height="42" rx="6"/>
  </g>
  <g fill="currentColor" font-size="13" text-anchor="middle"
     font-family="system-ui, sans-serif">
    <text x="350" y="36">M0 Werkzeugkasten</text>
    <text x="350" y="106">M1 Problemanalyse</text>
    <text x="350" y="176">M2 Vollständige Suche</text>
    <text x="350" y="246">M3 Laufzeitdenken</text>
    <text x="130" y="326">M4 Lineare Techniken</text>
    <text x="350" y="326">M5 Sortieren und Suchen</text>
    <g opacity="0.55">
      <text x="570" y="326">M6 Zeichenketten, Gitter</text>
      <text x="130" y="406">M7 Konstruktive Verfahren</text>
      <text x="790" y="176">B1 Pseudocode</text>
      <text x="790" y="246">B2 Quiz-Training</text>
    </g>
    <text x="574" y="164" font-size="12" opacity="0.75">Strang B</text>
  </g>
</svg>

**Gestrichelt und blass** heisst: noch nicht gebaut. Der gestrichelte Pfeil nach
rechts heisst ausserdem, dass Strang B nicht zwingend ist — sinnvoll ist er
trotzdem, und er läuft parallel, nicht am Schluss.

## Aufgaben über die Module hinweg

Der Graph oben zeigt, welches Modul auf welchem aufbaut. Die andere Achse ist
genauso wichtig: **dieselbe Aufgabe läuft über mehrere Module.**

Das ist Absicht. Eine SOI-Aufgabe besteht aus Teilaufgaben mit wachsenden
Schranken, und dieser Aufbau ist der rote Faden des Kurses. Du löst die **Ausdauer**
in M2 mit roher Gewalt, in M3 wird sie schnell, in M4 kommt eine neue Regel dazu
— und am Ende hast du alle 100 Punkte, mit einer Lösung, die du selbst
entwickelt hast.

| Aufgabe | Runde | Teilaufgaben | Punkte | Module |
|---|---|---|---|---|
| `cheeseparty` | Vorrunde | 1–2 | 100 | M1 |
| `directions` | Vorrunde | 1–3 | 100 | M1 |
| `sushi` | 2018 | 1–4 | 100 | M1 · M5 |
| `endurance` | Vorrunde | 1–5 | 100 | M2 · M3 · M4 |
| `stairracing` | 2021 | 1–4 | 100 | M0 · M2 · M3 · M4 |
| `thermalsprings` | 2023 | 1 | 20 von 100 | M5 |

Wer M0 bis M5 durchgearbeitet hat, hat **520 Punkte** eingereicht.

Deshalb lohnt es sich, die Aufgabenordner zu behalten: In M3, M4 und M5 baust du
auf Programmen auf, die du früher geschrieben hast — und die alte Lösung ist die
beste Kontrolle für die neue.

## Übersicht

Die Nummer sagt die Reihenfolge, der Name das Thema. Was drin steckt, sagt die
Konzeptspalte — wenn du das schon kannst, steig weiter
hinten ein. Auf jeder Modulseite steht oben, was du dafür mitbringen musst.

| Modul | Konzepte | L | Strang |
|---|---|---|---|
| M0 Werkzeugkasten | VS Code, Play-Knopf, Dateien, 5-Minuten-Regel | 2 | A |
| M1 Problemanalyse und Modellierung | Vom Text zum Modell · Die Probe am Extremfall · Prüfen statt Rechnen | 2 | A |
| M2 Vollständige Suche | Vollständige Suche · Die Invariante · Teilpunkte mitnehmen | 2 | A |
| M3 Laufzeitdenken | Komplexität und Faktor T · Weitergeben statt neu berechnen · Versteckte Schleifen · Mengen und Wörterbücher | 3 | A |
| M4 Felder und lineare Techniken | Präfixsummen · Zweizeiger und Fenster | 3 | A |
| M5 Sortieren und Suchen | Sortieren als Vorverarbeitung · Binäre Suche | 3 | A |
| M6 Zeichenketten und Gitter | Zeichenketten · Zweidimensionale Felder · Nachbarschaft | 2 | A |
| M7 Konstruktive Verfahren | Gierige Verfahren · Invarianten · Zustandsdenken | 2 | A |
| B1 Pseudocode und Simulation | Abläufe von Hand durchspielen | 3 | B |
| B2 Quiz-Training | Zeitdruck, MC-Strategie, wann raten | 2 | B |

Noch nicht gebaut: M6, M7, B1 und B2.

## Hintergrund

Ausserhalb des Kursfadens gibt es Seiten, die erklären, wie ein Werkzeug innen
funktioniert. Du brauchst sie nicht, um Aufgaben zu lösen.

| Seite | passt zu |
|---|---|
| [Sortierverfahren](hintergrund/sortierverfahren.md) | M5, und M3 als Vergleich von Komplexitäten |
