# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         # nums = set(nums)
#         output = []
#         pointer_end = k-1
#         pointer_start = 0
#         iterations = len(nums[k:])
#         for i in range(iterations +1):
#             if pointer_end == len(nums):
#                 output.append(max(nums[pointer_start:]))
#             else:
#                 k = nums[pointer_start:pointer_end+1]
#                 output.append(max(k))
#                 k.remove(nums[pointer_start])
#                 try:
#                     k.append(nums[pointer_end+1])
#                 except:
#                     pass
#             pointer_end += 1
#             pointer_start += 1
#         return output 
from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # stores indices
        
        for i, num in enumerate(nums):
            
            # 1. Remove smaller elements from back (they're useless)
            while q and nums[q[-1]] < num:
                q.pop()
            
            q.append(i)
            
            # 2. Remove front if it's out of the window
            if q[0] < i - k + 1:
                q.popleft()
            
            # 3. Add to result once window is full
            if i >= k - 1:
                output.append(nums[q[0]])
        
        return output            