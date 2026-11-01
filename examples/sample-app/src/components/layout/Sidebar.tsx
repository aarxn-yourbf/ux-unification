import { NavLink } from "react-router-dom";
const navItems = [
  { section: "Investigation", items: [{ label: "Alerts", to: "/alerts", area: "alerts" }, { label: "Cases", to: "/cases", area: "cases" }] },
  { section: "Strategy", items: [{ label: "Rules", to: "/rules", area: "rules" }, { label: "Plans", to: "/plans", area: "plans" }] },
];
export function Sidebar() {
  return <nav className="w-56 border-r border-border p-4">{navItems.map(s => <div key={s.section}><p className="text-xs text-muted uppercase">{s.section}</p>{s.items.map(i => <NavLink key={i.to} to={i.to} className="block py-1">{i.label}</NavLink>)}</div>)}</nav>;
}
