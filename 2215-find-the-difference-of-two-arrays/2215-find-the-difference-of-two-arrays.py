class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        left = []
        right = []
        for i,k in enumerate(nums1):
            if k in nums2:
                continue 
            else:
                left.append(k)
        for i,k in enumerate(nums2):
            if k in nums1:
                continue
            else:
                right.append(k)
        return [list(set(left)),list(set(right))]