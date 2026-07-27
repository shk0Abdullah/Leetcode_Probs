class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = sorted(map(lambda x: abs(x),nums))
        i = nums[-1]-1
        j = nums[-2]-1
        return i*j
