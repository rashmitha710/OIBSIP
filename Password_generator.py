# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 20:11:19 2024

@author: Rashmitha
"""

import random
import string


letters=string.ascii_letters
#['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=string.digits
#['0','1','2','3','4','5','6','7','8','9']
symbols=string.punctuation
#['!','@','$','#','%','&','(',')','*','+']
empty=[]
password=""

print("Welcome to password generator!!")
n_l=int(input("enter how many letters you want in your passsword?\n"))
n_s=int(input("enter how many symbols you want in your passsword?\n"))
n_n=int(input("enter how many numbers you want in your passsword?\n"))
for i in range(1,n_l+1):
    l = random.choice(letters)
    empty+=l
for i in range(1,n_s+1):
    s = random.choice(symbols)
    empty+=s
for i in range(1,n_n+1):
    n = random.choice(numbers)
    empty+=n
    
random.shuffle(empty)
#print(empty)
for i in empty:
    password+=i
print("Your password generated as:",password)