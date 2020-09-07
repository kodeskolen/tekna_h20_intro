# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 17:34:11 2020

@author: Marie
"""

# Regne ut volum  av en kule med radius 1.1 cm

# (4/3) pi r^3

from math import pi

radius = float(input("Gi meg en radius: "))

volum = (4/3)*pi*radius**3
print(f"Volum av en kule med radius {radius} er {volum:.2f}")
