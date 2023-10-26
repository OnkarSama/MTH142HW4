import numpy as np
import matplotlib.pyplot as plt

# Given differential equation function
def dP_dt(P):
    return P * (1 - P)

# Create a meshgrid for P values
P_values = np.linspace(-1, 2, 20)
t_values = np.linspace(-1, 2, 20)

# Create a 2D grid of P, t values
P, t = np.meshgrid(P_values, t_values)

# Calculate the slope at each point in the grid
dP = dP_dt(P)

# Plot the slope field
plt.figure(figsize=(8, 6))
plt.quiver(t, P, np.ones_like(dP), dP, angles='xy', scale=17, color='blue', width=0.003)

# Plot stable and unstable equilibria
plt.axhline(y=0, color='red', linestyle='--', label='Unstable Equilibrium')
plt.axhline(y=1, color='green', linestyle='--', label='Stable Equilibrium')

# Set plot limits
plt.xlim([0, 2])
plt.ylim([-1, 2])

# Add labels and legend
plt.xlabel('t')
plt.ylabel('P')
plt.title('Slope Field for dP/dt = P(1 - P)')
plt.legend()

# Show the plot
plt.show()
