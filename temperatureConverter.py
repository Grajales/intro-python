#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 16:11:04 2021

@author: LG29878
"""

def convert_temp():
    temp = int(input('What is the temp?'))
    temp_unit = (input('What is the temperature unit? f, C, K'))
    if temp_unit == "f":
        temp_c = ((temp - 32) * 5)/9
        temp_k = (temp_c + 273.15)
        temp_f = temp
    elif temp_unit == "C":
        temp_f = (temp * 9/5) + 32
        temp_k = (temp + 273.15)
        temp_c = temp
    else:
        temp_c = (temp - 273.15)
        temp_f = (temp_c * 9/5) + 32
        temp_k = temp
    return print(f'Celcius {temp_c} Fahrenheit {temp_f} Kelvin {temp_k}')
     

convert_temp()