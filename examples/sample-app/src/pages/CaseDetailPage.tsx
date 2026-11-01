import { useState } from "react";
import { PageHeader } from "../components/ui/PageHeader";
import { Tabs } from "../components/ui/Tabs";
export function CaseDetailPage() {
  const [tab, setTab] = useState("overview");
  return <><PageHeader title="Case" /><Tabs tabs={[{ id: "overview", label: "Overview" }, { id: "activity", label: "Activity" }]} active={tab} onChange={setTab} /></>;
}
