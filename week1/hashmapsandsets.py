#TWO SUM
#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    	#create a dictionary
        d={}
        for i in range(len(nums)):
        	#get the complement of the current number
            complement=target-nums[i]
            #check if complement of current number is in dictionary
            if complement in d:
                return (d[complement],i) #return indices
            d[nums[i]]=i #key is the number, value is the index
        return []

#VALID ANAGRAM
#Given two strings s and t , write a function to determine if t is an anagram of s.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        #create dictionaries
        dt = {}
        ds = {}
        
        #count amount of unique letters in each string and compare if equal
        for char in t:
            if char not in dt:
                dt[char] = 1
            else:
                dt[char] += 1
        
        for char in s:
            if char not in ds:
                ds[char] = 1
            else:
                ds[char] += 1
                
        return dt==ds