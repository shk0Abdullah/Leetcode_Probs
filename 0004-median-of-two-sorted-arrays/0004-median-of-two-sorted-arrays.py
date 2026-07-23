import math 
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        array = []
        pointer_nums1 = 0
        pointer_nums2 = 0
        while pointer_nums1 < len(nums1) and pointer_nums2 < len(nums2):
            if nums1[pointer_nums1] < nums2[pointer_nums2]:
                array.append(nums1[pointer_nums1])
                pointer_nums1 += 1
            else:
                array.append(nums2[pointer_nums2])
                pointer_nums2 += 1

        while pointer_nums1 < len(nums1):
            array.append(nums1[pointer_nums1])
            pointer_nums1 += 1

        while pointer_nums2 < len(nums2):
            array.append(nums2[pointer_nums2])
            pointer_nums2 += 1
        return self.median(array)

    def median(self, array):
        # return the float
        if len(array) %2==0:
            # means its even
            print(array)
            index = int(len(array)/2)-1
            print(index, index+1)
            print(array[index], array[index+1])

            return (array[index] + array[index+1])/2


        elif len(array) % 2 != 0:
            # its odd
            return math.ceil(array[int((len(array)/2))]) 




                    



                

