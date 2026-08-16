class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ret = [None]*len(nums)
        for index, i in enumerate(nums):
            k = 0
            for j in nums:
                if i > j:
                    k +=1
            ret[index] = k
        print(ret)
        return ret