'''
Group Anagrams
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
'''
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
      charDict = {}
      for i in range(0,len(strs)): #Populate the nested dictionary of characters in each string.
        charDict[i] = {}
        for char in strs[i]:
          charDict[i][char] = charDict[i].get(char, 0) + 1
      Output = []
      seen = []
      for i in range(0, len(strs)): 
        if i not in seen:
          Output.append([])
          Output[-1].append(strs[i])
          for j in range(i+1, len(strs)):
            if len(strs[i]) == len(strs[j]):
              if charDict[i] == charDict[j]:
                Output[-1].append(strs[j])
                seen.append(j)
      print(Output)
      return Output
      
Input = ["act","pots","tops","cat","stop","hat"]

if __name__ == "__main__":
  solution = Solution()
  solution.groupAnagrams(Input)

