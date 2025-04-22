'''
Group Anagrams
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
'''
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
      wordDict = {}
      for string in strs:
        charFreq = [0]*26
        for char in string:
          charFreq[ord(char.lower())-ord("a")] += 1
        wordDict.setdefault(tuple(charFreq), []).append(string)
      print(list(wordDict.values()))
      return list(wordDict.values())

Input = ["act","pots","tops","cat","stop","hat"]

if __name__ == "__main__":
  solution = Solution()
  solution.groupAnagrams(Input)