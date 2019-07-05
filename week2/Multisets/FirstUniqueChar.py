#FIRST UNIQUE CHARACTER IN A STRING
#https://leetcode.com/problems/first-unique-character-in-a-string/

import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_count = collections.Counter(s)
        
        verify = []
        unique = []
        for i in s_count:
            verify.append(s_count[i])
            if s_count[i] == 1:
                unique.append(i)

        if 1 not in verify:
            return -1
                
        for idx, letter in enumerate(list(s)):
            if letter in unique:
                return idx