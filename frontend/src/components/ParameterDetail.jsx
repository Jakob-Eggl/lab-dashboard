import React, { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import {
  ResponsiveContainer, LineChart, Line, XAxis, YAxis, Tooltip,
  ReferenceArea, CartesianGrid,
} from "recharts";
import { ChevronLeft } from "lucide-react";
import { api } from "../api";

function formatDate(d) {
  return new Date(d).toLocaleDateString("de-DE", { day: "2-digit", month: "2-digit", year: "numeric" });
}

export default function ParameterDetail() {
  const { code } = useParams();
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    setData(null);
    api.getHistory(code).then(setData).catch((e) => setError(e.message));
  }, [code]);

  if (error) return <p className="text-status-high">Fehler beim Laden: {error}</p>;
  if (!data) return <p className="text-muted">Lade Verlauf…</p>;

  const { parameter, points } = data;
  const chartData = points.map((p) => ({ ...p, dateLabel: formatDate(p.date) }));

  const hasRange = parameter.reference_low != null && parameter.reference_high != null;
  const values = points.map((p) => p.value);
  const yMin = hasRange ? Math.min(parameter.reference_low, ...values) : Math.min(...values, 0);
  const yMax = hasRange ? Math.max(parameter.reference_high, ...values) : Math.max(...values, 1);
  const pad = (yMax - yMin) * 0.15 || 1;

  return (
    <div className="flex flex-col gap-6">
      <Link to="/" className="inline-flex items-center gap-1 text-sm text-muted hover:text-ink w-fit">
        <ChevronLeft size={16} /> Übersicht
      </Link>

      <div>
        <h1 className="text-xl font-semibold tracking-tight">{parameter.name}</h1>
        <p className="text-sm text-muted mt-1">{parameter.full_name}</p>
      </div>

      {points.length === 0 ? (
        <div className="rounded-card border border-dashed border-border p-8 text-center text-muted">
          Für diesen Parameter liegen noch keine Werte vor.
        </div>
      ) : (
        <div className="rounded-card border border-border bg-surface p-4">
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={chartData} margin={{ top: 10, right: 16, left: 0, bottom: 0 }}>
                <CartesianGrid stroke="#E2E5DF" vertical={false} />
                <XAxis dataKey="dateLabel" tick={{ fontSize: 11, fill: "#6B7370" }} axisLine={{ stroke: "#E2E5DF" }} tickLine={false} />
                <YAxis
                  domain={[yMin - pad, yMax + pad]}
                  tick={{ fontSize: 11, fill: "#6B7370" }}
                  axisLine={false}
                  tickLine={false}
                  width={40}
                />
                {hasRange && (
                  <ReferenceArea
                    y1={parameter.reference_low}
                    y2={parameter.reference_high}
                    fill="#2F6F6B"
                    fillOpacity={0.08}
                    stroke="none"
                  />
                )}
                <Tooltip
                  formatter={(value) => [`${value} ${parameter.unit}`, parameter.name]}
                  labelStyle={{ color: "#16302E", fontWeight: 500 }}
                  contentStyle={{ borderRadius: 8, border: "1px solid #E2E5DF", fontSize: 13 }}
                />
                <Line
                  type="monotone"
                  dataKey="value"
                  stroke="#2F6F6B"
                  strokeWidth={2}
                  dot={{ r: 4, fill: "#2F6F6B" }}
                  activeDot={{ r: 6 }}
                />
              </LineChart>
            </ResponsiveContainer>
          </div>
          {hasRange && (
            <p className="text-xs text-muted mt-2">
              Grüner Bereich: allgemeiner Referenzbereich ({parameter.reference_low}&ndash;{parameter.reference_high} {parameter.unit}).
              Kann je nach Labor leicht abweichen &ndash; massgeblich ist der auf deinem Befund angegebene Bereich.
            </p>
          )}
        </div>
      )}

      <div className="rounded-card border border-border bg-surface p-4 flex flex-col gap-3">
        <h2 className="text-sm font-medium">Über {parameter.name}</h2>
        <p className="text-sm text-ink/90 leading-relaxed">{parameter.description}</p>
        <div className="grid sm:grid-cols-2 gap-3 mt-1">
          <div className="rounded-lg bg-status-highBg p-3">
            <div className="text-xs font-medium text-status-high mb-1">Bei erhöhten Werten</div>
            <p className="text-sm text-ink/90 leading-relaxed">{parameter.high_meaning}</p>
          </div>
          <div className="rounded-lg bg-status-lowBg p-3">
            <div className="text-xs font-medium text-status-low mb-1">Bei niedrigen Werten</div>
            <p className="text-sm text-ink/90 leading-relaxed">{parameter.low_meaning}</p>
          </div>
        </div>
        <p className="text-xs text-muted mt-1">
          Nur zur Orientierung, keine medizinische Beratung. Auffällige Werte bitte mit deinem Arzt/deiner Ärztin besprechen.
        </p>
      </div>

      {points.length > 0 && (
        <div className="rounded-card border border-border bg-surface overflow-hidden">
          <table className="w-full text-sm">
            <thead>
              <tr className="text-left text-xs text-muted border-b border-border">
                <th className="px-4 py-2 font-medium">Datum</th>
                <th className="px-4 py-2 font-medium">Wert</th>
              </tr>
            </thead>
            <tbody>
              {[...points].reverse().map((p) => (
                <tr key={p.entry_id + "-" + p.date} className="border-b border-border last:border-0">
                  <td className="px-4 py-2 text-muted">{formatDate(p.date)}</td>
                  <td className="px-4 py-2 font-mono tabular">{p.value} {parameter.unit}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
