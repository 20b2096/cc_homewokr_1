# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 22:08:56 2022

@author: nazim
"""

numberArray = [5,2,5,7,3,9,8,12,15,4]

average = sum(numberArray)/len(numberArray)

print ("average number:", average)



for i in range (len(numberArray)):
    print ("Student:",i, "score:", numberArray[i])
    
    if numberArray[i] < 5:
        grade = 'F'
    elif numberArray[i] < 8:
        grade = 'C'
    elif numberArray[i] < 10:
        grade = 'B'
    elif numberArray[i] <= 15:
        grade = 'A'
        
    print ("grade = ", grade)
    print()
    
    
