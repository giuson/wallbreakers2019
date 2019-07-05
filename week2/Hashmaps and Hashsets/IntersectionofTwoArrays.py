#INTERSECTION OF TWO ARRAYS
#https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list1 = set(nums1)
        list2 = set(nums2)
        
        output=[]
        if len(list1) < len(list2):
            for i in list1:
                if i in list2:
                    output.append(i)
        else:
            for i in list2:
                if i in list1:
                    output.append(i)
                    
        return output