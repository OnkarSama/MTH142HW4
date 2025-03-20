import numpy as np
import matplotlib.pyplot as plt

# Function to define the SIR model equations
def sir_model(s, i, beta, gamma):
    ds = -beta * s * i
    di = beta * s * i - gamma * i
    return ds, di

# Set the parameters for the SIR model
beta = 0.3  # Infection rate
gamma = 0.1  # Recovery rate

# Create a grid of points in the SI phase plane
s_values = np.linspace(0, 1, 20)
i_values = np.linspace(0, 1, 20)
s_grid, i_grid = np.meshgrid(s_values, i_values)

# Adjust U and V components directly to control the length of quivers
U = -beta * s_grid * i_grid
V = beta * s_grid * i_grid - gamma * i_grid

# Create a phase plane plot
plt.figure(figsize=(8, 6))

# Plot the quivers
plt.quiver(s_grid, i_grid, U, V, angles='xy', scale=1, color='blue', width=0.008)

# Plot multiple trajectories with different initial conditions
for s_init in [0.05, 0.1, 0.3, 0.5, 0.7, 0.9]:  # Add more initial conditions
    i_init = 1 - s_init
    s_trajectory, i_trajectory = [], []

    for _ in range(100):
        s_trajectory.append(s_init)
        i_trajectory.append(i_init)
        ds, di = sir_model(s_init, i_init, beta, gamma)
        s_init += ds
        i_init += di

    plt.plot(s_trajectory, i_trajectory, label=f'Initial S(t) = {s_trajectory[0]:.2f}', linewidth=5)

# Add labels and title
plt.xlabel('S(t)')
plt.ylabel('I(t)')
plt.title('SI Phase Plane of SIR Model')

# Add the line N = s + i
plt.plot(s_values, 1 - s_values, color='red', linestyle='-', label='N = S(t) + I(t)', linewidth=2)

# Show the legend
plt.legend()

# Show the plot
plt.show()
