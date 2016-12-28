"""
    Data Science and Machine Learning with Python
    Section 01 - Lesson 05
    Activity: Python 101
    ---------------------------------------------------------------
    Write some code that creates a list of integers, loops through
    each element of the list, and only prints
    out even numbers!
    ---------------------------------------------------------------
    Olavo Amorim Santos (olavo.a.santos@gmail.com)
"""
import numpy.random as rand

# Random number between 2 and 50
size = rand.randint(2, high=50)

# Random sized range of integers
list_of_integers = range(size)

# Loops through the list of integers
for n in list_of_integers:
    # If the value in the list is an even number AND is different zero
    if (list_of_integers[n] % 2) is 0 and list_of_integers[n] != 0:
        # Print the value
        print(list_of_integers[n])
