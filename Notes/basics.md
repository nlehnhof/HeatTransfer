### Basics
```
1. Conduction: Heat transfer in a solid or a stationary fluid (gas or liquid) due to the
random motion of its constituent atoms, molecules and/or electrons.

2. Convection: Heat transfer due to the combined influence of bulk and random motion
for fluid flow over a surface.

3. Radiation: Rate of energy emitted by matter due to changes in the electron configurations
of its atoms or molecules and transported as electromagnetic waves

• Conduction and convection require the presence of temperature variations in a
material medium (e.g., gas, liquid, solid).
• Although radiation originates from matter, its transport does not require a material
medium and occurs most efficiently in a vacuum.
```

# Conduction
## Rate Equation
### Fourier’s Law of Heat Conduction

\[
q'' = -k \, \frac{dT}{dx}
\]

where:  
- \( q'' \) = heat flux \([W/m^2]\)  
- \( k \) = thermal conductivity \([W/(m\cdot K)]\)  
- \( \frac{dT}{dx} \) = temperature gradient \([K/m]\) or \([^\circ C/m]\)

---

### One-Dimensional Steady Conduction (Plane Wall)

For one-dimensional, steady-state conduction across a plane wall with constant thermal conductivity:

\[
q''_x = k \, \frac{T_1 - T_2}{L}
\]

where:  
- \( T_1, T_2 \) = temperatures at each wall surface  
- \( L \) = wall thickness

---

### Heat Transfer Rate

The total heat transfer rate is:

\[
q_x = q''_x \cdot A
\]

where:  
- \( A \) = cross-sectional area normal to heat flow


# Convection
## Rate Equation

Relation of convection to flow over a surface and development of velocity and thermal boundary layers.
Newton's Law of Cooling: 
\[
q'' = h \left( T_s - T_{\infty} \right)
\]

where:  
- \( q'' \) = heat flux \([W/m^2]\)  
- \( h \) = convection heat transfer coefficient \([W/(m^2 \cdot K)]\)  
- \( T_s \) = surface temperature  
- \( T_{\infty} \) = free-stream (ambient) fluid temperature

# Radiation
## Rate Equation

Thermal radiation exchange due to electromagnetic wave emission, dependent on surface temperature and surface properties. No medium is required for heat transfer.

Energy outflow due to emission:
\[
 E = \varepsilon E_b = \varepsilon \sigma T^4_s   
\]

where:
- \(\sigma \) : Stephan-Boltzman Constant of \(5.67 × 10^{−8} \frac{W}{m2 · K^4}\)

Energy absorption due to irradiation:
\[
G_{abs} = \alpha G
\]
where:
- \(G_{abs} \) : Absorbed incident radiation
- \(\alpha \) : Surface absorptivity (\(0 \leq \alpha \leq 1\))

If α < 1 and the surface is opaque, portions of the irradiation are reflected. If the surface is semitransparent, portions of the irradiation may also be transmitted. However, whereas absorbed and emitted radiation increase and reduce, respectively, the thermal energy of matter, reflected and transmitted radiation have no effect on this energy. Note that the value of α depends on the nature of the irradiation, as well as on the surface itself. For example, the absorptivity of a surface to solar radiation may differ from its absorptivity to radiation emitted by the walls of a furnace.

In many engineering problems (a notable exception being problems involving solar radiation or radiation from other very high temperature sources), liquids can be considered opaque to radiation heat transfer, and gases can be considered transparent to it. Solids can be opaque (as is the case for metals) or semitransparent (as is the case for thin sheets of some polymers and some semiconducting materials).


### Net Radiation Heat Flux
Stefan–Boltzmann Law:
\[
q'' = \varepsilon \sigma \left( T_s^4 - T_{\text{sur}}^4 \right)
\]

where:  
- Irration: special case of surface exposed to large (encompassed) surroundings of uniform temperature
- assume $\alpha = \varepsilon$
- \( q'' \) = radiative heat flux \([W/m^2]\)  
- \( \varepsilon \) = surface emissivity \((0 \le \varepsilon \le 1)\)  
- \( \sigma \) = Stefan–Boltzmann constant  
  \[
  \sigma = 5.67 \times 10^{-8} \; [W/(m^2 \cdot K^4)]
  \]
- \( T_s \) = surface temperature \([K]\)  
- \( T_{\text{sur}} \) = surrounding surface temperature \([K]\)

#### Convection form (linearized):
\[
h_r = \varepsilon \sigma (T_s + T_{sur})(T^2_s + T^2_{surr})
\]
\[
q'' = q''_{conv} + q''_{rad} = h(T_s - T_{\infty}) + h_r(T_s - T_{sur})
\]

Can compare relative contributions of convection and radiation.

