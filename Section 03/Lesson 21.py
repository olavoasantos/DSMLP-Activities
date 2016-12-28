"""
    Data Science and Machine Learning with Python
    Section 03 - Lesson 21
    Activity: Multivariate Regression
    ---------------------------------------------------------------
    Mess around with the fake input data, and see if you can
    create a measurable influence of number of doors on
    price. Have some fun with it - why stop
    at 4 doors?
    ---------------------------------------------------------------
    Evaluates the combinations of the 11 parameters and ranks
    the models by the highest R².
    Olavo Amorim Santos (olavo.a.santos@gmail.com)
"""
import itertools
import pandas as pd
import statsmodels.api as sm

df = pd.read_excel('http://cdn.sundog-soft.com/Udemy/DataScience/cars.xls')

df['Model_ord'] = pd.Categorical(df.Model).codes
df['Make_ord'] = pd.Categorical(df.Make).codes
df['Trim_ord'] = pd.Categorical(df.Trim).codes
df['Type_ord'] = pd.Categorical(df.Type).codes

# Get combinations from params
param = ['Mileage', 'Make_ord', 'Model_ord', 'Trim_ord', 'Type_ord', 'Cylinder', 'Liter', 'Doors', 'Cruise', 'Sound',
         'Leather']
params = list()
for i in range(1, len(param) + 1):
    for l in list(itertools.combinations(param, i)):
        params.append(list(l))

results = list()
# It iterates through the combinations to determine the best R²
for param in params:
    X = df[param]
    y = df[['Price']]

    X1 = sm.add_constant(X)
    est = sm.OLS(y, X1).fit()

    if est.rsquared > 0.48:
        results.append({'r2': est.rsquared, 'params': param, 'len': len(param)})

print(sorted(results, key=lambda k: k['len'])[0])
