"""
    Data Science and Machine Learning with Python
    Section 02 - Lesson 14
    Activity: MatPlotLib Basics
    ---------------------------------------------------------------
    Try creating a scatter plot representing random data on age
    vs. time spent watching TV. Label the axes.
    ---------------------------------------------------------------
    Olavo Amorim Santos (olavo.a.santos@gmail.com)
"""
import numpy as np
import matplotlib.pyplot as plt

# It generates the values
count = 500
age = np.random.randint(0, 75, count)
tv_time = np.random.normal(6.0, 2.0, count) * age / 75

# It styles the axes
axes = plt.axes()
axes.set_xlim([-3, 80])
# axes.set_ylim([-5, 29])
axes.grid()

# It plots the scatter plot
plt.scatter(age, tv_time)
plt.show()
