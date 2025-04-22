#Permutation in String
#You are given two strings s1 and s2.
#Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.
#Both strings only contain lowercase letters.
class Solution:
  def checkInclusion(self, s1: str, s2: str) -> bool:
    #Preliminary check.
    if len(s1) > len(s2):
      return False
    #Initialize target hashmap and window hashmap.
    targetChars, windowChars = {}, {}
    for char in "abcdefghijklmnopqrstuvwxyz":
      targetChars[char], windowChars[char] = 0, 0
    #Populate target hashmap.  
    for char in s1:
      targetChars[char] += 1
    #Initialize sliding window.
    start = 0
    for end in range(len(s2)):
      #Add next character to window hashmap.
      windowChars[s2[end]] += 1
      #Start advancing start as soon as windows is the same size as s1.
      if end - start + 1 > len(s1):
        windowChars[s2[start]] -= 1
        start += 1
      #Compare window and target hashmaps.
      if windowChars == targetChars:
        return True
    #Loop finished with no match.
    return False