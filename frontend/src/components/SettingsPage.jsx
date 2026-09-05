import React, { useEffect, useState } from "react";
import { api } from "../api";

export default function SettingsPage() {
  const [birthYear, setBirthYear] = useState("");
  const [gender, setGender] = useState("");
  const [displayName, setDisplayName] = useState("");
  const [saved, setSaved] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    api.getSettings().then((s) => {
      setBirthYear(s.birth_year || "");
      setGender(s.gender || "");
      setDisplayName(s.display_name || "");
    }).catch((e) => setError(e.message));
  }, []);

  async function handleSubmit(e) {
    e.preventDefault();
    setError(null);
    try {
      await api.updateSettings({
        birth_year: birthYear ? parseInt(birthYear, 10) : null,
        gender: gender || null,
        display_name: displayName || null,
      });
      setSaved(true);
      setTimeout(() => setSaved(false), 2000);
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <form onSubmit={handleSubmit} className="flex flex-col gap-6 max-w-md">
      <div>
        <h1 className="text-xl font-semibold tracking-tight">Einstellungen</h1>
        <p className="text-sm text-muted mt-1">
          Geburtsjahr und Geschlecht werden nur genutzt, um passende Referenzbereiche
          anzuzeigen (z. B. unterscheiden sich manche Werte zwischen Mann und Frau).
        </p>
      </div>

      <label className="flex flex-col gap-1.5 text-sm">
        <span className="text-muted">Name (optional, nur zur Anzeige)</span>
        <input
          type="text"
          value={displayName}
          onChange={(e) => setDisplayName(e.target.value)}
          className="rounded-lg border border-border bg-surface px-3 py-2 focus:outline-none focus:ring-2 focus:ring-accent/40"
        />
      </label>

      <label className="flex flex-col gap-1.5 text-sm">
        <span className="text-muted">Geburtsjahr</span>
        <input
          type="number"
          min="1900"
          max="2100"
          value={birthYear}
          onChange={(e) => setBirthYear(e.target.value)}
          placeholder="z. B. 2001"
          className="rounded-lg border border-border bg-surface px-3 py-2 font-mono focus:outline-none focus:ring-2 focus:ring-accent/40"
        />
      </label>

      <label className="flex flex-col gap-1.5 text-sm">
        <span className="text-muted">Geschlecht</span>
        <select
          value={gender}
          onChange={(e) => setGender(e.target.value)}
          className="rounded-lg border border-border bg-surface px-3 py-2 focus:outline-none focus:ring-2 focus:ring-accent/40"
        >
          <option value="">Nicht angegeben</option>
          <option value="m">Männlich</option>
          <option value="f">Weiblich</option>
        </select>
      </label>

      {error && <p className="text-sm text-status-high">{error}</p>}

      <div className="flex items-center gap-3">
        <button
          type="submit"
          className="bg-accent text-white text-sm font-medium px-4 py-2 rounded-lg hover:bg-accent-dark transition-colors"
        >
          Speichern
        </button>
        {saved && <span className="text-sm text-status-normal">Gespeichert.</span>}
      </div>
    </form>
  );
}
