#VALID SUDOKU
#https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowCheck = []
        x=-1
        for row in board:
            rowCheck.append([])
            x+=1
            for element in row:
                if element!=".":
                    rowCheck[x].append(element)
            if len(rowCheck[x])!=len(set(rowCheck[x])):
                return False
        
        colCheck = [[],[],[],[],[],[],[],[],[]]
        for row in board:
            x=0
            for idx, element in enumerate(row):
                if element!=".":
                    colCheck[idx].append(element)
                    x=idx

        for i in colCheck:
            if len(i)!=len(set(i)):
                return False
            
        boxCheck = [[],[],[],[],[],[],[],[],[]]
        x=0
        for i, row in enumerate(board):
            if i%3 == 0:
                x=i
                boxCheckindex = x
            else:
                x = boxCheckindex
            for idx, element in enumerate(row):
                boxCheck[x].append(row[idx])
                _idx = idx+1
                if _idx%3 == 0:
                    x+=1
        
        finalCheck = []
        x=-1
        for box in boxCheck:
            finalCheck.append([])
            x+=1
            for element in box:
                if element!=".":
                    finalCheck[x].append(element)
            if len(finalCheck[x])!=len(set(finalCheck[x])):
                return False
        
        return True