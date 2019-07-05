#WORD PATTERN
#https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        patternList = []
        
        #store both inputs into separate arrays
        for i in pattern:
            patternList.append(i)
        strList = str.split(' ')
        
        #check if arrays are equal in size
        if len(patternList)!=len(strList):
            return False
        
        #map similar indices from both arrays to each other 
        mapped = list(zip(patternList, strList))
        
        #create a dictionary where key=pattern character, value=string, mapped accdg to index
        dictionary={}
        
        for eachPair in mapped:
            if eachPair[0] in dictionary:
                dictionary[eachPair[0]].append(eachPair[1])
            else:
                dictionary[eachPair[0]] = [eachPair[1]]
        
        #check if len(key) == len(set(values))
        keys=[] #store list of keys
        for key in dictionary:
            keys.append(key)
        
        vals =[] #store list of values
        for string in dictionary.values():
            if len(set(string))>1: #check if key has more than 1 unique value
                return False
            vals.append(set(string).pop())
        
        return len(keys) == len(set(vals))