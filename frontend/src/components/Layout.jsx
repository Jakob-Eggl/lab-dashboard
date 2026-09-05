import React from "react";
import { NavLink, Outlet } from "react-router-dom";
import { LayoutGrid, PlusCircle, ListOrdered, Settings2, Droplet } from "lucide-react";

const NAV_ITEMS = [
  { to: "/", label: "Übersicht", icon: LayoutGrid, end: true },
  { to: "/neu", label: "Neuer Eintrag", icon: PlusCircle },
  { to: "/eintraege", label: "Alle Einträge", icon: ListOrdered },
  { to: "/einstellungen", label: "Einstellungen", icon: Settings2 },
];

function NavItems({ orientation }) {
  const isRow = orientation === "row";
  return (
    <>
      {NAV_ITEMS.map(({ to, label, icon: Icon, end }) => (
        <NavLink
          key={to}
          to={to}
          end={end}
          className={({ isActive }) =>
            [
              "flex items-center gap-3 rounded-lg transition-colors",
              isRow
                ? "flex-col gap-1 px-2 py-1.5 text-[11px] flex-1 justify-center"
                : "px-3 py-2 text-sm w-full",
              isActive
                ? "text-accent-dark bg-accent-light font-medium"
                : "text-muted hover:text-ink hover:bg-black/[0.03]",
            ].join(" ")
          }
        >
          <Icon size={isRow ? 20 : 18} strokeWidth={2} />
          <span>{label}</span>
        </NavLink>
      ))}
    </>
  );
}

export default function Layout() {
  return (
    <div className="min-h-full flex flex-col md:flex-row">
      {/* Desktop side rail */}
      <aside className="hidden md:flex md:w-60 md:flex-col md:border-r md:border-border md:bg-surface md:px-3 md:py-5 md:sticky md:top-0 md:h-screen">
        <div className="flex items-center gap-2 px-2 pb-6">
          <Droplet size={22} className="text-accent" strokeWidth={2.2} />
          <span className="text-[15px] font-semibold tracking-tight">Laborwerte</span>
        </div>
        <nav className="flex flex-col gap-1">
          <NavItems orientation="column" />
        </nav>
        <div className="mt-auto px-2 pt-6 text-xs text-muted leading-relaxed">
          Alle Daten bleiben auf deinem Server. Keine Diagnose &ndash; nur Verlauf.
        </div>
      </aside>

      {/* Mobile top bar */}
      <header className="md:hidden flex items-center gap-2 px-4 py-3 border-b border-border bg-surface sticky top-0 z-10">
        <Droplet size={20} className="text-accent" strokeWidth={2.2} />
        <span className="text-[15px] font-semibold tracking-tight">Laborwerte</span>
      </header>

      <main className="flex-1 px-4 py-5 md:px-8 md:py-8 pb-20 md:pb-8 max-w-5xl w-full mx-auto">
        <Outlet />
      </main>

      {/* Mobile bottom tab bar */}
      <nav className="md:hidden fixed bottom-0 left-0 right-0 bg-surface border-t border-border flex px-1 py-1 z-10">
        <NavItems orientation="row" />
      </nav>
    </div>
  );
}
