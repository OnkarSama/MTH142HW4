import numpy as np
import matplotlib.pyplot as plt

# Given differential equation function
def dP_dt(P):
    return P * (1 - P)

# Euler's method
def euler_method(initial_P, delta_t, num_iterations):
    results = [("Iteration", "t", "P(t)", "dP/dt", "New t", "New P(t)")]

    P = initial_P
    t = 0
    for i in range(1, num_iterations + 1):
        dP = dP_dt(P)
        new_t = t + delta_t
        new_P = P + dP * delta_t

        results.append((i, round(t, 3), round(P, 3), round(dP, 3), round(new_t, 3), round(new_P, 3)))

        t, P = new_t, new_P

    return results

def main() :

    # Initial conditions
    initial_P = 0.05
    delta_t = 0.5
    num_iterations = 10

    # Perform Euler's method
    results = euler_method(initial_P, delta_t, num_iterations)

    # Display results
    for iteration, t, P, dP_dt, new_t, new_P in results:
        print(f"Iteration {iteration}: t = {t}, P(t) = {P}, dP/dt = {dP_dt}, New t = {new_t}, New P(t) = {new_P}")

    # Plot the solution curve
    t_values = np.arange(0, num_iterations + 1) * delta_t

    P_values = [initial_P] + [result[2] for result in results[1:]]  # Include initial condition

    plt.plot(t_values, P_values, marker='o', label='Euler\'s Method')

    # Add labels and legend
    plt.xlabel('t')
    plt.ylabel('P(t)')
    plt.title('Logistic Grow Using Euler\'s Method')
    plt.legend()

    # Show the plot
    plt.show()

main()