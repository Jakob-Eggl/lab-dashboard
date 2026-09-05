import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { api } from "../api";
import ParameterCard from "./ParameterCard";

export default function Dashboard() {
  const [items, setItems] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    api.getDashboard().then(setItems).catch((e) => setError(e.message));
  }, []);

  if (error) {
    return <p className="text-status-high">Fehler beim Laden: {error}</p>;
  }
  if (!items) {
    return <p className="text-muted">Lade Werte…</p>;
  }

  const hasAnyData = items.some((i) => i.latest_value != null);

  const byCategory = items.reduce((acc, item) => {
    const cat = item.parameter.category;
    (acc[cat] = acc[cat] || []).push(item);
    return acc;
  }, {});

  const outOfRange = items.filter((i) => i.status === "high" || i.status === "low");

  return (
    <div className="flex flex-col gap-8">
      <div className="flex items-start justify-between gap-4 flex-wrap">
        <div>
          <h1 className="text-xl font-semibold tracking-tight">Übersicht</h1>
          <p className="text-sm text-muted mt-1">Deine letzten Laborwerte auf einen Blick.</p>
        </div>
        <Link
          to="/neu"
          className="text-sm font-medium bg-accent text-white px-4 py-2 rounded-lg hover:bg-accent-dark transition-colors"
        >
          + Neuer Eintrag
        </Link>
      </div>

      {!hasAnyData && (
        <div className="rounded-card border border-dashed border-border p-8 text-center text-muted">
          Noch keine Werte erfasst. Leg mit deinem ersten Befund los.
          <div className="mt-4">
            <Link to="/neu" className="text-accent font-medium hover:underline">
              Ersten Eintrag anlegen →
            </Link>
          </div>
        </div>
      )}

      {outOfRange.length > 0 && (
        <div>
          <h2 className="text-sm font-medium text-muted mb-3">Außerhalb des Referenzbereichs</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
            {outOfRange.map((item) => (
              <ParameterCard key={item.parameter.code} item={item} />
            ))}
          </div>
        </div>
      )}

      {Object.entries(byCategory).map(([category, catItems]) => (
        <div key={category}>
          <h2 className="text-sm font-medium text-muted mb-3">{category}</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
            {catItems.map((item) => (
              <ParameterCard key={item.parameter.code} item={item} />
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}
