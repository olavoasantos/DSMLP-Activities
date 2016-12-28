"""
    Data Science and Machine Learning with Python
    Section 03 - Lesson 20
    Activity: Polynomial Regression
    ---------------------------------------------------------------
    Try different polynomial orders. Can you get a better fit with
    higher orders? Do you start to see overfitting, even
    though the r-squared score looks good for
    this particular data set?
    ---------------------------------------------------------------
    It analyses the variation of the R² in relation to the
    polynomial degree, interrupting if R² decreases
    or stabilizes.
    Olavo Amorim Santos (olavo.a.santos@gmail.com)
"""
from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# Definitions
np.random.seed(2)
pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds

# Polynomial fit
# Definitions
R2 = 0
degree = 0
offScore = 0
r_vals = list()
x = np.array(pageSpeeds)
y = np.array(purchaseAmount)

# It optimizes the polynomial degree between 1 and 20
for deg in range(1, 17):
    p = np.poly1d(np.polyfit(x, y, deg))

    # R² score
    r2 = r2_score(y, p(x))
    r_vals.append(r2)

    # It checks if r² is bigger than R²
    if r2 > R2:
        # It checks if the difference between r² and R² is smaller than 0.01
        if abs(r2-R2) < 0.01:
            offScore += 1.0
        R2 = r2
        degree += 1
    else:
        offScore += 1

    # It checks it polynomial degree is optimal
    if offScore > 1:
        break

# Graph plot
xp = np.linspace(0, 7, 100)
f, a = plt.subplots(2)
plt.subplots_adjust(hspace=.5)

# Scatter plot + polynomial fit
a[0].scatter(x, y)
a[0].set_ylim([min(y)-min(y)/2, max(y)+max(y)/2])
a[0].plot(xp, p(xp), c='r')
a[0].set_ylabel("Purchase amount")
a[0].set_xlabel("Page load speed")
a[0].set_title(str(degree) + " degree polynomial fit (R² = " + str(R2) + ")")

# R² variation
a[1].scatter(range(1, len(r_vals)+1), r_vals)
a[1].set_xlim([0, degree+1])
plt.xticks(np.arange(1, len(r_vals)+1, 1.0))
a[1].set_ylabel("R² value")
a[1].set_xlabel("Polynomial degree")
a[1].set_title("R² variation")

plt.show()
