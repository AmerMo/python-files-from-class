#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%

print(3 ** 2)

print(4 ** 2)

print(type(3))


#%%

def area_square_print(side):
    area = side ** 2
    
    print(area)

def area_square_return(side):
    area = side ** 2
    
    return area


print("the area of a square of side 3 is " + str(area_square_return(3)))

#%%


print(4 >= 4)
print(4 > 4)
print(4 == 4)
print(4 != "potato")


#%%

if 5 == 4:
    print("it was true")
else:
    print("it wasn't true")
    
    
#%%    

def area_square(side):
    if type(side) == int or type(side) == float:
        return side ** 2
    else:
        print("type must be int or float")

area_square("asdf")        
    
area_square(3333)        
    
#%%
   
def area_square(side):
    if type(side) == int:
        return side ** 2
    elif type(side) == float:
        return side ** 2
    else:
        print("type must be int or float") 
    
    
    







    
    







