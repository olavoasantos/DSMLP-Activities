"""
    Data Science and Machine Learning with Python
    Section 02 - Lesson 16
    Activity: Conditional Probability Activity & Exercise
    ---------------------------------------------------------------
    Modify the code above such that the purchase probability does
    NOT vary with age, making E and F actually independent.
    Then, confirm that P(E|F) is about the same as P(E),
    showing that the conditional probability of
    purchase for a given age is not any
    different than the a-priori
    probability of purchase
    regardless of age.
    ---------------------------------------------------------------
    This prints the probabilities from the original model - where
    the probability depends on the buyer's age - and the
    probabilities of a fixed purchase probability.
    Olavo Amorim Santos (olavo.a.santos@gmail.com)
"""
from numpy import random


def generate(prob):
    """
    It generates a random distribution based on a designated probability.
    :param      function    prob:   probability function with "ageDecade" argument
    :return:    list        [
                                totals:         Total number of people in each age group,
                                purchases:      Total number of things purchased by people in each age group,
                                totalPurchases: Grand total of purchases
                            ]
    """
    random.seed(0)

    totals = {20: 0, 30: 0, 40: 0, 50: 0, 60: 0, 70: 0}
    purchases = {20: 0, 30: 0, 40: 0, 50: 0, 60: 0, 70: 0}
    totalPurchases = 0
    choices = [20, 30, 40, 50, 60, 70]

    for _ in range(100000):
        ageDecade = random.choice(choices)
        purchaseProbability = prob(ageDecade)
        totals[ageDecade] += 1
        if random.random() < purchaseProbability:
            totalPurchases += 1
            purchases[ageDecade] += 1

    return totals, purchases, totalPurchases


def getProbability(age, probFunction=lambda x: float(x) / 100.0):
    """
    It gets the probability for a certain age based on a probability function.
    :param      int         age:                Age
    :param      function    probFunction:       Probability function
    :return:    dictionary  Dictionary with probabilities for certain age
    """
    totals, purchases, totalPurchases = generate(probFunction)

    return {
        'F': float(totals[age])/100000,
        'E': float(totalPurchases) / 100000.0,
        'E|F': float(purchases[age])/float(totals[age]),
        'E,F': float(purchases[age]) / 100000.0,
        'E.F': (float(totalPurchases) / 100000.0) * (float(totals[age])/100000)
    }

# Age dependent probability (default)
P = getProbability(30)

print('AGE DEPENDENT')
print("P(Purchase)=" + str(P["E"]))
print("P(30s)=" + str(P["F"]))
print("P(Purchase|30s)=" + str(P["E|F"]))
print("P(Purchase,30s)=" + str(P["E,F"]))
print("P(Purchase).P(30s)=" + str(P["E.F"]))

# Age independent probability (probability of purchase is 1/6)
P = getProbability(30, probFunction=lambda x: 1/6)

print('AGE INDEPENDENT')
print("P(Purchase)=" + str(P["E"]))
print("P(30s)=" + str(P["F"]))
print("P(Purchase|30s)=" + str(P["E|F"]))
print("P(Purchase,30s)=" + str(P["E,F"]))
print("P(Purchase).P(30s)=" + str(P["E.F"]))