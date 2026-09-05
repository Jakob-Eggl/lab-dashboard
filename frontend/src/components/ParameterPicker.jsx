import React, { useEffect, useMemo, useRef, useState } from "react";
import { Search, X } from "lucide-react";

export default function ParameterPicker({ parameters, usedCodes, onPick }) {
  const [open, setOpen] = useState(false);
  const [query, setQuery] = useState("");
  const containerRef = useRef(null);
  const inputRef = useRef(null);

  useEffect(() => {
    function handleClickOutside(e) {
      if (containerRef.current && !containerRef.current.contains(e.target)) {
        setOpen(false);
      }
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  const filtered = useMemo(() => {
    const q = query.trim().toLowerCase();
    const selectable = parameters.filter((p) => !p.computed);
    const matches = q
      ? selectable.filter(
          (p) =>
            p.name.toLowerCase().includes(q) ||
            p.full_name.toLowerCase().includes(q) ||
            p.category.toLowerCase().includes(q)
        )
      : selectable;

    const byCategory = matches.reduce((acc, p) => {
      (acc[p.category] = acc[p.category] || []).push(p);
      return acc;
    }, {});
    return byCategory;
  }, [parameters, query]);

  function pick(code) {
    if (usedCodes.has(code)) return;
    onPick(code);
    setQuery("");
    setOpen(false);
  }

  const hasResults = Object.keys(filtered).length > 0;

  return (
    <div ref={containerRef} className="relative">
      <div
        onClick={() => {
          setOpen(true);
          inputRef.current?.focus();
        }}
        className="flex items-center gap-2 rounded-lg border border-border bg-surface px-3 py-2 cursor-text focus-within:ring-2 focus-within:ring-accent/40"
      >
        <Search size={16} className="text-muted shrink-0" />
        <input
          ref={inputRef}
          type="text"
          value={query}
          onChange={(e) => {
            setQuery(e.target.value);
            setOpen(true);
          }}
          onFocus={() => setOpen(true)}
          placeholder="Parameter suchen und hinzufügen…"
          className="flex-1 outline-none bg-transparent text-sm min-w-0"
        />
        {query && (
          <button
            type="button"
            onClick={(e) => {
              e.stopPropagation();
              setQuery("");
              inputRef.current?.focus();
            }}
            className="text-muted hover:text-ink shrink-0"
          >
            <X size={15} />
          </button>
        )}
      </div>

      {open && (
        <div className="absolute z-20 mt-1 w-full max-h-72 overflow-y-auto rounded-lg border border-border bg-surface shadow-lg">
          {!hasResults && (
            <div className="px-3 py-3 text-sm text-muted">Kein Parameter gefunden.</div>
          )}
          {Object.entries(filtered).map(([category, params]) => (
            <div key={category}>
              <div className="px-3 pt-2 pb-1 text-[11px] uppercase tracking-wide text-muted sticky top-0 bg-surface">
                {category}
              </div>
              {params.map((p) => {
                const disabled = usedCodes.has(p.code);
                return (
                  <button
                    type="button"
                    key={p.code}
                    disabled={disabled}
                    onClick={() => pick(p.code)}
                    className={`w-full flex items-center justify-between gap-2 px-3 py-2 text-sm text-left ${
                      disabled ? "text-muted/60 cursor-not-allowed" : "hover:bg-accent-light"
                    }`}
                  >
                    <span>{p.name}</span>
                    <span className="text-xs text-muted shrink-0">
                      {disabled ? "hinzugefügt" : p.unit}
                    </span>
                  </button>
                );
              })}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
