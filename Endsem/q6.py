import math
from matplotlib import pyplot as plt
import numpy as np
def sampling_PDF(x):
    if abs(x) < 2:  return 0.5 * (x**2 - a**2)
    else: return 0
def target_PDF(x,a):
    return math.exp(-2*x)

def accept_reject(num_samples,a):
    accepted_samples = []
    majorizing_constant = 4
    while len(accepted_samples) < num_samples:
        x = np.random.uniform(0, 2)
        u = np.random.uniform(0, 2)
        if u <= target_PDF(x,a) / (majorizing_constant * sampling_PDF(x)):
            accepted_samples.append(x)
            print(len(accepted_samples))
    return accepted_samples




# def sampling_PDF(x):
#     return math.exp(-2*x) 
# def target_PDF(x,a):
#     return 0.5 * (a**2 - x**2)

num_samples = 20
a=2
accepted_samples = accept_reject(num_samples, 2)

plt.figure(figsize=(8, 4))
plt.hist(accepted_samples, bins=50)
plt.ylabel('No. of instances')
plt.grid()
plt.xlabel('x')
plt.title(' Accept-Reject method')
plt.show()