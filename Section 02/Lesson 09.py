"""
    Data Science and Machine Learning with Python
    Section 02 - Lesson 09
    Activity: Mean, Median, Mode, and introducing NumPy
    ---------------------------------------------------------------
    Find the mean and median of this data. In the code block
    below, write your code, and see if your
    result makes sense.
    ---------------------------------------------------------------
    Olavo Amorim Santos (olavo.a.santos@gmail.com)
"""
import numpy as np
import matplotlib.pyplot as plt

# It defines the income distribution properties
cen = 100
std_dev = 20
count = 10000

# It generates a random income array around cen with a
# standard deviation of std_dev with
# "count" data points
incomes = np.random.normal(cen, std_dev, count)

# It plots a histogram with the data segmented in 50 buckets
plt.hist(incomes, 50)
plt.show()

# It calculates and prints the Mean value of the distribution
mean = np.mean(incomes)
print(mean)

# It calculates and prints the Median value of the distribution
median = np.median(incomes)
print(median)
