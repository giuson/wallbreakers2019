#JEWELS AND STONES
#https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for stone in S:
            if stone in J:
                count += 1
        return count
                
