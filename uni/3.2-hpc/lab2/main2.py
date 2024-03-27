import numpy as np
import matplotlib.pyplot as plt
from numba import jit

# Parameters
L = 1.0  # Length of the domain
T = 2.0  # Final time
N = 1000  # Number of time steps
M = 200  # Number of spatial steps
dx = L / M
dt = T / N

# Initialize solution array
u = np.zeros((N+1, M+1))

# Initial conditions
x = np.linspace(0, L, M+1)
u[0] = 0.1 * np.sin(np.pi * x)

# Boundary conditions
u[:, 0] = 0
u[:, -1] = 0

# Derivative of initial conditions
x_prime = np.zeros_like(x)

# Define the wave equation solver
@jit(nopython=True)
def solve_wave_equation(u, x_prime):
    for n in range(N):
        for m in range(1, M):
            u[n+1, m] = u[n, m] + dt * x_prime[m] + \
                        (dt**2 / 2) * (np.exp(np.cos(x[m])) / 10) * \
                        ((u[n, m+1] - 2*u[n, m] + u[n, m-1]) / dx**2)
        # Calculate the derivative of the solution for next time step
        for m in range(1, M):
            x_prime[m] = (u[n+1, m+1] - u[n+1, m-1]) / (2 * dx)

# Solve the wave equation
solve_wave_equation(u, x_prime)

# Plotting
plt.figure(figsize=(8, 6))

for n in range(0, N+1, 50):
    plt.plot(x, u[n], label=f"t={n*dt:.2f}")

plt.xlabel('x')
plt.ylabel('u')
plt.title('Solution of Wave Equation')
plt.legend()
plt.grid(True)
plt.show()
