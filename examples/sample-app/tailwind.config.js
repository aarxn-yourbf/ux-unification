module.exports = {
  content: ["./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: "var(--color-primary)",
        surface: "var(--color-surface)",
        border: "var(--color-border)",
        danger: "var(--color-danger)",
        muted: "var(--color-muted)",
      },
      borderRadius: { card: "var(--radius-card)" },
    },
  },
};
