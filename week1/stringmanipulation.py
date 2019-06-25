#REVERSE STRING
#function that reverses a string
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse() #this method reverses the elements of a given list

#REVERSE WORDS IN A STRING
"""
Given a string, reverse the order of characters in each word within a sentence 
while still preserving whitespace and initial word order.
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        newArray=[]

        #separate by whitespace
        s.split(' ')
        li = list(s.split(" ")) 
        
        #append the inverse to new array
        for i in li:
            newArray.append(i[::-1])
        
        #put together all inverted words
        final = " ".join(str(x) for x in newArray)
        return final

#VALID PALINDROME
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        noSpecialChars=''.join([i for i in s if i.isalnum()]) #keep only alphanumeric characters
        lowercase = list(noSpecialChars.lower()) #change all chars to lowercase
        reverse = lowercase[::-1] #create reverse array
        
        #check if the arrays are the same
        if lowercase == reverse:
            return True
        else:
            return False   

#REVERSE VOWELS OF A STRING
#Write a function that takes a string as input and reverse only the vowels of a string.
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        word = list(s)
        
        #replace all vowels with a placeholder and append vowels to new list
        for idx, i in enumerate(word):
            if i in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                word[idx] = 'placeholder'
                vowels.append(i)
        
        #reverse vowels in word
        reverseVowels = vowels[::-1]
        
        #replace all placeholders with vowels in reverse order from reverseVowels
        x=0
        for idx, i in enumerate(word):
            if (i == 'placeholder') & (x < len(reverseVowels)):
                word[idx] = reverseVowels[x]
                x+=1
        
        replaced = ''.join(word)
        return str(replaced)
