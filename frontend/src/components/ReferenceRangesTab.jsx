import React, { useEffect, useMemo, useState } from "react";
import { RotateCcw, Search } from "lucide-react";
import { api } from "../api";

export default function ReferenceRangesTab() {
  const [parameters, setParameters] = useState(null);
  const [error, setError] = useState(null);
  const [query, setQuery] = useState("");
  const [drafts, setDrafts] = useState({}); // code -> { low, high }
  const [savingCode, setSavingCode] = useState(null);
  const [savedCode, setSavedCode] = useState(null);

  function load() {
    api.getParameters().then((params) => {
      setParameters(params);
      setDrafts(
        Object.fromEntries(
          params.map((p) => [p.code, { low: p.reference_low ?? "", high: p.reference_high ?? "" }])
        )
      );
    }).catch((e) => setError(e.message));
  }

  useEffect(load, []);

  const filtered = useMemo(() => {
    if (!parameters) return [];
    const q = query.trim().toLowerCase();
    const list = parameters.filter((p) => !p.computed || p.code === "bmi"); // BMI range is still editable
    if (!q) return list;
    return list.filter((p) => p.name.toLowerCase().includes(q) || p.category.toLowerCase().includes(q));
  }, [parameters, query]);

  const byCategory = useMemo(() => {
    return filtered.reduce((acc, p) => {
      (acc[p.category] = acc[p.category] || []).push(p);
      return acc;
    }, {});
  }, [filtered]);

  function updateDraft(code, field, value) {
    setDrafts((d) => ({ ...d, [code]: { ...d[code], [field]: value } }));
  }

  async function save(code) {
    const draft = drafts[code];
    setSavingCode(code);
    try {
      const low = draft.low === "" ? null : parseFloat(String(draft.low).replace(",", "."));
      const high = draft.high === "" ? null : parseFloat(String(draft.high).replace(",", "."));
      await api.setOverride(code, { low, high });
      load();
      setSavedCode(code);
      setTimeout(() => setSavedCode(null), 1500);
    } catch (e) {
      setError(e.message);
    } finally {
      setSavingCode(null);
    }
  }

  async function reset(code) {
    setSavingCode(code);
    try {
      await api.setOverride(code, { low: null, high: null });
      load();
    } catch (e) {
      setError(e.message);
    } finally {
      setSavingCode(null);
    }
  }

  if (error) return <p className="text-status-high">Fehler beim Laden: {error}</p>;
  if (!parameters) return <p className="text-muted">Lade Parameter…</p>;

  return (
    <div className="flex flex-col gap-4">
      <p className="text-sm text-muted">
        Die vorausgefüllten Bereiche sind allgemeine Orientierungswerte. Trag hier die exakten
        Bereiche von deinem Labor ein, wenn sie abweichen — sie werden dann überall im Dashboard verwendet.
      </p>

      <div className="flex items-center gap-2 rounded-lg border border-border bg-surface px-3 py-2">
        <Search size={16} className="text-muted shrink-0" />
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Parameter suchen…"
          className="flex-1 outline-none bg-transparent text-sm"
        />
      </div>

      <div className="flex flex-col gap-5">
        {Object.entries(byCategory).map(([category, params]) => (
          <div key={category}>
            <h3 className="text-xs uppercase tracking-wide text-muted mb-2">{category}</h3>
            <div className="rounded-card border border-border bg-surface divide-y divide-border">
              {params.map((p) => {
                const draft = drafts[p.code] || { low: "", high: "" };
                return (
                  <div key={p.code} className="flex items-center gap-2 px-3 py-2.5 flex-wrap">
                    <div className="min-w-[9rem] flex-1">
                      <div className="text-sm">{p.name}</div>
                      <div className="text-xs text-muted">
                        {p.unit || "\u2014"}
                        {p.is_custom_range && <span className="text-accent"> · angepasst</span>}
                      </div>
                    </div>
                    <input
                      type="text"
                      inputMode="decimal"
                      value={draft.low}
                      onChange={(e) => updateDraft(p.code, "low", e.target.value)}
                      placeholder="min"
                      className="w-20 rounded-lg border border-border bg-paper px-2 py-1.5 text-sm font-mono focus:outline-none focus:ring-2 focus:ring-accent/40"
                    />
                    <span className="text-muted text-sm">&ndash;</span>
                    <input
                      type="text"
                      inputMode="decimal"
                      value={draft.high}
                      onChange={(e) => updateDraft(p.code, "high", e.target.value)}
                      placeholder="max"
                      className="w-20 rounded-lg border border-border bg-paper px-2 py-1.5 text-sm font-mono focus:outline-none focus:ring-2 focus:ring-accent/40"
                    />
                    <button
                      type="button"
                      onClick={() => save(p.code)}
                      disabled={savingCode === p.code}
                      className="text-xs font-medium text-white bg-accent hover:bg-accent-dark rounded-lg px-3 py-1.5 disabled:opacity-60"
                    >
                      {savedCode === p.code ? "Gespeichert" : "Speichern"}
                    </button>
                    {p.is_custom_range && (
                      <button
                        type="button"
                        onClick={() => reset(p.code)}
                        title="Auf Standardwert zurücksetzen"
                        className="text-muted hover:text-ink p-1.5"
                      >
                        <RotateCcw size={15} />
                      </button>
                    )}
                  </div>
                );
              })}
            </div>
          </div>
        ))}
        {filtered.length === 0 && <p className="text-sm text-muted">Kein Parameter gefunden.</p>}
      </div>
    </div>
  );
}
