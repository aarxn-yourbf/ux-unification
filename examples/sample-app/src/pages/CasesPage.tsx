import { useState } from "react";
import { PageHeader } from "../components/ui/PageHeader";
import { DeleteDialog } from "../components/ui/DeleteDialog";
export function CasesPage() {
  const [del, setDel] = useState(false);
  return (
    <>
      <PageHeader title="Cases" />
      <table className="w-full"><thead><tr><th>Case</th><th>Owner</th></tr></thead><tbody /></table>
      <DeleteDialog show={del} onYes={() => setDel(false)} onNo={() => setDel(false)} />
    </>
  );
}
