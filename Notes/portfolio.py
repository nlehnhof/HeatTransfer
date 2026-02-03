import numpy as np
import matplotlib.pyplot as plt

# Enable interactive plotting so figures don't block
plt.ion()

# -----------------------------
# Given constants
# -----------------------------
Q_total = 10.0          # W, heat dissipation from phone
T_inf = 20.0            # °C, ambient air temperature
h = 50.0                # W/m^2·K, convection coefficient
A_base = 0.06 * 0.124   # m^2, phone back surface area

fin_lengths = np.linspace(0.001, 0.1, 100)  # 1 mm to 100 mm

# -----------------------------
# Material properties (W/m·K)
# -----------------------------
materials = {
    "Aluminum 2024-T6": 177,
    "AISI 302 Stainless Steel": 15.1,
    "White Pine Wood": 0.11,
    "Clay": 1.3
}

# -----------------------------
# Fin array options
# -----------------------------
fin_arrays = {
    "10 fins, 5mm dia": (10, 0.005),
    "20 fins, 3mm dia": (20, 0.003),
    "30 fins, 1mm dia": (30, 0.001)
}

# -----------------------------
# Fin efficiency (cylindrical fin, adiabatic tip)
# -----------------------------
def fin_efficiency(k, D, L, h):
    m = np.sqrt(4 * h / (k * D))
    Lc = L + D / 4
    return np.tanh(m * Lc) / (m * Lc)

# -----------------------------
# Base temperature calculation
# -----------------------------
def phone_temp(Q, k, L, h, N, D, A_base, T_inf):
    # Corrected fin length
    Lc = L + D / 4

    # Fin efficiency
    m = np.sqrt(4 * h / (k * D))
    eta = np.tanh(m * Lc) / (m * Lc)

    # Areas
    A_fin = np.pi * D * Lc                     # one fin (lateral)
    A_base_free = A_base - N * np.pi * (D/2)**2
    A_base_free = max(A_base_free, 0.0)

    # Explicit heat balance
    T_base = T_inf + Q / (
        h * A_base_free + N * eta * h * A_fin
    )

    return T_base, eta

# =====================================================
# 1) Phone temp vs fin length for different materials
# =====================================================
array_choice = "20 fins, 3mm dia"
N_fins, D = fin_arrays[array_choice]

plt.figure()
for material, k in materials.items():
    temps = []
    for L in fin_lengths:
        T_base, _ = phone_temp(Q_total, k, L, h, N_fins, D, A_base, T_inf)
        temps.append(T_base)
    plt.plot(fin_lengths * 1000, temps, label=material)

plt.xlabel("Fin Length (mm)")
plt.ylabel("Phone Surface Temperature (°C)")
# plt.title(f"Phone Surface Temperature vs Fin Length\n({array_choice})")
plt.legend()
plt.grid(False)
plt.show(block=False)
plt.savefig("materials_vs_length.png", dpi=300)

# =====================================================
# 2) Phone temp vs fin length for different fin arrays
# =====================================================
material_choice = "Aluminum 2024-T6"
k = materials[material_choice]

plt.figure()
for array_name, (N_fins, D) in fin_arrays.items():
    temps = []
    for L in fin_lengths:
        T_base, _ = phone_temp(Q_total, k, L, h, N_fins, D, A_base, T_inf)
        temps.append(T_base)
    plt.plot(fin_lengths * 1000, temps, label=array_name)

plt.xlabel("Fin Length (mm)")
plt.ylabel("Phone Surface Temperature (°C)")
# plt.title(f"Phone Surface Temperature vs Fin Length\n(Material: {material_choice})")
plt.legend()
plt.grid(False)
plt.show(block=False)
plt.savefig("length_vs_phone_temp_arrays.png", dpi=300)


# =====================================================
# 3) Optimal design example
# =====================================================
N_opt, D_opt = fin_arrays["20 fins, 3mm dia"]
k_opt = materials["Aluminum 2024-T6"]

temps_opt = []
eff_opt = []

for L in fin_lengths:
    T_base, eta = phone_temp(Q_total, k_opt, L, h, N_opt, D_opt, A_base, T_inf)
    temps_opt.append(T_base)
    eff_opt.append(eta)

plt.figure()
plt.plot(fin_lengths * 1000, temps_opt)
plt.xlabel("Fin Length (mm)")
plt.ylabel("Phone Surface Temperature (°C)")
# plt.title("Phone Surface Temperature vs Fin Length\n(Optimal Design)")
plt.grid(False)
plt.show(block=False)
plt.savefig("temps_vs_length_optimal.png", dpi=300)


# =====================================================
# 4) Fin efficiency vs fin length
# =====================================================
plt.figure()
plt.plot(fin_lengths * 1000, eff_opt)
plt.xlabel("Fin Length (mm)")
plt.ylabel("Fin Efficiency")
# plt.title("Fin Efficiency vs Fin Length\n(Optimal Design)")
plt.grid(False)
plt.show(block=False)
plt.savefig("efficiency_vs_length.png", dpi=300)


# # =====================================================
# # 5) Minimum fin length for η ≥ 0.75
# # =====================================================
# for L, T, eta in zip(fin_lengths, temps_opt, eff_opt):
#     if eta >= 0.75:
#         print(
#             f"Selected fin length: {L*1000:.1f} mm | "
#             f"Phone Temp: {T:.2f} °C | "
#             f"Fin Efficiency: {eta:.2f}"
#         )
#         break

input("\nPress Enter to close all plots...")
plt.close("all")
