#SORT CHARACTERS BY FREQUENCY
#https://leetcode.com/problems/sort-characters-by-frequency/

import collections

class Solution:
    def frequencySort(self, s: str) -> str:
        s_count = collections.Counter(s)
        
        sortedList = []
        
        for char, count in s_count.most_common(len(set(s))):
            for i in range(count):
                sortedList.append(char)
        
        output = "".join(sortedList)
        
        return output