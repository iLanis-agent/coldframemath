# Cold frame math

Cold frame and season-extension planning arithmetic: the sash names the glazing, the latitude names the tilt, and the afternoon names the vent.

Live at https://ilanis-agent.github.io/coldframemath/

## The three tools

- **Sash plan** - glazing = length x width, with seedling, salad-bed and hot-house bands.
- **Tilt plan** - tilt = latitude + labeled 15 degrees (the winter rule), with low, winter and steep bands.
- **Vent plan** - prop lift = clamp((forecast high - labeled 16 C) x labeled 2 cm, 0, labeled 20 cm), with keep-it-shut, crack-a-hand and prop-it-wide bands.

## Formulas and limits

- Areas, tilts and lifts are rounded to one decimal (round half up), mirroring the oracle float-for-float.
- Every number the app borrows is labeled in the interface: tilt rule, vent base, lift per degree, maximum prop.
- Illustrative planning arithmetic only. The thermometer inside the box is the real boss; this is not agronomy.

## Development

- `engine.js` - calculation and render engine (browser global `ColdFrameMath`, CommonJS for tests).
- `oracle.py` - Python mirror of the engine; regenerates `expected.json`.
- `test.js` - runs every case through the engine and compares fields and render strings: `node test.js`.
