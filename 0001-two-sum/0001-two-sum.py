class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute Force Approach n square
        # for i in (nums):
        #     rem_num = target - i
        #     k = nums.index(i)
        #     if rem_num in (nums[:k]+nums[k+1:]):
        #         y = [idx for idx,val in enumerate(nums) if val == rem_num ]
        #         for j in y:
        #             if j == k:
        #                 continue
        #             else:
        #                 return [j,k]
          

    # [3.2.4]



        # Big O n Approach
        k = nums
        nums = sorted(nums)
        starting = 0
        ending = len(nums)-1
        while starting != ending:
            current = nums[starting] + nums[ending]
            if current > target:
                ending -= 1
            elif current < target:
                starting += 1
            else:
                break
        x = k.index(nums[starting])
        k[x] = None
        y = k.index(nums[ending])
        k[y] = None
        
        
        return [x, y]