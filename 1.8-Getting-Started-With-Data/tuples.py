"""
Tuples are similar to list but tuples cannot be changed
"""

myTuple = (2,True, 4.96)

myTuple
# (2,True, 4.96)

len(myTuple) 
#3

myTuple[0] # gets item at index of 0
# 2 

myTuple * 3
# (2, True, 4.96, 2, True, 4.96, 2, True, 4.96)

myTuple[0:2]

"""
if you try to modify a tuple you will get an error 
"""

myTuple[1] = False
# TypeError: object doesn't support item assignment

