#SORT ARRAY BY PARITY
"""
Given an array A of non-negative integers, 
return an array consisting of all the even elements of A, 
followed by all the odd elements of A.
"""
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        evens = []
        odds = [] 

        #sort even and odd elements into separate arrays
        for i in A:
            if i%2==0:
                evens.append(i)
            else:
                odds.append(i)

        #return as one array with evens first followed by odds
        return evens+odds

#TRANSPOSE MATRIX
"""
The transpose of a matrix is the matrix flipped over it's main diagonal, 
switching the row and column indices of the matrix.
"""
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        transposed = []

        #initialize number of rows
        #number of rows = number of elements in first array
        for i in A[0]:
            transposed.append([])

        #go through each row in given matrix
        for rows in A:
            x=0 #index of row
            #go through each element in each row and append to new column
            for element in rows:
                transposed[x].append(element)
                x+=1 #move to next row

        return transposed

#FLIPPING AN IMAGE
"""
Given a binary matrix A, we want to flip the image horizontally, 
then invert it, and return the resulting image.
"""
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        newMatrix=[]

        #for each row in given matrix, append the inverse to new matrix
        for i in A:
            newMatrix.append(i[::-1])
        
        #go through each row and change 0's to 1's and 1's to 0's
        for i in newMatrix:
            #go through all elements in each row and make the switch, n is index
            for n, element in enumerate(i):
                print(i)
                if element==1:
                    i[n]=0
                else:
                    i[n]=1

        return newMatrix

                
            
            

                
                
