import { ReactNode } from "react";
type Props = { variant?: "primary" | "secondary" | "danger"; children: ReactNode; onClick?: () => void };
export function Button({ variant = "primary", children, onClick }: Props) {
  const styles = { primary: "bg-primary text-white", secondary: "border border-border", danger: "bg-danger text-white" };
  return <button className={`px-3 py-2 rounded-md ${styles[variant]}`} onClick={onClick}>{children}</button>;
}
