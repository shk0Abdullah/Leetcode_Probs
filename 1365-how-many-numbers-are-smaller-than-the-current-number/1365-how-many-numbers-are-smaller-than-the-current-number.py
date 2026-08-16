class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Big O n square
        # ret = [None]*len(nums)
        # for index, i in enumerate(nums):
        #     k = 0
        #     for j in nums:
        #         if i > j:
        #             k +=1
        #     ret[index] = k
        # print(ret)
        # return ret
        # I will write it for Big O n
        d = {}


        for i,v in enumerate(sorted(nums)):
            if v not in d.keys():
                d[v] = i 
        
        for index,k in enumerate(nums):
            nums[index] = d[k]
        return nums 