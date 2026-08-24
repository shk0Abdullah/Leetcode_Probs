class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # space is cheap, time is expensive
        #  use sliding window approah started with two no's if both are unique shif the 
        # first index by two
        first_index = 0 
        last_index = 1 # including
        while True:
            try:
                if nums[first_index] != nums[last_index]:
                    if nums[last_index] != nums[last_index+1]:

                        # shift the window by 2
                        first_index += 2
                        last_index += 2
                    elif nums[last_index] == nums[last_index+1]:
                        first_index = last_index
                        last_index +=1 
                elif nums[first_index] == nums[last_index]:
                    # check for the next element and pop it 
                    if nums[last_index+1] != nums[last_index]:
                        first_index += 2
                        last_index += 2

                    elif nums[last_index+1] == nums[last_index]:
                        nums.pop(last_index+1)
            except:
                print(nums)
                break
        