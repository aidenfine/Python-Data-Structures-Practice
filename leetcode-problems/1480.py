class Solution:
    def runningSum(nums):
        # get len of nums 
        n = len(nums)
        # empty array to store values 
        arr = [] 

        # in range create a list of numbers between 0 - n 
        for x in range(0,n):
            # if len of arr == 0 
            if (len(arr)==0):
                print(x)
                # remove value from nums and place into arr
                arr.append(nums[x])
            else:
                """
                this takes x from arr
                and takes x from nums
                add's together the two numbers
                then appends the number into arr
                """
                arr.append(arr[x-1]+nums[x])
        print(arr)
    nums = [1,2,3,4]
    runningSum(nums)
    