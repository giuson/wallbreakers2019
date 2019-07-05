#HAPPY NUMBER
#https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        
        stringN = str(n)
        
        numbers = []
        ans = 0
        
        while stringN!="1":
            #empty the numbers array at every iteration
            if len(numbers) > 0:
                del numbers[:]
            
            #append the squares of the digits
            for i in stringN:
                numbers.append(int(i)*int(i))
            
            #get the sum and reassign as new stringN
            ans = str(sum(numbers))
            stringN = ans
            
            #CONDITIONS TO BREAK THE LOOP
            #first check if it's a single digit
            if len(stringN) == 1:
                #break the loop if it's 1
                if stringN == "1":
                    break
                #also break the loop if it's not a 7
                if stringN!="7":
                    stringN="0"
                    break
        
        return stringN == "1"