"""
    Data Science and Machine Learning with Python
    Section 02 - Lesson 15
    Activity: Covariance and Correlation
    ---------------------------------------------------------------
    Numpy also has a numpy.cov function that can compute Covariance
    for you. Try using it for the pageSpeeds and purchaseAmounts
    data above. Interpret its results, and compare it to the
    results from our own covariance function above.
    ---------------------------------------------------------------
    Olavo Amorim Santos (olavo.a.santos@gmail.com)
"""
import numpy as np
import matplotlib.pyplot as plt

# Initialize plots
f, a = plt.subplots(3)
plt.subplots_adjust(hspace=1)

# Random generated
# It generates the values
pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000)

# It plots the scatter plot
a[0].scatter(pageSpeeds, purchaseAmount)
a[0].set_title('Correlation: {0}; Covariance: {1}'.format(np.corrcoef(pageSpeeds, purchaseAmount)[0][1], np.cov(pageSpeeds, purchaseAmount)[0][1]))

# Inverse dependency
# It generates the values
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds

# It plots the scatter plot
a[1].scatter(pageSpeeds, purchaseAmount)
a[1].set_title('Correlation: {0}; Covariance: {1}'.format(np.corrcoef(pageSpeeds, purchaseAmount)[0][1], np.cov(pageSpeeds, purchaseAmount)[0][1]))

# Linear dependency
# It generates the values
purchaseAmount = 100 - pageSpeeds * 3

# It plots the scatter plot
a[2].scatter(pageSpeeds, purchaseAmount)
a[2].set_title('Correlation: {0}; Covariance: {1}'.format(np.corrcoef(pageSpeeds, purchaseAmount)[0][1], np.cov(pageSpeeds, purchaseAmount)[0][1]))

plt.show()
