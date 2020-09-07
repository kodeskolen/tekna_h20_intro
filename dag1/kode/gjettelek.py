# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 19:37:23 2020

@author: Marie
"""

# Vi skal lage en gjettelek
# Vi tenker på et tall mellom 0 og 100
# Brukeren gjetter et tall
# Vi sier ifra om tallet er for stort eller for lite
# Hvis brukeren gjetter riktig er spillet over og de har vunnet
# Brukeren for et bestemt antall forsøk

from random import randint
fasit = randint(1,100)
maks_forsøk = 3

for forsøk in range(1, maks_forsøk + 1):
    gjett = float(input("Gjett et tall mellom 0 og 100: "))
    
    if gjett == fasit:
        print("Du klarte det")
        break
    elif gjett > fasit:
        print("Det er for høyt")
    else:
        print("Det er for lavt")
else:    
    print(f"Du har brukt opp dine {maks_forsøk} forsøk")
print("Spillet er over, takk for meg!")
