rho = 1.225
V = 5.0 # m/s
S = 0.26*2 * 0.08 # 52 cm span, 8 cm chord = 0.035 m2
Cl = 0.9 # low Re estimate for NACA 4412

# Lift in Newtons
L = 0.5 * rho * (V**2) * S * Cl
# Weight in grams (g = 9.81 m/s^2)
weight_g = (L / 9.81) * 1000
print(f"S={S:.1f}, L={L:.1f}, weight_g={weight_g:.0f}")
