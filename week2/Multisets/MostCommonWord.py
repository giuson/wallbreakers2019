#MOST COMMON WORD
#https://leetcode.com/problems/most-common-word/

import re
import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'\w+', paragraph)
        
        lowercase_words = []
        for i in words:
            if i.lower() not in banned:
                lowercase_words.append(i.lower())
        
        word_counter = collections.Counter(lowercase_words)

        for word, count in word_counter.most_common(1):
            return word