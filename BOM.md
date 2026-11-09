# Bill of Materials

### Configuration A: two-phase

| Qty | Part | Value | Notes |
|---|---|---|---|
| 1 | Timer IC | NE555N (DIP-8) | Confirmed original component |
| 1 | Resistor | 1 kΩ | R<sub>A</sub> |
| 1 | Resistor | 47 kΩ | R<sub>B</sub> |
| 1 | Electrolytic capacitor | 100 µF, ≥ 16 V | Timing C |
| 1 | Ceramic capacitor | 10 nF | Pin 5 decoupling |
| 1 | Ceramic capacitor | 100 nF | Supply decoupling, close to pin 8 |
| 3 | LED | Red, Yellow, Green | |
| 3 | Resistor | 220 Ω | LED current limiting |
| 1 | DC supply | 5 V | |

### Additional for Configuration B: three-phase

| Qty | Part | Value | Notes |
|---|---|---|---|
| 1 | Decade counter | CD4017B | |
| 9 | Signal diode | 1N4148 | Diode-OR for red (5) and green (4) |
| 1 | Resistor | 10 kΩ | R<sub>A</sub> (replaces 1 kΩ) |
| 1 | Resistor | 68 kΩ | R<sub>B</sub> (replaces 47 kΩ) |
| 1 | Electrolytic capacitor | 10 µF | Timing C (replaces 100 µF) |
| 3 | NPN transistor | 2N2222 / BC547 | Optional LED buffers |
