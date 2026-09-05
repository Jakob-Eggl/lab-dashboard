/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        paper: "#F5F6F2",
        surface: "#FFFFFF",
        border: "#E2E5DF",
        ink: "#16302E",
        muted: "#6B7370",
        accent: {
          DEFAULT: "#2F6F6B",
          dark: "#1F4B48",
          light: "#E4EFED",
        },
        status: {
          normal: "#3F7D5C",
          normalBg: "#E9F3EC",
          high: "#C1502D",
          highBg: "#FBEAE3",
          low: "#3E6FA0",
          lowBg: "#E8EFF5",
          unknown: "#9BA19D",
          unknownBg: "#EDEEEB",
        },
      },
      fontFamily: {
        sans: [
          "-apple-system",
          "BlinkMacSystemFont",
          "Segoe UI",
          "Roboto",
          "Helvetica Neue",
          "Arial",
          "sans-serif",
        ],
        mono: [
          "ui-monospace",
          "SFMono-Regular",
          "Menlo",
          "Consolas",
          "Liberation Mono",
          "monospace",
        ],
      },
      borderRadius: {
        card: "10px",
      },
    },
  },
  plugins: [],
};
