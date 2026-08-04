class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        x = list(range(min(nums),max(nums)))
        for i in set(nums):
            print(x)
            if i in x:
                x.remove(i)
            
        return x
