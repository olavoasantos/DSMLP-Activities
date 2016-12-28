"""
    Data Science and Machine Learning with Python
    Section 03 - Lesson 19
    Activity: Linear Regression
    ---------------------------------------------------------------
    Try increasing the random variation in the test data, and see
    what effect it has on the r-squared error value.
    ---------------------------------------------------------------
    This generates a random weight to the variation to yield a more
    organic set of results.
    Olavo Amorim Santos (olavo.a.santos@gmail.com)
"""
from scipy import stats
from numpy import random
from pylab import scatter
import matplotlib.pyplot as plt


# Function definitions
def predict(x):
    """
        It generates the function based on linear fit values
        :param      x:  Value
        :return:    Y value
        """
    return slope * x + intercept

# Variable definitions
pageSpeeds = random.normal(3.0, 1.0, 1000)
# The variation has a random weight based on varWeight variable
varWeight = 100
purchaseAmount = 100 - pageSpeeds * 3 + random.normal(0, 0.1, 1000) * random.randint(-varWeight, varWeight)

# Generate scatter plot
scatter(pageSpeeds, purchaseAmount)

# Linear fit
slope, intercept, r_value, p_value, std_err = stats.linregress(pageSpeeds, purchaseAmount)

# Generates the linear fit function
fitLine = predict(pageSpeeds)

# Plots the graphs
plt.scatter(pageSpeeds, purchaseAmount)
plt.plot(pageSpeeds, fitLine, c='r')
plt.suptitle('R² = ' + str(r_value ** 2))
plt.show()
