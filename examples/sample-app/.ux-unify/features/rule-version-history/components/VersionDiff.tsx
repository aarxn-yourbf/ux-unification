// Proposed: src/components/ui/VersionDiff.tsx — NEW pattern (Create).
// Reason: no comparison view exists in the product (patterns.md). Built only from
// existing tokens (border, surface, muted, danger, primary, rounded-card) so it
// matches the rest of the UI. Generic enough for any versioned object.
export type RuleCondition = { field: string; operator: string; value: string };
type Side = { version: number; savedAt: string; conditions: RuleCondition[] };

const key = (c: RuleCondition) => `${c.field} ${c.operator} ${c.value}`;

export function VersionDiff({ before, after, onClose }: { before: Side; after: Side; onClose: () => void }) {
  const beforeKeys = new Set(before.conditions.map(key));
  const afterKeys = new Set(after.conditions.map(key));
  const column = (side: Side, other: Set<string>, mark: "removed" | "added") => (
    <div className="flex-1 border border-border rounded-card bg-surface">
      <p className="p-3 border-b border-border font-semibold">Version {side.version} · <span className="text-muted font-normal">{side.savedAt}</span></p>
      <ul className="p-3 space-y-1 font-mono text-sm">
        {side.conditions.map(c => {
          const changed = !other.has(key(c));
          const prefix = changed ? (mark === "removed" ? "−" : "+") : " ";
          const tone = changed ? (mark === "removed" ? "text-danger" : "text-primary") : "";
          return <li key={key(c)} className={tone}><span aria-hidden>{prefix} </span>{key(c)}{changed && <span className="sr-only"> ({mark})</span>}</li>;
        })}
      </ul>
    </div>
  );
  return (
    <section className="mt-6" aria-label="Version comparison">
      <div className="flex justify-between items-center mb-3">
        <h2 className="font-semibold">Compare versions</h2>
        <button className="text-muted" onClick={onClose}>Close comparison</button>
      </div>
      <div className="flex gap-4">
        {column(before, afterKeys, "removed")}
        {column(after, beforeKeys, "added")}
      </div>
    </section>
  );
}
