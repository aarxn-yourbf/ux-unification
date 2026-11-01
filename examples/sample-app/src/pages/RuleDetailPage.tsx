import { useState } from "react";
import { PageHeader } from "../components/ui/PageHeader";
import { Tabs } from "../components/ui/Tabs";
import { Button } from "../components/ui/Button";
import { ConfirmModal } from "../components/ui/ConfirmModal";
export function RuleDetailPage() {
  const [tab, setTab] = useState("definition");
  const [confirm, setConfirm] = useState(false);
  return (
    <>
      <PageHeader title="Rule detail" actions={<><Button variant="secondary">Save changes</Button><Button variant="danger" onClick={() => setConfirm(true)}>Delete</Button></>} />
      <Tabs tabs={[{ id: "definition", label: "Definition" }, { id: "performance", label: "Performance" }]} active={tab} onChange={setTab} />
      <ConfirmModal open={confirm} title="Delete rule?" message="This rule will stop scoring transactions." onConfirm={() => setConfirm(false)} onCancel={() => setConfirm(false)} />
    </>
  );
}
