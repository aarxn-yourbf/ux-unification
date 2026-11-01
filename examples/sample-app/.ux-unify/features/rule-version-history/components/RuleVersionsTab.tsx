// Proposed: src/pages/rules/RuleVersionsTab.tsx (or next to RuleDetailPage.tsx)
// Uses only existing components: DataTable (+selectable), StatusBadge (+archived),
// Button, ConfirmModal (+confirmVariant), EmptyState. No new dependencies or tokens.
import { useState } from "react";
import { DataTable, Column } from "../../components/ui/DataTable";
import { StatusBadge } from "../../components/ui/StatusBadge";
import { Button } from "../../components/ui/Button";
import { ConfirmModal } from "../../components/ui/ConfirmModal";
import { EmptyState } from "../../components/ui/EmptyState";
import { hasPermission, Role } from "../../auth/permissions";
import { VersionDiff, RuleCondition } from "./VersionDiff";

export type RuleVersion = {
  id: string;
  version: number;
  status: "active" | "archived";
  author: string;
  savedAt: string; // formatted date, same format as elsewhere
  summary: string;
  conditions: RuleCondition[];
};

type Props = {
  versions: RuleVersion[];
  role: Role;
  loading?: boolean;
  error?: boolean;
  onRetry?: () => void;
  onRestore: (version: RuleVersion) => Promise<void>;
};

export function RuleVersionsTab({ versions, role, loading, error, onRetry, onRestore }: Props) {
  const [selected, setSelected] = useState<string[]>([]);
  const [comparing, setComparing] = useState(false);
  const [toRestore, setToRestore] = useState<RuleVersion | null>(null);
  const [restoring, setRestoring] = useState(false);

  // Convention (global-patterns.md): hide actions the role cannot perform.
  const canRestore = hasPermission(role, "rules") && role === "data_scientist";
  const nextVersion = Math.max(0, ...versions.map(v => v.version)) + 1;

  if (error) {
    return <EmptyState title="Couldn't load versions. Try again." action={<Button variant="secondary" onClick={onRetry}>Try again</Button>} />;
  }
  if (!loading && versions.length <= 1) {
    return <EmptyState title="This rule has only one version. Versions appear here each time you save changes." />;
  }

  const columns: Column<RuleVersion>[] = [
    { key: "version", header: "Version", render: v => `Version ${v.version}` },
    { key: "status", header: "Status", render: v => <StatusBadge status={v.status} /> },
    { key: "author", header: "Author" },
    { key: "savedAt", header: "Saved" },
    { key: "summary", header: "Summary" },
  ];
  if (canRestore) {
    columns.push({
      key: "id",
      header: "",
      render: v => v.status === "active" ? null : <Button variant="secondary" onClick={() => setToRestore(v)}>Restore version</Button>,
    });
  }

  const pair = versions.filter(v => selected.includes(v.id)).sort((a, b) => a.version - b.version);

  return (
    <div className="pt-4">
      <div className="flex justify-between items-center mb-3">
        <p className="text-muted">Select two versions to compare</p>
        <Button variant="secondary" onClick={() => setComparing(true)} disabled={selected.length !== 2}>Compare</Button>
      </div>

      <DataTable
        columns={columns}
        rows={versions}
        loading={loading}
        selectable
        maxSelected={2}
        selectedIds={selected}
        getRowId={v => v.id}
        getRowLabel={v => `Select version ${v.version}`}
        onSelectionChange={ids => { setSelected(ids); setComparing(false); }}
      />

      {comparing && pair.length === 2 && (
        <VersionDiff before={pair[0]} after={pair[1]} onClose={() => setComparing(false)} />
      )}

      <ConfirmModal
        open={!!toRestore}
        title={`Restore version ${toRestore?.version}?`}
        message={`This creates version ${nextVersion} with the same conditions as version ${toRestore?.version}. The current version stays in the history.`}
        confirmText={restoring ? "Restoring…" : "Restore version"}
        confirmVariant="primary"
        onCancel={() => setToRestore(null)}
        onConfirm={async () => {
          if (!toRestore) return;
          setRestoring(true);
          await onRestore(toRestore);
          setRestoring(false);
          setToRestore(null);
        }}
      />
    </div>
  );
}
