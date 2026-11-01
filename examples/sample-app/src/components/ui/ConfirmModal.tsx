import { Button } from "./Button";
type Props = { open: boolean; title: string; message: string; confirmText?: string; onConfirm: () => void; onCancel: () => void };
export function ConfirmModal({ open, title, message, confirmText = "Delete", onConfirm, onCancel }: Props) {
  if (!open) return null;
  return (
    <div role="dialog" className="fixed inset-0 bg-black/40 grid place-items-center">
      <div className="bg-surface rounded-card p-6 w-96">
        <h2 className="font-semibold">{title}</h2><p className="text-muted">{message}</p>
        <div className="flex justify-end gap-2 mt-4"><Button variant="secondary" onClick={onCancel}>Cancel</Button><Button variant="danger" onClick={onConfirm}>{confirmText}</Button></div>
      </div>
    </div>
  );
}
