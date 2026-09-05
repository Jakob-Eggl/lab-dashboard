import React, { useRef, useState } from "react";
import { Download, Upload, AlertTriangle } from "lucide-react";
import { api } from "../api";

export default function DataTab() {
  const fileInputRef = useRef(null);
  const [status, setStatus] = useState(null); // { type: "success" | "error", message }
  const [pendingImport, setPendingImport] = useState(null); // parsed JSON, waiting for confirmation
  const [importing, setImporting] = useState(false);

  async function handleExport() {
    setStatus(null);
    try {
      const data = await api.exportData();
      const blob = new Blob([JSON.stringify(data, null, 2)], { type: "application/json" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      const stamp = new Date().toISOString().slice(0, 10);
      a.href = url;
      a.download = `laborwerte-backup-${stamp}.json`;
      document.body.appendChild(a);
      a.click();
      a.remove();
      URL.revokeObjectURL(url);
      setStatus({ type: "success", message: "Backup wurde heruntergeladen." });
    } catch (e) {
      setStatus({ type: "error", message: e.message });
    }
  }

  function handleFileChosen(e) {
    const file = e.target.files?.[0];
    if (!file) return;
    setStatus(null);
    const reader = new FileReader();
    reader.onload = () => {
      try {
        const parsed = JSON.parse(reader.result);
        if (!parsed.entries || !parsed.settings) {
          throw new Error("Das ist keine gültige Backup-Datei.");
        }
        setPendingImport(parsed);
      } catch (err) {
        setStatus({ type: "error", message: "Datei konnte nicht gelesen werden: " + err.message });
      }
    };
    reader.readAsText(file);
    e.target.value = ""; // allow re-selecting the same file later
  }

  async function confirmImport() {
    if (!pendingImport) return;
    setImporting(true);
    try {
      const result = await api.importData(pendingImport);
      setStatus({
        type: "success",
        message: `Import abgeschlossen: ${result.imported_entries} Einträge wiederhergestellt.`,
      });
      setPendingImport(null);
    } catch (e) {
      setStatus({ type: "error", message: e.message });
    } finally {
      setImporting(false);
    }
  }

  return (
    <div className="flex flex-col gap-6 max-w-xl">
      <div>
        <h3 className="text-sm font-medium mb-1">Backup exportieren</h3>
        <p className="text-sm text-muted mb-3">
          Lädt eine JSON-Datei mit allen Einträgen, deinem Profil und deinen angepassten
          Referenzbereichen herunter. Am besten regelmäßig sichern, z. B. nach jedem neuen Befund.
        </p>
        <button
          type="button"
          onClick={handleExport}
          className="inline-flex items-center gap-2 text-sm font-medium bg-accent text-white px-4 py-2 rounded-lg hover:bg-accent-dark transition-colors"
        >
          <Download size={16} /> Alle Daten exportieren
        </button>
      </div>

      <div className="border-t border-border pt-6">
        <h3 className="text-sm font-medium mb-1">Backup wiederherstellen</h3>
        <p className="text-sm text-muted mb-3">
          Achtung: Das ersetzt <strong>alle</strong> aktuell gespeicherten Daten in dieser Installation
          durch den Inhalt der Datei.
        </p>
        <input
          ref={fileInputRef}
          type="file"
          accept="application/json"
          onChange={handleFileChosen}
          className="hidden"
        />
        <button
          type="button"
          onClick={() => fileInputRef.current?.click()}
          className="inline-flex items-center gap-2 text-sm font-medium border border-border px-4 py-2 rounded-lg hover:bg-black/[0.03] transition-colors"
        >
          <Upload size={16} /> Backup-Datei auswählen
        </button>
      </div>

      {pendingImport && (
        <div className="rounded-card border border-status-high/40 bg-status-highBg p-4 flex flex-col gap-3">
          <div className="flex items-center gap-2 text-status-high text-sm font-medium">
            <AlertTriangle size={16} /> Wirklich alle aktuellen Daten ersetzen?
          </div>
          <p className="text-sm text-ink/90">
            Diese Datei enthält {pendingImport.entries.length} Eintrag/Einträge
            (Stand: {new Date(pendingImport.exported_at).toLocaleString("de-DE")}). Alle jetzt
            gespeicherten Einträge, Einstellungen und angepassten Referenzbereiche werden
            unwiderruflich damit überschrieben.
          </p>
          <div className="flex gap-3">
            <button
              type="button"
              onClick={confirmImport}
              disabled={importing}
              className="text-sm font-medium bg-status-high text-white px-4 py-2 rounded-lg disabled:opacity-60"
            >
              {importing ? "Importiert…" : "Ja, ersetzen"}
            </button>
            <button
              type="button"
              onClick={() => setPendingImport(null)}
              className="text-sm font-medium px-4 py-2 rounded-lg hover:bg-black/[0.03]"
            >
              Abbrechen
            </button>
          </div>
        </div>
      )}

      {status && (
        <p className={`text-sm ${status.type === "error" ? "text-status-high" : "text-status-normal"}`}>
          {status.message}
        </p>
      )}
    </div>
  );
}
