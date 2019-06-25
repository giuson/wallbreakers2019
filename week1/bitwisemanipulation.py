#NUMBER COMPLEMENT
'''
Given a positive integer, output its complement number. 
The complement strategy is to flip the bits of its binary representation.
'''
class Solution:
    def findComplement(self, num: int) -> int:
        n = num
        x = 0
        while n!=0:
            num ^= (1 << x) 
            n = num >> x
            x+=1
        return num

#SINGLE NUMBER
#Given a non-empty array of integers, every element appears twice except for one. Find that single one.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = []
        nums.sort()
        
        #append to new list if no replicates
        for i in nums:
            if i in temp:
                temp.remove(i)
            else:
                temp.append(i)
        
        return temp[0]