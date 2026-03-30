import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# ----------------------
# Material & geometry
# ----------------------
rho = 2700        # kg/m3
c = 885           # J/kg·K
L = 0.01          # m (thickness)

# ----------------------
# Cooling conditions
# ----------------------
T_air = 25 + 273.15     # K
h = 100                 # W/m2·K
epsilon = 0.8
sigma = 5.67e-8         # W/m2·K4

# ----------------------
# ODE function for lumped cooling
# ----------------------
def dTdt(t, T):
    # Convection
    q_conv = h * (T - T_air)
    # Radiation
    q_rad = epsilon * sigma * (T**4 - T_air**4)
    # Lumped capacitance: dT/dt = -q_net / (rho c L)
    return -(q_conv + q_rad) / (rho * c * L)

# ----------------------
# Initial & final temperatures
# ----------------------
T0 = 750 + 273.15   # K
T_safe = 40 + 273.15  # K

# ----------------------
# Solve ODE
# ----------------------
sol = solve_ivp(dTdt, t_span=(0, 3600), y0=[T0], max_step=1, dense_output=True)

# ----------------------
# Find time to reach T_safe
# ----------------------
t_vals = sol.t
T_vals = sol.y[0]

# Interpolate to find exact time for T_safe
from scipy.interpolate import interp1d
f = interp1d(T_vals, t_vals)
t_safe_sec = f(T_safe)
t_safe_min = t_safe_sec / 60
print(f"Time to cool to 40°C: {t_safe_min:.2f} minutes")

# ----------------------
# Plot
# ----------------------
plt.figure(figsize=(6,4))
plt.plot(t_vals/60, T_vals-273.15)
plt.axhline(40, color='red', linestyle='--', label='Safe-to-touch 40°C')
plt.xlabel('Time [min]')
plt.ylabel('Temperature [°C]')
plt.title('Cooling of Workpiece')
plt.grid(True)
plt.legend()
plt.show()