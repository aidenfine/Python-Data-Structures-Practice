import random

value = random.randint(1, 50)
list = range(1,50)
print(value)
def search(value, list):

    # O(1)
    found = False
    position = -1
    index = 0
    # O(n)
    while not found and index < len(list):
        # O(1)
        if list[index] == value:
            found = True
            position = index
        else:
            index += 1
    print("n found")
    print(position)

search(value, list)