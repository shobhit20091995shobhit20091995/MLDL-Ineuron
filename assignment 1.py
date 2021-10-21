# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 11:28:51 2021

@author: shobhit kumar
"""


# part 1
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i ,end=',')

        

# part 2
firstname = input("\n What is your last name?:")
lastname = input("What is your last?")
print(firstname[::-1] + " " + lastname[::-1])

# part 3
pi = 3.1415926535897931
r= 12.0
V= 4.0/3.0*pi* r**3
print('\nThe volume of the sphere is: ',V,'cm3')
