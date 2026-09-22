#fibonacci.py

#Auteur: michel ratsizafy
# created: 09/16/2026

import numpy as np

def fibonacci(n):
    if n == 1:
        return np.array([0])
    elif n == 2:
        return np.array([0,1])


#Create an empty of integers, large enough to hold the sequence
    fib = np.zeros(n, dtype=int)
    fib[1] = 1
#the first element is qlready 0, set the second to 1
    for ii in range(2, n):
        fib[ii] = fib[ii-2] + fib[ii-1]


     #return the array
    return fib