# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 18:16:40 2020

@author: Marie
"""

from pylab import arange, sqrt

x = arange(1, 11)
y = sqrt(x)
print(x)
print(y)

def kvadrer(x):
    return x**2

z = kvadrer(x)
print(z)

for y_verdi in y:
    print(f"{y_verdi:.2f}")
    
print(y[0])



