"""
list = [1,2,3,4]

A = [list]*3 # takes the list and create 3 new separate list that are the exact same 

if 1 in list:
    print("yes")
print(A)

list[2]=45 # puts the number 45 into the 2nd index of the list
print(A)
"""
# ------------------------------------------------------------------

myList = [1024, 3, True, 6.5]
print(myList[2])

myList.append(False) # list.append adds a new item to the end of the list 
print(myList)        # list.append(item)

myList.insert(2,4.5) # inserts and item in position of a list 
# print(myList)      # list.insert(i,item) i = index 

print(myList.pop()) # list.pop removes and returns the last item in a list
# print(myList)     # list.pop()

print(myList.pop(1)) # list.pop(i) removes and returns the item in the specified index 
# print(myList)      # list.pop(i) i = index

myList.pop(2)  
print(myList)

myList.sort()        # .sort modifies a list to be sorted 
print(myList)        # list.sort()

myList.reverse()
print(myList.reverse()) # list.reverse() modifies a list ot be in reverse order
print(myList.count(6.5)) # list.count(item) returns the number of occurrences of item
print(myList.index(4.5)) # 
myList.remove(6.5) # list.remove(item) removes the first occurrences of item
print(myList)
del myList[i] # del list[i] deletes i 
print(myList)


print((54).__add__(21)) # just adds the two numbers

range(10)
# range (0, 10)

list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
