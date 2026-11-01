// Older dialog, still used on Cases page
export function DeleteDialog({ show, onYes, onNo }: { show: boolean; onYes: () => void; onNo: () => void }) {
  if (!show) return null;
  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center">
      <div style={{ background: "#fff", borderRadius: 4, padding: 16 }}>
        <p>Are you sure?</p>
        <button onClick={onYes} style={{ color: "#b91c1c" }}>Yes</button>
        <button onClick={onNo}>No</button>
      </div>
    </div>
  );
}
