#FRIEND CIRCLES
"""
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. 
For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. 
And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. 
If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. 
And you have to output the total number of friend circles among all the students.
"""
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        N=len(M) #number of students
        unionFind=list(range(N)) #indices
        
        def find(x):
            if unionFind[x]!=x: 
                return find(unionFind[x])
            else: return x
        
        #check if there is a relationship between each student
        for i in range(N):
            for j in range(N):
                #if there is, check if there are other relations
                if M[i][j] == 1:
                    unionFind[find(i)]=find(j)
        
        friendships= []
        for i in range(N):
            friendships.append(find(i))
      
        friendshipCircles = len(set(friendships))
                    
        return friendshipCircles

