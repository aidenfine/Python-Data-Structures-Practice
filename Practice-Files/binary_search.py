import random
from unittest import result

def binary_search(list, target):

    #!!!!!! If you binary search the list HAS TO BE SORTED !!!!!!

    #list is nums 0-8
    first = 0
    last = len(list) - 1

    while first <= last:
        #gets midpoint
        midpoint = (first + last)//2

        # best case 
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target: 
            #new first is first num in splitted list
            first = midpoint + 1
        else:
            #new last is last num in splitted list
            last = midpoint - 1

    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("target not found in list")

random = random.randint(1,10)
numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, random)
verify(result)
