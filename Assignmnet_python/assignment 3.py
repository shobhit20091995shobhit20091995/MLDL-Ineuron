# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 12:36:08 2021

@author: shobh
"""
# part 1

# myreduce funtion was self made and tested using add funtion and giving input as list :
def add(a,b):
    return a+b

def myreduce(func, mylist):
    x = mylist[0]
    for i in range(1, len(mylist)):
        x = func(x, mylist[i])
    print(x)
    return (x)

l1=[1,2,3]
myreduce(add,l1)

# myfilter funtion was self made and tested using is_even funtion and giving input as list :

def is_even(number):
    return number % 2 == 0
    
def myfilter(funtion,lis):    
   y = []
   for i in range(0, len(lis)):
        if funtion(lis[i]) == True :
            y.append(lis[i]) 
   
   #print(y)
   return y

list_2=[2,3,4,5,6,7,8,9,10]
print(myfilter(is_even,list_2))






# part 2

# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
l =[]
for i in 'xyz':
    for j in range(1,5):
        l.append(i*j)
print(l)      

#['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz'] 

l1 =[]
for i in 'xyz':
    l1.append(i)
for i in 'xyz':
    l1.append(i*2)
for i in 'xyz':
    l1.append(i*3)
print(l1)

# [[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6],

l2=[]
for i in range(2,5):
    for j in range(0,3):
        l2.append([i+j])  
l3=[2,3,4,5]
for j in range(4):
    final_list = list(map(lambda x: x+j, l3))
    l2.append(final_list)
print(l2)
    

# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

l4=[]
listinner=[1,2,3]
for i in range(1,4):
    for j in range(1,4):
        l4.append((j,i))
print(l4)       
        
        
        
        
        

