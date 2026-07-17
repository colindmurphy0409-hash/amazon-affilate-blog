/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,ts,tsx}'],
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#f0fdf9',
          100: '#ccfbf1',
          200: '#99f6e4',
          400: '#2dd4bf',
          500: '#14b8a6',
          600: '#0d9488',
          700: '#0f766e',
          800: '#115e59',
          900: '#134e4a',
        },
        sage: {
          50: '#f4f7f4',
          100: '#e5ebe4',
          200: '#c9d8c8',
          400: '#7a9e7a',
          500: '#5f8a5f',
          600: '#4a7354',
          700: '#3d5f46',
        },
        coral: {
          50: '#fff5f2',
          100: '#ffe8e2',
          200: '#ffd0c4',
          400: '#f4846a',
          500: '#e86f5a',
          600: '#d45a48',
          700: '#b84838',
        },
        gold: {
          50: '#fdfaf3',
          100: '#f9f0dc',
          200: '#f0ddb0',
          400: '#d4a84b',
          500: '#c9952e',
          600: '#a67c23',
        },
        ink: {
          DEFAULT: '#0f172a',
          muted: '#475569',
          faint: '#94a3b8',
        },
        surface: {
          DEFAULT: '#ffffff',
          soft: '#f8fafc',
          muted: '#f1f5f9',
          warm: '#faf8f5',
        },
        amazon: {
          DEFAULT: '#ff9900',
          dark: '#e47911',
        },
        category: {
          beauty: {
            DEFAULT: '#e86f5a',
            light: '#fff5f2',
            dark: '#d45a48',
            ring: '#ffd0c4',
          },
          fitness: {
            DEFAULT: '#14b8a6',
            light: '#f0fdf9',
            dark: '#0f766e',
            ring: '#99f6e4',
          },
          home: {
            DEFAULT: '#5f8a5f',
            light: '#f4f7f4',
            dark: '#4a7354',
            ring: '#c9d8c8',
          },
        },
      },
      fontFamily: {
        sans: ['"Source Sans 3"', 'system-ui', 'sans-serif'],
        display: ['"Fraunces"', 'Georgia', 'serif'],
      },
      boxShadow: {
        card: '0 1px 3px rgba(15, 23, 42, 0.06), 0 8px 24px rgba(15, 23, 42, 0.06)',
        lift: '0 12px 40px rgba(15, 23, 42, 0.12)',
        glow: '0 0 40px rgba(20, 184, 166, 0.15)',
      },
      backgroundImage: {
        'mesh-hero':
          'radial-gradient(ellipse 80% 60% at 10% 20%, rgba(20,184,166,0.18), transparent 50%), radial-gradient(ellipse 60% 50% at 90% 10%, rgba(232,111,90,0.14), transparent 45%), radial-gradient(ellipse 70% 60% at 70% 90%, rgba(201,149,46,0.12), transparent 50%), radial-gradient(ellipse 50% 40% at 20% 80%, rgba(95,138,95,0.12), transparent 45%)',
        'body-pattern':
          'radial-gradient(circle at 1px 1px, rgba(15,23,42,0.04) 1px, transparent 0)',
      },
    },
  },
  plugins: [require('@tailwindcss/typography')],
};
