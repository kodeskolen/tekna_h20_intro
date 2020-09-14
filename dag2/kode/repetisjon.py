# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:01:50 2020

@author: Marie
"""
from pylab import sqrt
a = float(input("Hva er a?"))
b = float(input("hva er b?"))
c = float(input("hva er c?"))

if b**2 - 4*a*c < 0:
    print("Det finnes ingen reelle løsninger")
elif b**2 - 4*a*c == 0:
    løsning = -b/(2*a)
    print(f"Løsingen er {løsning}")
else:
    løsning1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    løsning2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    
    print(f"{løsning1} og {løsning2}")
