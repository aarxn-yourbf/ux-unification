import { ReactNode } from "react";
import { EmptyState } from "./EmptyState";
export type Column<T> = { key: keyof T; header: string; render?: (row: T) => ReactNode };
type Props<T> = { columns: Column<T>[]; rows: T[]; loading?: boolean; onRowClick?: (row: T) => void };
export function DataTable<T>({ columns, rows, loading, onRowClick }: Props<T>) {
  if (loading) return <div className="animate-pulse h-32 bg-surface" />;
  if (!rows.length) return <EmptyState title="Nothing here yet" />;
  return (
    <table className="w-full border border-border rounded-card">
      <thead><tr>{columns.map(c => <th key={String(c.key)} className="text-left p-2 text-muted">{c.header}</th>)}</tr></thead>
      <tbody>{rows.map((r, i) => <tr key={i} onClick={() => onRowClick?.(r)}>{columns.map(c => <td key={String(c.key)} className="p-2">{c.render ? c.render(r) : String(r[c.key])}</td>)}</tr>)}</tbody>
    </table>
  );
}
