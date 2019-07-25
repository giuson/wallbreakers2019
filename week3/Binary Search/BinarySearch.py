#BINARY SEARCH
#https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        firstIndex = 0
        lastIndex = len(nums)-1
        mid = int((firstIndex + lastIndex)/2)
        
        while lastIndex - firstIndex >= 0:
            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                #check upper half
                firstIndex = mid+1
                mid = int((firstIndex + lastIndex)/2)

            elif nums[mid] > target:
                lastIndex = mid-1
                mid = int((firstIndex + lastIndex)/2)
        
        return -1