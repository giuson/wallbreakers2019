#POW(X,N)
#https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n > 1:
            value = self.myPowHelper(x, x, n)
            return value
        else:
            newX = 1/x
            value = self.myPowHelper(newX, newX , abs(n))
            return value            

    def myPowHelper(self, prev, x, n):
        if n == 1:
            return prev
        elif n % 2 == 0:
            value = self.myPowHelper(prev, x, n//2)
            result = value * value
            prev=result
            return result
        else:
            value = self.myPowHelper(prev, x, n//2)
            result = x * value * value
            prev=result
            return result