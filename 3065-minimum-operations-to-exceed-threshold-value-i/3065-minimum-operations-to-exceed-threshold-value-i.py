class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        output = 0
        if len(nums) == 0  :
            return output
        for i in nums:
            if i >= k:  
                continue
            else:
                output +=1
        return output

