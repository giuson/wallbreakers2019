#DESIGN HASHSET
#https://leetcode.com/problems/design-hashset/

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = []

    def add(self, key: int) -> None:
        if key in self.set:
            i = self.set.index(key)
            self.set[i] = key
        else:
            self.set.append(key)

    def remove(self, key: int) -> None:
        if key in self.set:
            i = self.set.index(key)
            self.set.pop(i)
        
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.set:
            return True
        return False