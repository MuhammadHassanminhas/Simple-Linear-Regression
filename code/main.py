import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def calculate_slope_intercept(X, Y):
   

    Sum_X = X.sum()
    Sum_Y = Y.sum()
    Square_X = Sum_X ** 2

    
    XY = np.dot(X, Y) 

    m = ((Y.size() * XY) - (Sum_X * Sum_Y)) / (Y.size() * Square_X)
    c = ((Y.size() * Sum_Y) - (m * Sum_X)) / Y.size()

    return m, c

df = pd.read_csv('Housing.csv')

X = df['price']
Y = df['area']

slope, intercept = calculate_slope_intercept(X, Y)




