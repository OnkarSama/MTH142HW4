import numpy as np
import matplotlib.pyplot as plt

# Given differential equation function for S
def dS_dt(a, S, I):
    return -a * S * I

# Given differential equation function for I
def dI_dt(a, b, S, I):
    return a * S * I - b * I

# Given differential equation function for R
def dR_dt(b, I):
    return b * I

# Euler's method for the SIR model
def euler_sir_model(initial_S, initial_I, initial_R, a, b, delta_t, num_iterations):
    results = [("Iteration", "t", "S(t)", "I(t)", "R(t)", "New t", "New S(t)", "New I(t)", "New R(t)")]

    S = initial_S
    I = initial_I
    R = initial_R

    t = 0
    for i in range(1, num_iterations + 1):
        dS = dS_dt(a, S, I)
        dI = dI_dt(a, b, S, I)
        dR = dR_dt(b, I)

        new_t = t + delta_t
        new_S = S + dS * delta_t
        new_I = I + dI * delta_t
        new_R = R + dR * delta_t

        results.append((i, round(t, 3), round(S, 3), round(I, 3), round(R, 3),
                        round(new_t, 3), round(new_S, 3), round(new_I, 3), round(new_R, 3)))

        t, S, I, R = new_t, new_S, new_I, new_R

    return results

def main():
    # Initial conditions for the SIR model
    initial_S = 999000
    initial_I = 1000
    initial_R = 0.0

    # Parameters for the SIR model
    a = 1.47 * pow(10,-7)  # Infection rate (beta)
    b = 0.0588  # Recovery rate (gamma)

    delta_t = 1.0
    num_iterations = 120

    # Perform Euler's method for the SIR model
    results = euler_sir_model(initial_S, initial_I, initial_R, a, b, delta_t, num_iterations)

    # Display results
    for iteration, t, S, I, R, new_t, new_S, new_I, new_R in results:
        print(f"Iteration {iteration}: t = {t}, S(t) = {S}, I(t) = {I}, R(t) = {R}, "
              f"New t = {new_t}, New S(t) = {new_S}, New I(t) = {new_I}, New R(t) = {new_R}")

    # Plot the solution curves
    t_values = np.arange(0, num_iterations + 1) * delta_t

    S_values = [initial_S] + [result[2] for result in results[1:]]  # Include initial condition
    I_values = [initial_I] + [result[3] for result in results[1:]]  # Include initial condition
    R_values = [initial_R] + [result[4] for result in results[1:]]  # Include initial condition

    plt.plot(t_values, S_values, marker='o', label='Susceptible', markersize=2)
    plt.plot(t_values, I_values, marker='o', label='Infectious', markersize=2)
    plt.plot(t_values, R_values, marker='o', label='Recovered', markersize=2)

    # Add labels and legend
    plt.xlabel('t')
    plt.ylabel('Population')
    plt.title('SIR Model Using Euler\'s Method')
    plt.legend()

    # Show the plot
    plt.show()

main()
