#MINIMUM NUMNBER OF ARROWS TO BURST BALLOONS
#https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        
        if len(points) == 0:
            return 0
        if len(points) == 1:
            return 1
        
        arrows = 1
        
        arrow = points[0][1]
        
        for i in points:
            print(i)
            first_element = i[0]
            second_element = i[1]
            if arrow <= second_element:
                if arrow < first_element:
                    arrow = second_element
                    print(arrow)
                    arrows+=1
        
        return arrows