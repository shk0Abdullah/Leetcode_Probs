class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Linear Complexity
        # k = max(nums)
        # for i in (range(0, k+1)):
        #     if i not in nums:
        #         return i
        # return k+1
        # Better One
        return sum(range(len(nums)+1)) - sum(nums) 