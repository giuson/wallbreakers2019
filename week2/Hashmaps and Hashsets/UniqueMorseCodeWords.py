#UNIQUE MORSE CODE WORDS
#https://leetcode.com/problems/unique-morse-code-words/

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dictionary = {}
        
        #Create dictionary that maps letters to morse code representation
        x=0
        for a in alphabet:
            dictionary[a]=morseCode[x]
            x+=1
        
        #Transform each word to morse code representation and append to array
        transformation = []
        for i, word in enumerate(words):
            transformation.append([])
            for char in word:
                morse = dictionary.get(char)
                transformation[i].append(morse)
        
        #Concatenate every word
        concatenatedList = []
        for i in transformation:
            concatenated = ''.join(i)
            concatenatedList.append(concatenated)
        
        #Find number of unique concatenations
        s = set(concatenatedList)
        
        return len(s)