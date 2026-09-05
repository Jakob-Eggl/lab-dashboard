import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { Pencil, Trash2, ChevronDown, ChevronUp } from "lucide-react";
import { api } from "../api";

function formatDate(d) {
  return new Date(d).toLocaleDateString("de-DE", { day: "2-digit", month: "2-digit", year: "numeric" });
}

export default function EntryList() {
  const [entries, setEntries] = useState(null);
  const [parametersByCode, setParametersByCode] = useState({});
  const [error, setError] = useState(null);
  const [openId, setOpenId] = useState(null);

  function load() {
    Promise.all([api.getEntries(), api.getParameters()])
      .then(([entries, params]) => {
        setEntries(entries);
        setParametersByCode(Object.fromEntries(params.map((p) => [p.code, p])));
      })
      .catch((e) => setError(e.message));
  }

  useEffect(load, []);

  async function handleDelete(id) {
    if (!confirm("Diesen Eintrag wirklich löschen?")) return;
    await api.deleteEntry(id);
    load();
  }

  if (error) return <p className="text-status-high">Fehler beim Laden: {error}</p>;
  if (!entries) return <p className="text-muted">Lade Einträge…</p>;

  return (
    <div className="flex flex-col gap-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-xl font-semibold tracking-tight">Alle Einträge</h1>
          <p className="text-sm text-muted mt-1">{entries.length} Befund{entries.length === 1 ? "" : "e"} erfasst.</p>
        </div>
        <Link to="/neu" className="text-sm font-medium bg-accent text-white px-4 py-2 rounded-lg hover:bg-accent-dark transition-colors">
          + Neu
        </Link>
      </div>

      {entries.length === 0 && (
        <div className="rounded-card border border-dashed border-border p-8 text-center text-muted">
          Noch keine Einträge vorhanden.
        </div>
      )}

      <div className="flex flex-col gap-3">
        {entries.map((entry) => {
          const isOpen = openId === entry.id;
          return (
            <div key={entry.id} className="rounded-card border border-border bg-surface overflow-hidden">
              <button
                type="button"
                onClick={() => setOpenId(isOpen ? null : entry.id)}
                className="w-full flex items-center justify-between px-4 py-3 text-left"
              >
                <div>
                  <div className="text-sm font-medium">{formatDate(entry.entry_date)}</div>
                  <div className="text-xs text-muted mt-0.5">
                    {entry.lab_name || "Ohne Laborangabe"} &middot; {entry.measurements.length} Wert{entry.measurements.length === 1 ? "" : "e"}
                  </div>
                </div>
                <div className="flex items-center gap-1 text-muted">
                  <Link
                    to={`/eintraege/${entry.id}/bearbeiten`}
                    onClick={(e) => e.stopPropagation()}
                    className="p-2 hover:text-accent"
                    aria-label="Bearbeiten"
                  >
                    <Pencil size={16} />
                  </Link>
                  <span
                    onClick={(e) => { e.stopPropagation(); handleDelete(entry.id); }}
                    className="p-2 hover:text-status-high cursor-pointer"
                    aria-label="Löschen"
                  >
                    <Trash2 size={16} />
                  </span>
                  {isOpen ? <ChevronUp size={18} /> : <ChevronDown size={18} />}
                </div>
              </button>
              {isOpen && (
                <div className="px-4 pb-4 border-t border-border pt-3">
                  {entry.note && <p className="text-sm text-muted italic mb-3">{entry.note}</p>}
                  <table className="w-full text-sm">
                    <tbody>
                      {entry.measurements.map((m) => {
                        const p = parametersByCode[m.parameter_code];
                        return (
                          <tr key={m.id} className="border-b border-border last:border-0">
                            <td className="py-1.5 pr-3">{p ? p.name : m.parameter_code}</td>
                            <td className="py-1.5 font-mono tabular">
                              {m.value} {p ? p.unit : (m.unit_override || "")}
                            </td>
                          </tr>
                        );
                      })}
                    </tbody>
                  </table>
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}
