#PEAK INDEX IN A MOUNTAIN ARRAY
#https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        d = {}
        for idx, i in enumerate(A):
            d[i] = idx
            
        A.sort(reverse=True)
        target = A[0]
        
        return d[target]


'''
My attempt at a binary search solution that unfortunately did not work

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        
        l = 0
        r = len(A)-1
        
        while l<r:
            mid = int((l+r)/2)
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                return mid
            elif A[mid] > A[mid-1] and A[mid] < A[mid+1]:
                l = mid+1
            if A[mid] < A[mid-1] and A[mid] > A[mid+1]:
                r = mid-1
        
        return -1
'''