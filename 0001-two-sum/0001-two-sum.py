class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in (nums):
            rem_num = target - i
            k = nums.index(i)
            if rem_num in (nums[:k]+nums[k+1:]):
                y = [idx for idx,val in enumerate(nums) if val == rem_num ]
                for j in y:
                    if j == k:
                        continue
                    else:
                        return [j,k]
          