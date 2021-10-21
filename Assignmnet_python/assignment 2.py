# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 02:56:46 2021

@author: shobhit kumar
"""

# star pattern code -- part 1

for i in range(5):
    for j in range(i+1):
        print("* ",end="")
    print("\n")
for i in reversed(range(5)):
    for j in range(i-1):
        print("* ",end="")
    print("\n")
    
    
# part 2 

print("reversing the input word --\nineuron ")

a='ineuron'
for i in reversed(a):
    print(i,end='')
