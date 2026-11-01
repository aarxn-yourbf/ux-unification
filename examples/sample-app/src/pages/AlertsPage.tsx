import { DataTable } from "../components/ui/DataTable";
import { PageHeader } from "../components/ui/PageHeader";
import { StatusBadge } from "../components/ui/StatusBadge";
export function AlertsPage() {
  return <><PageHeader title="Alerts" /><DataTable columns={[{ key: "id", header: "Alert" }, { key: "status", header: "Status", render: (r: any) => <StatusBadge status={r.status} /> }]} rows={[]} /></>;
}
