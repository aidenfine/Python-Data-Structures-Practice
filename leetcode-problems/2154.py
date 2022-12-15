class Solution:
    def findFinalValue(nums, original):
        # search list for original number 
        # use binary search 

        first = 0
        last = len(nums) - 1
        inList = False

        while first <= last:
            mid = (first + last)//2
            if nums[mid] == original:
                inList = True
                original = 2 * original
                # while inList:
                #     original = 2 * original
                #     if original is not in list:
                #         return original
            elif nums[mid] < original:
                first = mid + 1
            else:
                last = mid - 1
            while inList == True:
                if nums[mid] == original:
                    original = 2 * original 
                elif nums[mid] < original:
                    first = mid + 1
                else:
                    last = mid - 1
            print(original)
    nums = [5,3,6,1,12]
    original = 3
    findFinalValue(nums, original)
        # return original # if org is not found in list 
