#VALID ANAGRAM
#https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S = sorted(list(s))
        T = sorted(list(t))
        return S == T