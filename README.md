# Laborwerte-Dashboard

Selbst gehostetes Dashboard für deine Blutbefunde: Werte manuell eintragen,
Verlauf pro Parameter als Diagramm ansehen, Referenzbereiche und
Erklärtexte pro Parameter inklusive. Läuft komplett lokal auf deinem
Homeserver, keine Cloud, keine externen Aufrufe zur Laufzeit.

**Wichtiger Hinweis:** Diese App ist ein persönliches Tracking-Tool und
ersetzt keine ärztliche Beratung. Referenzbereiche sind allgemeine
Orientierungswerte und können je nach Labor/Messmethode leicht abweichen —
maßgeblich ist immer der auf deinem tatsächlichen Befund angegebene Bereich.

## Was ist schon drin

- Manuelle Eingabe von Befunden (Datum, Labor, beliebig viele Parameter)
- **75 Laborparameter** vorkonfiguriert: Leber, Niere, Blutfette, Blutzucker,
  Schilddrüse, Blutbild (inkl. Differenzialblutbild), Elektrolyte,
  Eisenhaushalt, Vitamine, Spurenelemente, Gerinnung, Hormone, Muskel & Herz,
  Pankreas, Entzündung/Immunsystem, Körpermaße
- **Körpergröße & Gewicht eintragbar, BMI wird automatisch berechnet**, sobald
  beide Werte im selben Eintrag vorhanden sind
- Durchsuchbare Parameterauswahl beim Eintragen (kein unübersichtliches
  Dropdown mehr)
- Dashboard mit Statusfarben (im Bereich / erhöht / erniedrigt)
- Verlaufsdiagramm pro Parameter mit eingezeichnetem Referenzbereich, sauber
  gerundeten Achsenwerten
- Infotext je Parameter: was er ist, was erhöhte/niedrige Werte bedeuten können
- **Referenzbereiche und Einheiten individuell überschreibbar** unter
  Einstellungen → Referenzbereiche — z. B. wenn dein Labor andere Grenzwerte
  oder eine andere Einheit verwendet als hinterlegt. Ein "Zurücksetzen"-Button
  stellt die Standardwerte wieder her. Hinweis: Eine geänderte Einheit ist nur
  eine Anzeige-Beschriftung, sie rechnet bereits gespeicherte Werte nicht um.
- Referenzbereiche alters-/geschlechtsabhängig, wo relevant (z. B. Hämoglobin,
  Ferritin, Harnsäure, Testosteron)
- **Vollständiger Export/Import als JSON-Backup** unter Einstellungen → Daten
- Mobile-optimierte Oberfläche (Bottom-Nav auf dem Handy, Seitenleiste am Desktop)
- Alle Daten in einer lokalen SQLite-Datei in einem Docker-Volume

## Zum Thema "globale Referenzwerte automatisch abrufen"

Es gibt keine verlässliche, strukturierte öffentliche Quelle, die Referenzbereiche
je Labor/Alter/Geschlecht liefert — jedes Labor kalibriert seine Geräte leicht
unterschiedlich, und die Werte stehen meist nur als Text auf den Befunden selbst.
Der praktikable Weg: **Einstellungen → Referenzbereiche** — dort siehst du pro
Parameter den hinterlegten Standardwert und kannst ihn mit dem exakten Bereich
von deinem Arzt/Labor überschreiben. Diese eigenen Werte werden dann überall
im Dashboard verwendet (Statusfarben, Diagramm-Referenzbereich, etc.).

## Noch nicht drin (bewusst erstmal weggelassen)

- Foto-Upload mit automatischer Texterkennung (OCR). Die Datenstruktur ist
  darauf vorbereitet (`Entry.photo_path`), aber der Baustein selbst kommt in
  einem zweiten Schritt, sobald das Kern-Dashboard bei dir läuft und passt.
- Automatischer Online-Abgleich von Referenzbereichen. Stattdessen liegt eine
  kuratierte Liste in `backend/app/parameters_data.py`, plus die
  benutzerfreundliche Override-Funktion unter Einstellungen → Referenzbereiche
  (siehe oben).

## Deployment auf Proxmox/Portainer

Voraussetzung: Ein LXC/VM mit Docker (z. B. über die Proxmox-Community-Scripts
einen "Docker"-LXC aufsetzen) und Portainer, das darauf zeigt.

