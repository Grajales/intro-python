#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:30:23 2021

@author: LG29878
"""
sei_class= {
  "teacher": "Jimmy",
  "students": ["Yacko", "Wacko", "Dot"],
  "classroom": 2,
  "in_session": True,
  "schedule": {
    "morning": "Python Basics",
    "afternoon": "Enumerables"
  }
}
print(sei_class)
print(sei_class["teacher"])
print(sei_class["schedule"])
#teacher1=sei_class.teacher not possible

print(sei_class.keys())
print(list(sei_class.keys()))
print(list(range(1,6))) #starting point =1, max=6 is non inclusive for(i=1;i <6;i++)
print(list(range(6)))# starting poiunt not needed, 6 is the non inclusive max
for i in range(1, 6):
  print(i)
print(len(sei_class))

for i in range(0, 6,2):
  print(i)
planeteers = ["Earth", "Wind", "Captain Planet", "Fire", "Water"]
print(planeteers[1])
planeteers.append('Heart')
print(planeteers)
planeteers.append('Heart')
planeteers.remove('Captain Planet')
rangers = ["Red", "Blue", "Pink", "Yellow", "Black"]
planeteers.extend(rangers)
print(planeteers)

def double(number=5):
    return number * 2

print(double())
  
def double(number):
    return number * 2
print(double(3))