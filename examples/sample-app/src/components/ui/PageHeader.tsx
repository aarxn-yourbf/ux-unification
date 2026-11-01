import { ReactNode } from "react";
export function PageHeader({ title, actions }: { title: string; actions?: ReactNode }) {
  return <header className="flex justify-between items-center mb-6"><h1 className="text-2xl font-semibold">{title}</h1><div>{actions}</div></header>;
}
