"""NE555 astable timing calculator.

Usage:
    python ne555_calc.py                 # runs the project's design values
    python ne555_calc.py 1000 47000 100e-6
"""
import sys

LN2 = 0.693


def astable(ra, rb, c):
    t_high = LN2 * (ra + rb) * c
    t_low = LN2 * rb * c
    period = t_high + t_low
    return {
        "T_HIGH (s)": t_high,
        "T_LOW (s)": t_low,
        "Period (s)": period,
        "Frequency (Hz)": 1 / period,
        "Duty cycle (%)": 100 * t_high / period,
    }


def show(label, ra, rb, c):
    print(f"\n{label}:  RA = {ra:g} Ω, RB = {rb:g} Ω, C = {c:g} F")
    for k, v in astable(ra, rb, c).items():
        print(f"  {k:<16} {v:.3f}")


if len(sys.argv) == 4:
    show("Custom", *map(float, sys.argv[1:]))
else:
    show("Config A: two-phase", 1e3, 47e3, 100e-6)
    show("Config B: clock for CD4017", 10e3, 68e3, 10e-6)
    show("Equal resistors (shows the duty-cycle trap)", 47e3, 47e3, 100e-6)
