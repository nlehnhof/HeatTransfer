import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# GIVEN PROPERTIES
# -------------------------------
T_s = 330             # Bottle surface temperature [K]
T_inf = 300           # Ambient air temperature [K]
sigma = 5.67e-8       # Stefan-Boltzmann constant [W/m²·K⁴]
alpha_nom = 0.85      # Absorptivity of black powder coating
epsilon = 0.9         # Emissivity of black powder coating
q_solar = 800         # Solar irradiance [W/m²]
h_nom = 10            # Convective heat transfer coefficient [W/m²·K]
A = 0.03              # Surface area [m²]

# -------------------------------
# FUNCTION TO CALCULATE STEADY-STATE WATER TEMPERATURE
# -------------------------------
def water_temperature(Ts, alpha, epsilon, q_solar, sigma, h, T_inf):
    """
    Ts: bottle surface temperature [K]
    alpha: surface absorptivity
    epsilon: surface emissivity
    q_solar: solar irradiance [W/m²]
    sigma: Stefan-Boltzmann constant
    h: convective coefficient [W/m²·K]
    T_inf: ambient temperature [K]
    """
    q_rad = epsilon * sigma * (Ts**4 - T_inf**4)
    q_net = alpha * q_solar - q_rad
    T_w = Ts - q_net / h
    return T_w

# -------------------------------
# BASE CASE
# -------------------------------
T_w_base = water_temperature(T_s, alpha_nom, epsilon, q_solar, sigma, h_nom, T_inf)
print(f"Steady-state water temperature: {T_w_base:.1f} K ({T_w_base - 273.15:.1f} °C)")

# -------------------------------
# SENSITIVITY ANALYSIS 1: Absorptivity
# -------------------------------
alpha_values = np.linspace(0.6, 0.95, 8)
T_w_alpha = [water_temperature(T_s, a, epsilon, q_solar, sigma, h_nom, T_inf) for a in alpha_values]

plt.figure(figsize=(6,4))
plt.plot(alpha_values, np.array(T_w_alpha)-273.15, marker='o', color='black')
plt.xlabel("Absorptivity α")
plt.ylabel("Water Temperature [°C]")
# plt.title("Sensitivity: Water Temperature vs. Absorptivity")
plt.grid(False)
plt.show()

# -------------------------------
# SENSITIVITY ANALYSIS 2: Convective Coefficient h
# -------------------------------
h_values = np.linspace(5, 25, 9)
T_w_h = [water_temperature(T_s, alpha_nom, epsilon, q_solar, sigma, h_val, T_inf) for h_val in h_values]

plt.figure(figsize=(6,4))
plt.plot(h_values, np.array(T_w_h)-273.15, marker='s', color='blue')
plt.xlabel("Convective Coefficient h [W/m²·K]")
plt.ylabel("Water Temperature [°C]")
# plt.title("Sensitivity: Water Temperature vs. Convective Coefficient")
plt.grid(False)
plt.show()