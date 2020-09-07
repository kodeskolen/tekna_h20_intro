# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 18:43:54 2020

@author: Marie
"""

# Erik setter inn 10 000 kroner på BSU
# med renter 2.9
# Hvor mye penger har han etter 10 år?

penger = 10000 
rente = 1.029 

antall_år = 10 

for år in [1, 2, 3, 4]:
    penger *= rente
    print(f"Etter {år:2} år er det {penger:.2f} kr")
    
    
