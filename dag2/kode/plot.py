# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 18:31:38 2020

@author: Marie
"""
from pylab import *

x = arange(0, 8, 0.1)
y = sin(x)
z = cos(x)
print(x)

plot(x, y)
plot(x, z)
plot(1, sin(1), "ro")

xlabel("Tid")
ylabel("Høyde")
xlim(-5, 7.9)
ylim(-1, 1)
title("Posisjon til pendel som funksjon av tid")
axhline(0)
axvline(0)
show()





