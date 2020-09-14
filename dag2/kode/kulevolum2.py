# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 17:38:28 2020

@author: Marie
"""

from math import pi

def kulevolum(radius):
    return (4/3)*pi*radius**3

radius_klinkekule = 1 #cm
radius_tennisball = 2.5 #cm
radius_bowlingball = 7 #cm

volum_klinkekule = kulevolum(radius_klinkekule)
volum_tennisball = kulevolum(radius_tennisball)
volum_bowlingball = kulevolum(radius_bowlingball)

