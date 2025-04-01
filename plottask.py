# This program displays 
# a histogam of a normal distribution of 1000 values
# with a mean of 5 and standard deviation of 2,
# and a plot of the function $h(x)=x^3$ in the range 0 to 10
# Author: Stephen Kerr

# import numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt

# create a normal distribution of 1000 values
normal_dist = np.random.normal(5, 2, 1000)

# create h(x)=x^3
x = np.linspace(0, 10, 100)
y = x ** 3

# create plot
plt.figure(figsize=(10, 5))

# plot the histogram of the normal distribution
plt.hist(normal_dist, bins=30, edgecolor='black')

# plot the function h(x)=x^3
plt.plot(x, y, color='red', label='h(x)=x^3')

# add labels and title
plt.xlabel('x')
plt.ylabel('Frequency / h(x)')
plt.title('Histogram of Normal Distribution and Plot of h(x)=x^3')

# add legend
plt.legend(['Normal Distribution', 'h(x)=x^3'])

# add grid
plt.grid(True)

# save plot as png
plt.savefig('normal_dist_and_hx.png') 

# Reference: https://numpy.org/doc/stable/reference/generated/numpy.linspace.html