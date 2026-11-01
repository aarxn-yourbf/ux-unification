export function EmptyState({ title, action }: { title: string; action?: React.ReactNode }) {
  return <div className="p-8 text-center text-muted"><p>{title}</p>{action}</div>;
}
