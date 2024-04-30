import numpy as np
from matplotlib import pyplot as plt


def psi(x, a):
    if abs(x) < 2:  return 0.5 * (x**2 - a**2)
    else: return 0

a_values = np.linspace(0, 2, 20)

for a_val in (a_values):
    x_val = 1
    step_size_val = 0.8
    x_list = [x_val]
    accepted_count = 0
    rejected_count = 0 

    for _ in range(20000):
        old_probability = psi(x_val, a_val)
        x_new_val = x_val + (2 * np.random.uniform() - 1) * step_size_val
        new_probability = psi(x_new_val, a_val)
        gamma_val = np.random.uniform()

        if gamma_val < min(1, new_probability / old_probability):
            x_val = x_new_val
            x_list.append(x_val)
            accepted_count += 1
        else:
            rejected_count += 1

    x_list = np.array(x_list)
    
plt.figure(figsize=(12, 6))

plt.hist(x_list, bins=200)
plt.xlabel('Position', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.title('Observed position', fontsize=16)
plt.grid(True, which="both", ls="--", alpha=0.5)

plt.tight_layout()
plt.savefig("Q7 SHO Monte Carlo.png")
