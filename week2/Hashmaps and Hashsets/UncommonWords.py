#UNCOMMON WORDS FROM TWO SENTENCES
#https://leetcode.com/problems/uncommon-words-from-two-sentences/

from collections import defaultdict

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        freqdict = defaultdict(int)
        
        #separate each word
        a = A.split(' ')
        b = B.split(' ')
        
        output = []
        
        #put both sentences in one array
        combination = a + b
        
        #increase count, accdg to number of times word is repeated
        for i in combination:
            freqdict[i]+=1
        
        #if count is 1, append to output array
        for i in freqdict:
            if freqdict.get(i)==1:
                output.append(i)
    
        return output