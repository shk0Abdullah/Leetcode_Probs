import math
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        prod = 0
        if nums[0] < 0 and nums[1] < 0:
            prod = abs(nums[0]*nums[1])
        max_prod = prod* nums[-1]
        k = nums[-1] * nums[-2] * nums[-3]
        if k > max_prod:
            max_prod = k
        return max_prod

  