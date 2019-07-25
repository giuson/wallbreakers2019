#ASSIGN COOKIES
#https://leetcode.com/problems/assign-cookies/

import collections

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        satisfied = []
        
        #REMOVE ALL COMMON ELEMENTS
        common = set(g) & set(s)
        satisfied.extend(common)
        
        for i in satisfied:
            g.remove(i)
            s.remove(i)

        if len(s)==0 or len(g) == 0:
            return len(satisfied)
        else:
            satisfiedCount = len(satisfied)

            while len(s)>0 and len(g)>0:
                if s[-1] < g[-1]:
                    g.pop()
                else:
                    satisfiedCount += 1
                    s.pop()
                    g.pop()

            return satisfiedCount