class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(filter(lambda x: x>0,nums))
        # print(nums)
        if not nums:
            return 1
        k = max(nums)
        x = range(1,k+1) 
        for i in x:
            if i not in nums:
                return i
        return k+1
        # try:
        #     nums = list(filter(lambda x: x>0,nums))
        #     if len(nums) ==1 and nums[0] != 1:
        #         return 1
        #     k = list(range(1, max(nums)+1))
        #     print(k, nums)
        #     val = list(set(nums)^set(k))
        #     if not val:
        #         return max(nums) + 1
        #     return val[0]
        # except:
        #     return 1
