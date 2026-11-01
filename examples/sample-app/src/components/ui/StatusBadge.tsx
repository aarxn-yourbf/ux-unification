const tone = { active: "bg-green-100 text-green-800", draft: "bg-gray-100 text-muted", paused: "bg-yellow-100 text-yellow-800" };
export function StatusBadge({ status }: { status: keyof typeof tone }) {
  return <span className={`px-2 py-0.5 rounded-full text-xs ${tone[status]}`}>{status}</span>;
}
