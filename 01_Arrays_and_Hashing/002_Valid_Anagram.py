'''
Valid Anagram
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      a1 = [i for i in s]
      a2 = [i for i in t]
      if sorted(a1) == sorted(a2):
        return True
      return False
      
s: str = input("Input first string")
t: str = input("Input second string")

if __name__ == "__main__":
  solution = Solution()
  if solution.isAnagram(s,t):
    print("The two strings are anagrams")
  else:
    print("The two strings are not anagrams")
  