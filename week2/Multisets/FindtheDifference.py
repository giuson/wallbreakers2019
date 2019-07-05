#FIND THE DIFFERENCE
#https://leetcode.com/problems/find-the-difference/

import collections

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = collections.Counter(s)
        t_count = collections.Counter(t)
        
        for letter in t_count:
            if letter not in s_count:
                return letter
            elif t_count[letter]!=s_count[letter]:
                return letter