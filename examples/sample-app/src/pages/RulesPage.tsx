import { useNavigate } from "react-router-dom";
import { DataTable } from "../components/ui/DataTable";
import { PageHeader } from "../components/ui/PageHeader";
import { StatusBadge } from "../components/ui/StatusBadge";
import { Button } from "../components/ui/Button";
export function RulesPage() {
  const nav = useNavigate();
  return (
    <>
      <PageHeader title="Rules" actions={<Button>New rule</Button>} />
      <DataTable columns={[{ key: "name", header: "Rule" }, { key: "status", header: "Status", render: (r: any) => <StatusBadge status={r.status} /> }]} rows={[]} onRowClick={(r: any) => nav(`/rules/${r.id}`)} />
    </>
  );
}
