type Tab = { id: string; label: string };
export function Tabs({ tabs, active, onChange }: { tabs: Tab[]; active: string; onChange: (id: string) => void }) {
  return <div className="flex gap-4 border-b border-border">{tabs.map(t => <button key={t.id} onClick={() => onChange(t.id)} className={t.id === active ? "border-b-2 border-primary" : "text-muted"}>{t.label}</button>)}</div>;
}
