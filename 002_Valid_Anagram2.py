'''
Valid Anagram
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t):
        return False
      dict1, dict2 = {}, {}
      for letter in s:
        dict1[letter] = dict1.get(letter, 0) + 1
      for letter in t:
        dict2[letter] = dict2.get(letter, 0) + 1
      if dict1 == dict2:
        return True
      
s: str = input("Input first string")
t: str = input("Input second string")

if __name__ == "__main__":
  solution = Solution()
  if solution.isAnagram(s,t):
    print("The two strings are anagrams")
  else:
    print("The two strings are not anagrams")
  