1. Diesen Ordner (`lab-dashboard/`) auf den Server bringen, z. B. per `git`,
   `scp` oder indem du ihn als ZIP hochlädst und entpackst. Portainer braucht
   Zugriff auf den Ordner mit `docker-compose.yml`, `backend/` und `frontend/`.

2. In Portainer: **Stacks → Add stack**
   - Name: `labor-dashboard`
   - Build method: **Repository** (falls der Ordner in einem Git-Repo liegt)
     oder **Upload**, wenn du die Dateien direkt hochlädst.
   - Falls du "Web editor" nutzt: Inhalt von `docker-compose.yml` einfügen —
     Portainer baut dann `./backend` und `./frontend` aus dem Kontext, den du
     mit hochlädst.

3. Deploy the stack. Portainer baut beide Images (dauert beim ersten Mal ein
   paar Minuten, danach nur bei Änderungen).

4. Danach ist das Dashboard unter `http://<server-ip>:8088` erreichbar.
   Port bei Bedarf in `docker-compose.yml` anpassen.

5. Optional: In deinem Reverse Proxy (z. B. nginx Proxy Manager, Caddy,
   Traefik) einen eigenen Hostnamen mit HTTPS davorsetzen, wenn du von
   unterwegs zugreifen willst (z. B. per WireGuard/Tailscale ins Heimnetz,
   dann Reverse Proxy nur intern).

### Ohne Portainer (direkt per CLI)

```bash
cd lab-dashboard
docker compose up -d --build
```

### Backup

**Empfohlen:** In der App unter Einstellungen → Daten → "Alle Daten exportieren"
— lädt eine JSON-Datei mit allen Einträgen, Einstellungen und angepassten
Referenzbereichen herunter. Über "Backup wiederherstellen" auf derselben Seite
lässt sie sich auch wieder komplett einspielen (ersetzt dabei alle aktuellen
Daten, mit Sicherheitsabfrage).

Alternativ liegen alle Daten ohnehin im Docker-Volume `labor-data` (SQLite-Datei),
falls du lieber auf Dateisystemebene sichern willst:

```bash
docker run --rm -v labor-dashboard_labor-data:/data -v $(pwd):/backup \
  alpine tar czf /backup/labor-data-backup.tar.gz -C /data .
```

(Volume-Name kann je nach Stack-Namen in Portainer leicht abweichen — mit
`docker volume ls` nachsehen.)

## Eigene Parameter oder Referenzbereiche anpassen

Alles steckt in `backend/app/parameters_data.py`, in der Liste `PARAMETERS`.
Ein Eintrag sieht so aus:

```python
{
    "code": "ggt",                 # interner Code, wird auch als DB-Key verwendet
    "name": "GGT",                 # Kurzname für die Karten
    "full_name": "Gamma-Glutamyltransferase",
    "unit": "U/l",
    "category": "Leber",           # Gruppierung im Dashboard
    "description": "...",
    "high_meaning": "...",
    "low_meaning": "...",
    "ranges": [
        {"gender": "m", "min_age": 0, "max_age": 200, "low": 10, "high": 71},
        {"gender": "f", "min_age": 0, "max_age": 200, "low": 6, "high": 42},
    ],
},
```

Einfach einen neuen Eintrag ergänzen (eindeutigen `code` wählen) und den
`backend`-Container neu bauen (`docker compose up -d --build backend`).
Bereits gespeicherte Messwerte bleiben erhalten, da sie per `code` referenziert
werden.

## Lokale Entwicklung (ohne Docker)

Backend:

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
DATA_DIR=./data uvicorn app.main:app --reload
```

Frontend:

```bash
cd frontend
npm install
npm run dev
```

Im Dev-Modus läuft das Frontend auf Port 5173 und das Backend auf 8000 —
dafür in `vite.config.js` einen Proxy für `/api` auf `http://localhost:8000`
ergänzen, oder direkt mit der gebauten Docker-Variante testen, dort ist das
schon per nginx gelöst.

## Nächste Schritte (Vorschlag)

1. Ersten echten Befund eintragen und schauen, ob Kategorien/Parameter passen.
2. Fehlende Parameter in `parameters_data.py` ergänzen.
3. Wenn das passt: Foto-Upload + OCR als zweiten Ausbauschritt angehen
   (z. B. Tesseract lokal im Backend-Container, mit manueller Bestätigung
   der erkannten Werte vor dem Speichern — volle Automatik ohne Kontrolle
   ist bei Laborberichten erfahrungsgemäß nicht zuverlässig genug).
