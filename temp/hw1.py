# coding: utf-8
'''
@author: TC
@file: hw1.py
@time: 2019/3/25 23:28
'''
import matplotlib.pyplot as plt
import numpy as np

m = 10
X0 = np.ones((m, 1))
X1 = np.array([4, 8, 9, 8, 7, 12, 6, 10, 6, 9]).reshape(m, 1)

X = np.hstack((X0, X1))

y = np.array([
    9, 20, 22, 15, 17, 23, 18, 25, 10, 20
]).reshape(m, 1)

# The Learning Rate alpha.
alpha = 0.01

def error_function(theta, X, y):
    '''Error function J definition.'''
    diff = np.dot(X, theta) - y
    return (1./2*m) * np.dot(np.transpose(diff), diff)

def gradient_function(theta, X, y):
    '''Gradient of the function J definition.'''
    diff = np.dot(X, theta) - y
    return (1./m) * np.dot(np.transpose(X), diff)

def gradient_descent(X, y, alpha):t
    '''Perform gradient descent.'''
    theta = np.array([1, 1]).reshape(2, 1)
    gradient = gradient_function(theta, X, y)
    while not np.all(np.absolute(gradient) <= 1e-5):
        theta = theta - alpha * gradient
        gradient = gradient_function(theta, X, y)
    return theta

optimal = gradient_descent(X, y, alpha)
print('optimal:', optimal)
print('error function:', error_function(optimal, X, y)[0,0])


x = [4, 8, 9, 8, 7, 12, 6, 10, 6, 9]
y = [9, 20, 22, 15, 17, 23, 18, 25, 10, 20]
x1 = np.linspace(3, 12, 10)
y1 = optimal.tolist()[0][0] * x1 + optimal.tolist()[1][0]
plt.plot(x, y, 'o')
plt.plot(x1, y1)
plt.show()