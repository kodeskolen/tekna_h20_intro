# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 18:55:45 2020

@author: Marie
"""
def midtpunkt(a, b):
    return (a + b)/2

maks_tall = 100
min_tall = 0
maks_forsøk = 10

print(f"Tenk på et tall mellom {min_tall} og {maks_tall}")

for forsøk in range(1, maks_forsøk+1):
    gjett = int(midtpunkt(min_tall, maks_tall))
    
    print(f"Tenker du på {gjett}?")
    svar = input("Var dette for høyt, for lavt eller riktig?")
    if svar=="riktig":
        print("Jippi")
        print(f"Jeg greide det på {forsøk} forsøk")
        break
    elif svar=='for lavt':
        min_tall = gjett
    elif svar=="for høyt":
        maks_tall = gjett
    else:
        print("jeg forsto ikke hva du mente. Du må svare 'riktig', 'for høyt' eller 'for lavt'")
    
    
    
