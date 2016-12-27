"""
    Data Science and Machine Learning with Python
    Section 02 - Lecture 10
    Activity: Standard Deviation and Variance
    ---------------------------------------------------------------
    Experiment with different parameters on the normal function,
    and see what effect it has on the shape of the
    distribution. How does that new shape
    relate to the standard deviation
    and variance?
"""
import numpy.random as rand
import matplotlib.pyplot as plt


# Function to standardize plotting
def plot(data: tuple, title: str):
    """
    It plots the histograms.
    :param  tuple   data:   List of distributions
    :param  str     title:  Title of the figure
    :return: pass
    """
    plt.figure()
    list_range = get_range(data)
    plt.subplot(311)
    plt.title('{0} {1}, {2}, {3}'.format(title, cen[0], cen[1], cen[2]))
    plt.hist(data[0], 100, range=list_range)
    plt.subplot(312)
    plt.hist(data[1], 100, range=list_range)
    plt.subplot(313)
    plt.hist(data[2], 100, range=list_range)

    pass


# Function to get max and min from list of distributions
def get_range(lists: tuple):
    """
    It gets the max and min values from a list of distributions.
    :param      tuple   lists:  list of distributions
    :return:    list   [ min, max ]
    """
    max_val = None
    min_val = None
    for dist in lists:
        if max_val is None or max(dist) > max_val:
            max_val = max(dist)

        if min_val is None or min(dist) < min_val:
            min_val = min(dist)

    return [min_val, max_val]

# It defines random center values
cen = rand.randint(100, 1000000, 3)
cen.sort()
# It defines random standard deviation values
std_dev = rand.randint(0, 100000, 3)
std_dev.sort()
# It defines random result number values
count = rand.randint(50, 10000, 3)
count.sort()

# It generates normal distribution with different center values
cen_var = (
    rand.normal(cen[0], std_dev[1], count[1]),
    rand.normal(cen[1], std_dev[1], count[1]),
    rand.normal(cen[2], std_dev[1], count[1]),
)
# It generates normal distribution with different standard deviation values
std_var = (
    rand.normal(cen[1], std_dev[0], count[1]),
    rand.normal(cen[1], std_dev[1], count[1]),
    rand.normal(cen[1], std_dev[2], count[1]),
)
# It generates normal distribution with different count values
count_var = (
    rand.normal(cen[1], std_dev[1], count[0]),
    rand.normal(cen[1], std_dev[1], count[1]),
    rand.normal(cen[1], std_dev[1], count[2]),
)

# It plots the histograms
plot(cen_var, 'Center:')
plot(count_var, 'Count:')
plot(std_var, 'Standard deviation:')

# It shows the plots
plt.show()
