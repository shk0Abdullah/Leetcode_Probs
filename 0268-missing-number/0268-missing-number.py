class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        k = max(nums)
        for i in (range(0, k+1)):
            if i not in nums:
                return i
        return k+1