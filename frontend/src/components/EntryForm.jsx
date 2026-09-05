import React, { useEffect, useMemo, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { X, Plus } from "lucide-react";
import { api } from "../api";

export default function EntryForm() {
  const { id } = useParams();
  const isEdit = Boolean(id);
  const navigate = useNavigate();

  const [parameters, setParameters] = useState([]);
  const [entryDate, setEntryDate] = useState(() => new Date().toISOString().slice(0, 10));
  const [labName, setLabName] = useState("");
  const [note, setNote] = useState("");
  const [rows, setRows] = useState([]); // { parameter_code, value }
  const [pickerCode, setPickerCode] = useState("");
  const [error, setError] = useState(null);
  const [saving, setSaving] = useState(false);

  useEffect(() => {
    api.getParameters().then(setParameters).catch((e) => setError(e.message));
  }, []);

  useEffect(() => {
    if (!isEdit) return;
    api.getEntries().then((entries) => {
      const entry = entries.find((e) => String(e.id) === String(id));
      if (!entry) return;
      setEntryDate(entry.entry_date);
      setLabName(entry.lab_name || "");
      setNote(entry.note || "");
      setRows(entry.measurements.map((m) => ({ parameter_code: m.parameter_code, value: String(m.value) })));
    }).catch((e) => setError(e.message));
  }, [id, isEdit]);

  const byCategory = useMemo(() => {
    return parameters.reduce((acc, p) => {
      (acc[p.category] = acc[p.category] || []).push(p);
      return acc;
    }, {});
  }, [parameters]);

  const usedCodes = new Set(rows.map((r) => r.parameter_code));
  const paramByCode = useMemo(() => Object.fromEntries(parameters.map((p) => [p.code, p])), [parameters]);

  function addRow(code) {
    if (!code || usedCodes.has(code)) return;
    setRows((r) => [...r, { parameter_code: code, value: "" }]);
    setPickerCode("");
  }

  function updateRowValue(code, value) {
    setRows((r) => r.map((row) => (row.parameter_code === code ? { ...row, value } : row)));
  }

  function removeRow(code) {
    setRows((r) => r.filter((row) => row.parameter_code !== code));
  }

  async function handleSubmit(e) {
    e.preventDefault();
    setError(null);
    const measurements = rows
      .filter((r) => r.value !== "")
      .map((r) => ({ parameter_code: r.parameter_code, value: parseFloat(r.value.replace(",", ".")) }));

    if (measurements.length === 0) {
      setError("Bitte mindestens einen Wert eintragen.");
      return;
    }
    setSaving(true);
    try {
      const payload = { entry_date: entryDate, lab_name: labName || null, note: note || null, measurements };
      if (isEdit) {
        await api.updateEntry(id, payload);
      } else {
        await api.createEntry(payload);
      }
      navigate("/eintraege");
    } catch (err) {
      setError(err.message);
    } finally {
      setSaving(false);
    }
  }

  return (
    <form onSubmit={handleSubmit} className="flex flex-col gap-6 max-w-2xl">
      <div>
        <h1 className="text-xl font-semibold tracking-tight">{isEdit ? "Eintrag bearbeiten" : "Neuer Eintrag"}</h1>
        <p className="text-sm text-muted mt-1">Trag die Werte von deinem Befund ein.</p>
      </div>

      <div className="grid sm:grid-cols-2 gap-4">
        <label className="flex flex-col gap-1.5 text-sm">
          <span className="text-muted">Datum</span>
          <input
            type="date"
            value={entryDate}
            onChange={(e) => setEntryDate(e.target.value)}
            required
            className="rounded-lg border border-border bg-surface px-3 py-2 focus:outline-none focus:ring-2 focus:ring-accent/40"
          />
        </label>
        <label className="flex flex-col gap-1.5 text-sm">
          <span className="text-muted">Labor / Praxis (optional)</span>
          <input
            type="text"
            value={labName}
            onChange={(e) => setLabName(e.target.value)}
            placeholder="z. B. Hausarzt Dr. Muster"
            className="rounded-lg border border-border bg-surface px-3 py-2 focus:outline-none focus:ring-2 focus:ring-accent/40"
          />
        </label>
      </div>

      <div className="flex flex-col gap-2">
        <span className="text-sm text-muted">Werte</span>

        {rows.length > 0 && (
          <div className="flex flex-col gap-2">
            {rows.map((row) => {
              const p = paramByCode[row.parameter_code];
              if (!p) return null;
              return (
                <div key={row.parameter_code} className="flex items-center gap-2">
                  <span className="text-sm w-40 shrink-0 truncate" title={p.name}>{p.name}</span>
                  <input
                    type="text"
                    inputMode="decimal"
                    value={row.value}
                    onChange={(e) => updateRowValue(row.parameter_code, e.target.value)}
                    placeholder="Wert"
                    className="flex-1 rounded-lg border border-border bg-surface px-3 py-2 text-sm font-mono focus:outline-none focus:ring-2 focus:ring-accent/40"
                  />
                  <span className="text-xs text-muted w-16 shrink-0">{p.unit}</span>
                  <button
                    type="button"
                    onClick={() => removeRow(row.parameter_code)}
                    className="text-muted hover:text-status-high p-1"
                    aria-label={`${p.name} entfernen`}
                  >
                    <X size={16} />
                  </button>
                </div>
              );
            })}
          </div>
        )}

        <div className="flex items-center gap-2 mt-1">
          <select
            value={pickerCode}
            onChange={(e) => addRow(e.target.value)}
            className="flex-1 rounded-lg border border-border bg-surface px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-accent/40"
          >
            <option value="">Parameter hinzufügen…</option>
            {Object.entries(byCategory).map(([cat, params]) => (
              <optgroup key={cat} label={cat}>
                {params.map((p) => (
                  <option key={p.code} value={p.code} disabled={usedCodes.has(p.code)}>
                    {p.name}{usedCodes.has(p.code) ? " (bereits hinzugefügt)" : ""}
                  </option>
                ))}
              </optgroup>
            ))}
          </select>
          <Plus size={18} className="text-muted shrink-0" />
        </div>
      </div>

      <label className="flex flex-col gap-1.5 text-sm">
        <span className="text-muted">Notiz (optional)</span>
        <textarea
          value={note}
          onChange={(e) => setNote(e.target.value)}
          rows={2}
          className="rounded-lg border border-border bg-surface px-3 py-2 focus:outline-none focus:ring-2 focus:ring-accent/40"
        />
      </label>

      {error && <p className="text-sm text-status-high">{error}</p>}

      <div className="flex gap-3">
        <button
          type="submit"
          disabled={saving}
          className="bg-accent text-white text-sm font-medium px-4 py-2 rounded-lg hover:bg-accent-dark transition-colors disabled:opacity-60"
        >
          {saving ? "Speichert…" : "Eintrag speichern"}
        </button>
      </div>
    </form>
  );
}
