#IS SUBSEQUENCE
#https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        test = []
        
        if len(s) < 1:
            return True
        
        if s[0] in t:
            index = t.index(s[0])
            test.append(index)
        else:
            return False

        for i in s[1:]:
            next_index = t.find(i, index)
            if next_index == -1:
                return False
            else:
                test.append(next_index)
                index = next_index+1
        
        if(test == sorted(test)):
            return True
        else:
            return False