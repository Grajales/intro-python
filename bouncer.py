#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 13:43:56 2021

@author: LG29878
"""

    
print(type(False)) 
print(type(0))
print(type(""))
print(type(None)) 
print(False==False)
print(0==False)
print(None==False)
print(""==False)

hello = ['ehllo',"world",50]
print(hello)
print(hello[0])
numbers = [1,2,3]
print(type(numbers))
numbers.append(4)
print(numbers)
numbers.append(100)
print(numbers)
something="hwllo"
numbers.append(something)
print(numbers)
print(numbers[4])
numbers.pop()
print(numbers)
numbers.pop(1)
print(numbers)
second_numbers =[4,5,6]
numbers.extend(second_numbers)
print(numbers)
print(dir(numbers))
vowels =['a','e','i','u' ]
vowels.insert(2,'o')
print(vowels)
vowels2 =['a','e','i','u','o']
vowels3=sorted(vowels2)
print(vowels3)
vowels.remove("o") ##removes the first match
print(vowels)
# age=int(input('what is your age ?'))
# if age<18:
#     print('You are too young to enter')
# elif age>18 and age<21:
#     print('you can enter by cannot drink')
# else: 
#     print ('Come in! Drink all you want')
    
