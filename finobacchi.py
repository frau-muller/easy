# -*- coding: utf-8 -*-
"""finobacchi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uUAx2xjQ6FqsEqh1ZmXxWl8dGvt-Gyqn
"""

def fib(n):
    fib= [0,1]+[0]*(n-1)
    for i in range(2,n+1):
        fib[i]=fib[i-1]+ fib[i-2]
    return fib
fib(20)