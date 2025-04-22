#Minimum Window Substring
#Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".
#You may assume that the correct output is always unique.
class Solution:
  def minWindow(self, s: str, t: str) -> str:
    #Initialize variables.
    res = "" #Output
    start = 0
    matches = 0
    targetChars, windowChars = {}, {}
    #Preliminary check.``
    if len(s) < len(t):
      return res
    #Initialize and populate target and window character counters.
    for char in t:
      targetChars[char] = targetChars.get(char, 0) + 1
      windowChars[char] = 0
    #Start sliding window.
    for end in range(len(s)):
      #Add new char to windowChars, and update matches.
      rightChar = s[end]
      if rightChar in targetChars:
        windowChars[rightChar] += 1
        if windowChars[rightChar] == targetChars[rightChar]:
          matches += 1
      #If the current substring is valid.
      if matches == len(targetChars):
        #Shorten the window until the substring is no longer valid.
        while matches == len(targetChars):
          leftChar = s[start]
          #Update windowChars and matches if necessary.
          if leftChar in targetChars:
            if windowChars[leftChar] == targetChars[leftChar]:
              matches -= 1
            windowChars[leftChar] -= 1
          #Advance start pointer.
          start += 1
        #And update the shortest valid substring encountered so far.
        if len(res) > len(s[start-1:end+1]) or res == "":
          res = s[start-1:end+1]
          
    return res

s = input("Input s:")
t = input("Input t:")

if __name__ == "__main__":
  solution = Solution()
  print(solution.minWindow(s,t))