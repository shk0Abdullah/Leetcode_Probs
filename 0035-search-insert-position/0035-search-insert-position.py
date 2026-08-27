class Solution:
    
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.target = target
        try:
            print("dsjfghj")
            return nums.index(target)
        except:
            # there would be two cases 
            # check the middle value and divide and found the place if not exists throw the len(nums) 
            k = len(nums)
            mid = int(k/2)
            print(mid, nums[mid])   
            if target > nums[mid]:
                index = mid
                while True:
                    try:
                        if nums[index] < target and nums[index+1] >target:
                            return index+1
                        else:
                            index +=1
                    except:
                    
                        return len(nums)
                
            elif target < nums[mid]:
                index = mid
                print(index)
                while True:
                    try:
                        if nums[index] > target and nums[index-1] < target:
                            return index
                        else:
                            index -=1
                            print(index)
                    except:
                        return 0

        