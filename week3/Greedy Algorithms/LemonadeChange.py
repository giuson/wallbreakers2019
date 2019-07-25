#LEMONADE CHANGE
#https://leetcode.com/problems/lemonade-change/

import collections

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = []
        
        if bills[0] != 5:
            return False
        
        change.append(bills[0])
        changeCount = collections.Counter(change)
        
        for i in bills[1:]:
            if i == 5:
                changeCount[5] += 1
            if i == 10:
                if changeCount[5] > 0:
                    changeCount[10] += 1
                    changeCount[5] -= 1
                else:
                    return False
            if i == 20:
                if changeCount[10] > 0 and changeCount[5] > 0:
                    changeCount[20] += 1
                    changeCount[10] -= 1
                    changeCount[5] -= 1
                elif changeCount[5] > 2:
                    changeCount[20] += 1
                    changeCount[5] -= 3
                else:
                    return False
        
        return True