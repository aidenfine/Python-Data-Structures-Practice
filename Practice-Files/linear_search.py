
list = [5,8,4,6,9,2]
n = 9
def linear_search(list, target):
    i = 0
    while i < len(list):
        if list[i] == target:
            return True
        i = i + 1
    return False

if linear_search(list, n):
    print("found")
else:
    print("not found")