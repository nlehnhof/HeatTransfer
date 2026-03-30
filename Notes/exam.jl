# Oven wall consisting of insulation. k = 0.04, oven air is at T = 320 *C with h = 35. Surface of the inside oven wall absorbs radiant flux of 100 from the oven. Outer air is at 25 degrees C with h of 12.
# Assume steady-state, one d, constant properties, negligible contact resistance, negligible radiation from outside sources.
# What insulation thickness L is required to maintain the outer wall temp at T = 45 *C.

# air | insulation | air
# q conv + q rad | q cond | q conv
# q conv + q rad = q cond = q conv
# q conv = 12 * (45 - 25) = 240 W/m^2
# q cond = k * (320 - 45) / L = 0.04 * 275 / L = 11 / L W/m^2
# q rad = 100 W/m^2
# 240 + 100 = 11 / L
# L = 11 / 340
# Prove it
# q_conv_out = 12 * (45 - 25)
# q_cond = 0.04 * (320 - 45) / L
# q_rad = 100
# Why don't I need to find the inner wall temperature?
# Because the inner wall temperature is not needed to solve for the insulation thickness. The problem states that the surface of the inside oven wall absorbs a radiant flux of 100 W/m^2, which means that the inner wall temperature is not directly relevant to the calculation of the insulation thickness. The key factors in determining the insulation thickness are the convective heat transfer on the outer surface and the conductive heat transfer through the insulation, which are both influenced by the temperatures and properties given in the problem.
# How do I know that the q conv = q cond?
# In steady-state heat transfer, the rate of heat transfer through the system must be constant. This means that the heat transfer by convection on the outer surface must equal the heat transfer by conduction through the insulation, which in turn must equal the heat transfer by convection on the inner surface. Therefore, we can set q_conv (outer) + q_rad = q_cond = q_conv (inner). Since we are given that the radiant flux absorbed by the inner wall is 100 W/m^2, we can include that in our calculations to find the required insulation thickness.
# Calculate the required insulation thickness L to maintain the outer wall temperature at 45 degrees C.
q_conv_out = 12 * (45 - 25) # W/m^2
q_rad = 100 # W/m^2
q_cond = q_conv_out + q_rad # W/m^2
k = 0.04 # W/m*K
T_inner = 320 # degrees C
T_outer = 45 # degrees C
L = k * (T_inner - T_outer) / q_cond # m
println("The required insulation thickness L is: ", L, " meters")
# But what about the convection from the oven to the first inner wall? Doesn't that add some flux?
# The convection from the oven to the first inner wall does contribute to the heat transfer, but in this problem, we are given that the surface of the inside oven wall absorbs a radiant flux of 100 W/m^2. This means that the radiant heat transfer is already accounted for in the problem statement, and we can focus on the convective heat transfer on the outer surface and the conductive heat transfer through the insulation to find the required insulation thickness. The key point is that we are looking for a steady-state solution where the total heat transfer (convective + radiant) on the inner surface equals the conductive heat transfer through the insulation, which in turn equals the convective heat transfer on the outer surface.
# But aren't they separate? The radiant flux is absorbed, and the convection is a separate mechanism. Shouldn't I add them together to get the total heat transfer from the oven to the inner wall?
# You are correct that the radiant flux and the convective heat transfer are separate mechanisms. In this problem, we are given that the surface of the inside oven wall absorbs a radiant flux of 100 W/m^2, which means that this radiant heat transfer is already included in the total heat transfer from the oven to the inner wall. Therefore, when calculating the total heat transfer from the oven to the inner wall, we should indeed add the convective heat transfer to the radiant heat transfer to get the total heat transfer. However, since we are ultimately interested in finding the insulation thickness required to maintain a certain outer wall temperature, we can focus on the balance of heat transfer at steady state, where the total heat transfer from the oven (convective + radiant) must equal the conductive heat transfer through the insulation, which in turn must equal the convective heat transfer on the outer surface.
# We can ignore the inner wall convection because at steady-state, the inner wall temperature will be the same as the oven air temperature, so there will be no convective heat transfer from the oven to the inner wall. Therefore, we can focus on the radiant heat transfer and the conductive heat transfer through the insulation to find the required insulation thickness. The key point is that at steady state, the total heat transfer from the oven (radiant) must equal the conductive heat transfer through the insulation, which in turn must equal the convective heat transfer on the outer surface.
# That's because the conduction needs to account only for the temperature difference between the inner wall and the outer wall, which is 320 - 45 = 275 degrees C. The convective heat transfer from the oven to the inner wall is not relevant to the calculation of the insulation thickness because it does not affect the temperature difference across the insulation. The radiant heat transfer is already accounted for in the problem statement, so we can focus on the conductive heat transfer through the insulation to find the required thickness.
# But how do we know for sure that at steady-state the inner wall temperature will be the same as the oven air temperature? Isn't it possible that the inner wall temperature could be different due to the radiant heat transfer?
# You are correct that the inner wall temperature could be different from the oven air temperature due to the radiant heat transfer. However, in this problem, we are given that the surface of the inside oven wall absorbs a radiant flux of 100 W/m^2, which means that the inner wall temperature will be influenced by both the convective heat transfer from the oven air and the radiant heat transfer. At steady state, the inner wall temperature will adjust to a value where the total heat transfer (convective + radiant) from the oven to the inner wall equals the conductive heat transfer through the insulation. Therefore, while it is possible for the inner wall temperature to be different from the oven air temperature, we can still solve for the required insulation thickness by considering the balance of heat transfer at steady state.
# So we can focus on the balance of heat transfer at steady state, where the total heat transfer from the oven (convective + radiant) must equal the conductive heat transfer through the insulation, which in turn must equal the convective heat transfer on the outer surface. This allows us to find the required insulation thickness without needing to explicitly calculate the inner wall temperature, as it will be determined by the balance of heat transfer in the system.
# Like so, we can set up the equations as follows:
# q_conv_out = h_out * (T_outer - T_ambient)
# q_rad = 100 W/m^2
# q_cond = k * (T_inner - T_outer) / L
# At steady state, we have:
# q_conv_out + q_rad = q_cond
# Substituting the expressions for q_conv_out and q_cond, we get:
# h_out * (T_outer - T_ambient) + 100 = k * (T_inner - T_outer) / L
# Rearranging the equation to solve for L, we have:
# L = k * (T_inner - T_outer) / (h_out * (T_outer - T_ambient) + 100)
# Now we can plug in the values to calculate the required insulation thickness L.
h_out = 12 # W/m^2*K
T_ambient = 25 # degrees C
L = k * (T_inner - T_outer) / (h_out * (T_outer - T_ambient) + q_rad)
println("The required insulation thickness L is: ", L, " meters")