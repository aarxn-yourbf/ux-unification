export type Role = "analyst" | "data_scientist" | "manager";
export const permissions: Record<string, Role[]> = {
  alerts: ["analyst", "manager"],
  cases: ["analyst", "manager"],
  rules: ["data_scientist", "manager"],
  plans: ["data_scientist"],
};
export function hasPermission(role: Role, area: string) {
  return permissions[area]?.includes(role) ?? false;
}
