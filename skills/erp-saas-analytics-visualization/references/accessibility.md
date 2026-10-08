# Accessibility

- Every chart has a title, a one-sentence text summary, and a data table or CSV alternative.
- Do not use color alone: add labels, patterns, markers, or direct labels. Contrast >= 4.5:1 for text, 3:1 for graphical elements.
- Use a colorblind-safe palette; sequential for magnitude, diverging only around a meaningful midpoint, categorical <= 6 colors.
- Keyboard: focusable controls, visible focus, arrow-key navigation of data points where the library supports it; `aria-label`/`role="img"` with summary for canvas charts.
- Respect reduced motion; avoid auto-playing animation. Tooltips must be reachable by keyboard/touch.
- Locale-aware numbers/dates/currency; show units and time zone.
