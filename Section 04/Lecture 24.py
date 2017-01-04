"""
    Data Science and Machine Learning with Python
    Section 04 - Lesson 24
    Activity: Train / Test
    ---------------------------------------------------------------
    Try measuring the error on the test data using different
    degree polynomial fits. What degree works best?
    ---------------------------------------------------------------
    It compares the fitting and R² for 1 to 9th degree
    polynomial fit.
    Olavo Amorim Santos (olavo.a.santos@gmail.com)
"""
from pylab import *
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# # # It generates the samples
np.random.seed(2)

# Page speed and purchase amount functions
pageSpeeds = np.random.normal(3.0, 1.0, 100)
purchaseAmount = np.random.normal(50.0, 30.0, 100) / pageSpeeds

# # # It creates train/test groups
# Page speed groups
trainX = pageSpeeds[:80]
testX = pageSpeeds[80:]

# Purchase amount groups
trainY = purchaseAmount[:80]
testY = purchaseAmount[80:]

# # # It fits to a polynomial
n = range(1, 10)
R = {"r2_test": [], "r2_train": []}

# # Training data
x = np.array(trainX)
y = np.array(trainY)

# # Test data
testx = np.array(testX)
testy = np.array(testY)

# # Fits to an nth-degree
fig = plt.figure()
xp = np.linspace(0, 7, 100)

for degree in n:
    p4 = np.poly1d(np.polyfit(x, y, degree))

    # Compare fitted curve to the train group
    axes = fig.add_subplot(len(n), 2, 2*degree-1)
    axes.scatter(x, y)
    axes.set_xlim([0, 7])
    axes.set_ylim([-50, 250])
    axes.plot(xp, p4(xp), c='r')
    axes.set_title("Train group - {0} degree fit".format(degree))

    # Compare fitted curve to the test group
    axes = fig.add_subplot(len(n), 2, 2*degree)
    axes.scatter(testx, testy)
    axes.set_xlim([0, 7])
    axes.set_ylim([-50, 250])
    axes.plot(xp, p4(xp), c='r')
    axes.set_title("Test group - {0} degree fit".format(degree))

    # Compares R² score against the train/test data
    r2_test = r2_score(testy, p4(testx))
    r2_train = r2_score(np.array(trainY), p4(np.array(trainX)))

    R["r2_train"].append(r2_train)
    R["r2_test"].append(r2_test)

plt.tight_layout(h_pad=0.2)

# Plots the polynomial degree vs R² score
f, a = plt.subplots(2, sharex=True)

# R² Train data variation
a[0].scatter(n, R["r2_train"])
a[0].set_xlim([0, n[len(n)-1]+1])
a[0].set_ylabel("R² train value")
a[0].set_title("R² train variation")
a[0].grid()

# R² Test data variation
a[1].scatter(n, R["r2_test"])
a[1].set_xlim([0, n[len(n)-1]+1])
a[1].set_ylabel("R² test value")
a[1].set_xlabel("Polynomial degree")
a[1].grid()

f.subplots_adjust(hspace=0)
plt.xticks(np.arange(1, n[len(n)-1]+1, 1.0))
plt.show()
