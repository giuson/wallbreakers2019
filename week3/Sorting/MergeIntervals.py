#MERGE INTERVALS
#https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0 or len(intervals) == 1:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        curr = intervals[0][1]
        merged = [[intervals[0][0]]]
        
        x=0
        for i in intervals:
            first_element = i[0]
            second_element = i[1]
            print(merged)
            if curr < first_element:
                #new interval
                merged.append(i)
                if curr < second_element:
                    curr = second_element
                x+=1
            else:
                if curr < second_element:
                    curr = second_element
                    if len(merged[x]) == 2:
                        merged[x][1] = curr
                    else:
                        merged[x].append(curr)
                else:
                    if len(merged[x]) == 2:
                        merged[x][1] = curr
                    else:
                        merged[x].append(curr)
                
        return merged