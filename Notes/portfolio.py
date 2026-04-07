import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# -------------------------------
# GIVEN PROPERTIES
# -------------------------------
T_inf = 300           # Ambient air temperature [K]
sigma = 5.67e-8       # Stefan-Boltzmann constant [W/m²·K⁴]
alpha_nom = 0.91      # Absorptivity
epsilon = 0.94        # Emissivity
q_solar = 800         # Solar irradiance [W/m²]
h_nom = 10            # Convective coefficient [W/m²·K]

# -------------------------------
# ENERGY BALANCE FUNCTION
# -------------------------------
def energy_balance(Ts, alpha, epsilon, q_solar, h, T_inf):
    return alpha*q_solar - h*(Ts - T_inf) - epsilon*sigma*(Ts**4 - T_inf**4)

# -------------------------------
# BASE CASE
# -------------------------------
T_w_base = fsolve(lambda T: energy_balance(T, alpha_nom, epsilon, q_solar, h_nom, T_inf), T_inf)[0]
print(f"Steady-state water temperature: {T_w_base:.1f} K ({T_w_base - 273.15:.1f} °C)")

# -------------------------------
# SENSITIVITY ANALYSIS 1: Absorptivity
# -------------------------------
alpha_values = np.linspace(0.6, 0.95, 8)
T_w_alpha = [fsolve(lambda T: energy_balance(T, a, epsilon, q_solar, h_nom, T_inf), T_inf)[0] for a in alpha_values]

plt.figure(figsize=(6,4))
plt.plot(alpha_values, np.array(T_w_alpha)-273.15, marker='o', color='darkred')
plt.xlabel("Absorptivity α")
plt.ylabel("Water Temperature [°C]")
# plt.title("Sensitivity of Water Temperature to Absorptivity")
plt.grid(False)
plt.show()

# -------------------------------
# SENSITIVITY ANALYSIS 2: Convection
# -------------------------------
h_values = np.linspace(5, 25, 9)
T_w_h = [fsolve(lambda T: energy_balance(T, alpha_nom, epsilon, q_solar, h_val, T_inf), T_inf)[0] for h_val in h_values]

plt.figure(figsize=(6,4))
plt.plot(h_values, np.array(T_w_h)-273.15, marker='s', color='blue')
plt.xlabel("Convective Coefficient h [W/m²·K]")
plt.ylabel("Water Temperature [°C]")
# plt.title("Sensitivity of Water Temperature to Convection Coefficient")
plt.grid(False)
plt.show()