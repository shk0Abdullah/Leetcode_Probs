class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = sorted([i for i in nums if i%k==0] ) 
        print(nums)
        p= k
        while True:
            if p not in nums:
                return p
            else:
                p +=k

