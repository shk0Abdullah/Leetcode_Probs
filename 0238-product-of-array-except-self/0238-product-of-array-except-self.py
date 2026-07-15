import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = math.prod(nums)
        if prod==0:
            zeros = nums.count(0)
            if zeros >1:
                return [0]* len(nums)
            else:
                arr = [0] * len(nums)
                index_of_zero = nums.index(0)
                nums.pop(index_of_zero)
                arr[index_of_zero] = math.prod(nums)
                return arr
            
        else:    
            for i,k in enumerate(nums):
                nums[i] = int(prod/nums[i])
            return nums