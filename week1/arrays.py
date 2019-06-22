#SORT ARRAY BY PARITY
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        evens = []
        odds = []
        for i in A:
            if i%2==0:
                evens.append(i)
            else:
                odds.append(i)
        return evens+odds

#TRANSPOSE MATRIX
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        newArray = []
        for i in A[0]:
            newArray.append([])
        for i in A:
            x=0
            for j in i:
                newArray[x].append(j)
                x+=1
        return newArray

#FLIPPING AN IMAGE
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        newArray=[]
        for i in A:
            newArray.append(i[::-1])
            
        
        for i in newArray:
            x=0
            for n, j in enumerate(i):
                print(i)
                if j==1:
                    i[n]=0
                else:
                    i[n]=1
                x+=1

        return newArray

                
            
            

                
                
