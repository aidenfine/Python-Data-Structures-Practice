# Python-Data-Structures-Practice

A place to save my work 🙃
<br>
<h2>Big O</h2>
<ul>
    <h4>Most Common</h4> 
    <li>O(1) - constant </li>
    <li>O(log n) - logarthmic </li>
    <li>O(n) - linear </li>
    <li>O(n²) - quadratic </li>
    <h4>Less Common</h4>
    <li>O(2ⁿ) - exponential </li>
    <li>O(nⁿ) - ?? </li>
    <li>O(n!) - factorial </li> 
</ul>

<h3>Code Examples</h3>

```python
# O(1)
s = 4 + 3

# O(n)
for i = 0; i < n; i+=1:

# O(n)
s = 0
for i = 0; i < n; i+=1:
    # O(1)
    s += 1;

# O(n²)
for i = 0; i < n; i += 1:
    for j = 0; j < y; j += 1

# O(n) 
# this is just showing that no matter how many for loops being used its still O(n)
for i = 0; i < n; i+=1:
for i = 0; i < n; i+=1:
for i = 0; i < n; i+=1:

# O(log n)
while n > 0:
    n /= 2
# output 
100
50
25
12.5
6.25
...

# O(nlog n)
for i = 0; i < n; i+= 1:
    while x > 0:
        x /= 2;
```

<h3>Linear Search</h3>

```python
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

# O(1) + O(n) * O(1) ----> O(n)
```

<h3>Binary Search</h3>
Solved from leetcode question [704.] (https://leetcode.com/problems/binary-search/description/ "704.").

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0 # get first number in the list 
        last = len(nums)-1 # get last number in the list 

        while first <= last: # when first number is bigger than last number loop
            mid = (first + last)//2 # get mid point by add first+last then divide 
            # this is best case or fastest runtime
            if nums[mid] == target:
                return mid
            # if mid is less than check left side of list 
            elif nums[mid] < target:
                first = mid + 1
            else:
                last = mid - 1
        return -1
```