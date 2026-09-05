import React from "react";
import { Link } from "react-router-dom";
import { ArrowUp, ArrowDown, Minus } from "lucide-react";

const STATUS_STYLES = {
  normal: { bar: "bg-status-normal", text: "text-status-normal", bg: "bg-status-normalBg", label: "im Bereich" },
  high: { bar: "bg-status-high", text: "text-status-high", bg: "bg-status-highBg", label: "erhöht" },
  low: { bar: "bg-status-low", text: "text-status-low", bg: "bg-status-lowBg", label: "erniedrigt" },
  unknown: { bar: "bg-status-unknown", text: "text-status-unknown", bg: "bg-status-unknownBg", label: "keine Daten" },
};

function formatDate(d) {
  if (!d) return "";
  return new Date(d).toLocaleDateString("de-DE", { day: "2-digit", month: "2-digit", year: "numeric" });
}

export default function ParameterCard({ item }) {
  const style = STATUS_STYLES[item.status] || STATUS_STYLES.unknown;
  const { parameter } = item;

  let trend = null;
  if (item.latest_value != null && item.previous_value != null) {
    const diff = item.latest_value - item.previous_value;
    if (Math.abs(diff) > 1e-9) {
      trend = diff > 0 ? "up" : "down";
    } else {
      trend = "flat";
    }
  }

  return (
    <Link
      to={`/parameter/${parameter.code}`}
      className="group relative flex flex-col gap-2 rounded-card border border-border bg-surface p-4 hover:border-accent/40 transition-colors"
    >
      <span className={`absolute left-0 top-0 h-full w-1 rounded-l-card ${style.bar}`} />
      <div className="pl-2 flex items-start justify-between gap-2">
        <div>
          <div className="text-sm font-medium text-ink leading-tight">{parameter.name}</div>
          <div className="text-xs text-muted mt-0.5">{parameter.category}</div>
        </div>
        <span className={`text-[11px] px-1.5 py-0.5 rounded ${style.bg} ${style.text} whitespace-nowrap`}>
          {style.label}
        </span>
      </div>

      <div className="pl-2 flex items-end gap-2 mt-1">
        {item.latest_value != null ? (
          <>
            <span className="font-mono tabular text-2xl text-ink leading-none">
              {item.latest_value}
            </span>
            <span className="text-xs text-muted mb-0.5">{item.unit}</span>
            {trend && (
              <span className="ml-auto flex items-center text-muted mb-0.5">
                {trend === "up" && <ArrowUp size={15} />}
                {trend === "down" && <ArrowDown size={15} />}
                {trend === "flat" && <Minus size={15} />}
              </span>
            )}
          </>
        ) : (
          <span className="text-sm text-muted">Noch kein Wert erfasst</span>
        )}
      </div>

      <div className="pl-2 flex items-center justify-between text-xs text-muted">
        <span>
          {parameter.reference_low != null
            ? `Referenz: ${parameter.reference_low}\u2013${parameter.reference_high} ${parameter.unit}`
            : "Kein Referenzbereich hinterlegt"}
        </span>
        <span>{formatDate(item.latest_date)}</span>
      </div>
    </Link>
  );
}
