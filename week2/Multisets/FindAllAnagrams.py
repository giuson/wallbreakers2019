#FIND ALL ANAGRAMS
#https://leetcode.com/problems/find-all-anagrams-in-a-string/

import collections

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        output = []
        window_size = len(p)
        pattern = collections.Counter(p)
        window = collections.Counter(s[:window_size-1]) 

        for i in range(window_size-1,len(s)):
            letter = s[i]
            window[letter] += 1 
            firstLetterIndex = i - window_size + 1 
            firstLetter = s[firstLetterIndex]

            if window == pattern:    
              output.append(firstLetterIndex) 
            
            window[firstLetter] -= 1 
            if window[firstLetter] == 0:
                window.pop(firstLetter)

        return output
