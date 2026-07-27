class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        starting_pointer = 0
        end_pointer = k-1
        iterations = len(nums[k:])
        max_avg = -math.inf
        x = sum(nums[starting_pointer:end_pointer+1])
        if len(nums) == 1:
            return nums[0]
        if len (nums) <k:
            iterations = len(nums)
        for i in range(iterations+1):
            
            if max_avg < x:
                max_avg = x
            x -= nums[starting_pointer]
            end_pointer +=1
            try:
                x += nums[end_pointer]
            except:
                pass
            starting_pointer +=1

        return max_avg/k