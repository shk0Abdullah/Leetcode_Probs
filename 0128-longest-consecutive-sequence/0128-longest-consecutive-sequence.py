class Solution:
    def __init__(self):

        self.longest = 1

    def longestConsecutive(self, nums: List[int]) -> int:
        self.nums = set(sorted(nums))
        self.longLst = []
        if len(self.nums) == 0:
            return 0
        for i in self.nums:
            if i - 1 not in self.nums:
                self.recursion(i)

        return max(self.longLst)

    def recursion(self, i):
            
        if i + self.longest in self.nums:
            self.longest += 1
            self.recursion(i)

        else:
            self.longLst.append(self.longest)
            self.longest = 1
