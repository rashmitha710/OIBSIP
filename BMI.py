# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 17:22:27 2024

@author: Rashmitha
"""

def BMI(w,h):
    return round((w/h**2),2)


print("Welcome to Body Mass Index")

w=float(input("Enter the Weight in Kgs : "))
h=float(input("Enter the Height in Meters : "))

bmi=BMI(w,h)
if(bmi<=18.5):
    print("You are underweight.")
elif(18.5<bmi<=24.9):
    print("You are Normal.")
elif(25<bmi<=29.9):
    print("You are Overweight.")
elif(30<bmi<=34.9):
    print("You are Obese.")
elif(35<bmi<=39.9):
    print("You are Severely Obese.")
else:
    print("You are Morbidly Obese.")
    
    