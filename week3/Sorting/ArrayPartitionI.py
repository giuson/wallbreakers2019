#ARRAY PARTITION I
#https://leetcode.com/problems/array-partition-i/

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sums = []
        
        for idx, i in enumerate(nums):
            if idx%2 == 1:
                prev_num = nums[idx-1]
                sums.append(min(i, prev_num))
                
        return sum(sums)