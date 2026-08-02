class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # bad solution quadratic complexity
        # set_nums = set()
        # for i in nums: 
        #     if i in set_nums:
        #         return True
        #     else: 
        #         set_nums.add(i)
        # return False
        # Linear Complexity
        if len(set(nums)) != len(nums):
            return True
        return False