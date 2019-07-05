#DISTRIBUTE CANDIES
#https://leetcode.com/problems/distribute-candies/

class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        unique = set(candies)
        if int(len(unique)) >= int(len(candies)/2):
            return int(len(candies)/2)
        else:
            return int(len(unique))