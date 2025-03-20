import numpy as np
import matplotlib.pyplot as plt

# Function to define the differential equations
def sir_model(s, i, a, b):
    ds = -a * s * i
    di = a * s * i - b * i
    return ds, di

# Function to calculate dI/dS
def dI_dS(s, i, a, b):
    return (a * s - b) / (-a * s)

# Function to check if a point is above the N = S + I line
def is_above_line(s, i):
    return i <= 1 - s

# Set the parameters for the SIR model
a = 0.3  # Infection rate
b = 0.1  # Recovery rate

# Create a grid of points in the SI phase plane
s_values = np.linspace(0.01, 1, 20)
i_values = np.linspace(0.01, 1, 20)
s_grid, i_grid = np.meshgrid(s_values, i_values)

# Calculate the derivatives at each point in the grid
dsdt_grid, didt_grid = sir_model(s_grid, i_grid, a, b)

# Calculate dI/dS at each point in the grid
dI_dS_grid = dI_dS(s_grid, i_grid, a, b)

# Create a phase plane plot with quiver and slope field
plt.figure(figsize=(10, 8))

# Plot the quivers
plt.quiver(s_grid, i_grid, dsdt_grid, didt_grid, angles='xy', scale=2, color='blue', width=0.008)

# Plot the I-nullcline
I_nullcline = (b / a) * np.ones_like(i_values)
plt.plot(I_nullcline, i_values, color='green', linewidth=5, linestyle='--', label='I-nullcline')

# Plot the slope field
plt.streamplot(s_grid, i_grid, dsdt_grid, didt_grid, color='grey', linewidth=0.5, density=1, arrowstyle='->', arrowsize=1.5)

# Plot trajectories
for _ in range(10):
    s_init, i_init = np.random.uniform(0.01, 1), np.random.uniform(0.01, 1)
    s_trajectory, i_trajectory = [], []

    for _ in range(100):
        s_trajectory.append(s_init)
        i_trajectory.append(i_init)
        ds, di = sir_model(s_init, i_init, a, b)
        s_init += ds
        i_init += di

        # Stop trajectory if it crosses the N = S + I line
        if not is_above_line(s_init, i_init):
            break

    plt.plot(s_trajectory, i_trajectory, label=f'Trajectory ({s_trajectory[0]:.2f}, {i_trajectory[0]:.2f})', linewidth=2)

plt.plot(s_values, 1 - s_values, color='red', linestyle='-', label='N = S(t) + I(t)', linewidth=2)

# Add labels and title
plt.xlabel('S(t)')
plt.ylabel('I(t)')
plt.title('SI Phase Plane with I-nullcline, Slope Field, and Trajectories (Stopping at N = S + I)')

# Show the legend
plt.legend()

# Show the plot
plt.show()
