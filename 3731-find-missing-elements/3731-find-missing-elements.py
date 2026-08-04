class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
      return list(filter( lambda x: x not in nums, list(range(min(nums), max(nums)))))
