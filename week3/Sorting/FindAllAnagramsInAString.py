#FIND ALL ANAGRAMS IN A STRING
#https://leetcode.com/problems/find-all-anagrams-in-a-string/

import collections

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        P = list(p)
        S = list(s)
        P.sort()
        pattern_len = len(p)
        
        test = []
        indices = []
        
        for i in S[:pattern_len]:
            test.append(i)
        
        test.sort()
        
        if P == test:
            indices.append(0)

        remove = -1
        for idx, i in enumerate(S[pattern_len:]):
            currIdx = idx+pattern_len
            remove += 1
            test.remove(S[remove])
            position = bisect.bisect(test, i)
            bisect.insort(test, i)
            if P == test:
                indices.append(currIdx-(pattern_len-1))
        
        return indices