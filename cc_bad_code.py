# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 22:05:12 2022

@author: nazim
"""




#score
num1 = 5
num2 = 2
num3 = 5
num4 = 7
num5 = 3
num6 = 9
num7 = 8
num8 = 12
num9 = 15
num10 = 4


sumNum = (num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10)
average = sumNum/10

print (average)



numberArray = [4,1,6,11,2]

for i in range (len(numberArray)):
    print ("Student:",i, "score:", numberArray[i])
    
    if numberArray[i] < 5:
        grade = 'F'
        if numberArray[i] > 4 & numberArray[i] < 8:
            grade = 'C'
            if numberArray[i] > 7 & numberArray[i] < 10:
                grade = 'B'
                if numberArray[i] > 10:
                    grade = 'A'
                
    print ("grade = ", grade)
    print()
    
    
    
    
    
    

