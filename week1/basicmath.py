#FIZZ BUZZ
"""
program that outputs the string representation of numbers from 1 to n.
for multiples of three it should output “Fizz” 
for the multiples of five output “Buzz”
For numbers which are multiples of both three and five output “FizzBuzz”.
"""
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizzBuzz = []

        #go through 1 to n and check if divisible by 5, 3, or both and append appropriate result
        for i in range(1, n+1):
            if i%15==0:
                fizzBuzz.append("FizzBuzz")
            elif i%5==0:
                fizzBuzz.append("Buzz")
            elif i%3==0:
                fizzBuzz.append("Fizz")
            else: fizzBuzz.append(str(i))

        return fizzBuzz
            
#PLUS ONE
"""Given a non-empty array of digits representing a non-negative integer, plus one to the integer."""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int("".join(map(str, digits))) #turn input into a number
        newNumber = number + 1 #add one
        output = list(map(int, str(newNumber))) #turn back into array
        return output
        
#POWER OF TWO
#Given an integer, write a function to determine if it is a power of two.
import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        test = int(math.log2(n))
        if n != 2**test:
            return False
        else:
            return True