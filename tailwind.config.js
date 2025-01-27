// tailwind.config.js
module.exports = {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        roboto: ["Roboto", "sans-serif"],
      },
      colors: {
        bgPrimary: "rgb(var(--color-bg-primary) / <alpha-value>)",
        bgSecondary: "rgb(var(--color-bg-secondary) / <alpha-value>)",
        textPrimary: "rgb(var(--color-text-primary) / <alpha-value>)",
        textGray: "rgb(var(--color-text-gray) / <alpha-value>)",
        bgLinear: "rgb(var(--color-bg-linear) / <alpha-value>)",
        primaryColor: "rgb(var(--color-primary) / <alpha-value>)",

        bgLinear: "rgb(var(--color-bg-linear) / <alpha-value>)",
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
