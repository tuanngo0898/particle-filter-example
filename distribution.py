import random
from matplotlib import pyplot as plt 
import numpy as np 

arr = []
for i in range(10000):
	arr.append(random.uniform(0, 1))

# mu, sigma = 0, 0.1 # mean and standard deviation
# arr = np.random.uniform(mu, sigma, 10000)

# mu, sigma = 0, 0.1 # mean and standard deviation
# arr = np.random.normal(mu, sigma, 10000)

hist, bin_edges = np.histogram(arr,bins=100)
print(bin_edges)


plt.plot(hist)
plt.ylim(0,500)
plt.show()