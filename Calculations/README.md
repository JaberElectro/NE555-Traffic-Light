# Timing Calculations

## Equations (standard astable)

| Quantity | Formula |
|---|---|
| T<sub>HIGH</sub> | 0.693 (R<sub>A</sub> + R<sub>B</sub>) C |
| T<sub>LOW</sub> | 0.693 R<sub>B</sub> C |
| Period T | 0.693 (R<sub>A</sub> + 2R<sub>B</sub>) C |
| Duty cycle | (R<sub>A</sub> + R<sub>B</sub>) / (R<sub>A</sub> + 2R<sub>B</sub>) |

The 0.693 is ln 2. It comes from the capacitor charging from ⅓ to ⅔ V<sub>CC</sub>, a ratio of exactly 2 in the remaining voltage.

## Design values

| Design | R<sub>A</sub> | R<sub>B</sub> | C | T<sub>HIGH</sub> | T<sub>LOW</sub> | Period | Duty |
|---|---|---|---|---|---|---|---|
| A: two-phase lights | 1 kΩ | 47 kΩ | 100 µF | 3.33 s | 3.26 s | 6.58 s | 50.5 % |
| B: CD4017 clock | 10 kΩ | 68 kΩ | 10 µF | 0.54 s | 0.47 s | 1.01 s | 53.4 % |
| Equal resistors (counter-example) | 47 kΩ | 47 kΩ | 100 µF | 6.51 s | 3.26 s | 9.77 s | 66.7 % |

## Design checks

- **R<sub>A</sub> minimum:** when the output goes low, pin 7 shorts the top of R<sub>B</sub> to ground, so R<sub>A</sub> alone limits current from V<sub>CC</sub>: 5 V / 1 kΩ = 5 mA, well within the discharge transistor's rating.
- **LED current:** (5 V − 2.0 V) / 220 Ω ≈ 14 mA, within the 555's output capability and a normal LED's rating.
- **Tolerance:** with a ±20 % electrolytic, the real Config A period can fall anywhere from about 5.3 s to 7.9 s.

## Reproduce

```bash
python ne555_calc.py                    # design values above
python ne555_calc.py 1000 47000 100e-6  # any RA RB C
```
