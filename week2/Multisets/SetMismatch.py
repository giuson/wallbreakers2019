#SET MISMATCH
#https://leetcode.com/problems/set-mismatch/

import collections

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        output = []
        num_count = collections.Counter(nums)
        
        for num, count in num_count.most_common(1):
            output.append(num)
                
        if 1 not in nums:
            output.append(1)
            return output
        
        elif len(nums) not in nums:
            output.append(len(nums))
            return output
        
        else:
            nums_set = list(set(nums))
            for idx, num in enumerate(nums_set):
                if num+1 != nums_set[idx+1]:
                    output.append(num+1)
                    return output
