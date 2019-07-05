#GROUPS OF SPECIAL-EQUIVALENT STRINGS
#https://leetcode.com/problems/groups-of-special-equivalent-strings/

class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        newArray=[]
        
        if len(A[0])==1:
            return len(set(A))
                
        elif len(A[0])==2:
            return len(A)
            
        else:
            x=-1
            for eachString in A:
                newArray.append({})
                x+=1
                for idx, eachChar in enumerate(eachString):
                    if eachChar in newArray[x]:
                        if idx % 2 == 1:
                            newArray[x][eachChar].append("1")
                        if idx % 2 == 0:
                            newArray[x][eachChar].append("0")
                    else:
                        if idx % 2 == 1:
                            newArray[x][eachChar] = ["1"]
                        if idx % 2 == 0:
                            newArray[x][eachChar] = ["0"]
           
            tmp=[]

            for i in newArray:
                if i not in tmp:
                    tmp.append(i)        
            
            return len(tmp)