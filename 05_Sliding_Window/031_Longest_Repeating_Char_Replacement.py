#Longest Repeating Character Replacement
#You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.
#After performing at most k replacements, return the length of the longest substring which contains only one distinct character.
class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    #Initialize variables
    maxLength = 0
    start = 0
    otherChar_counter = 0
    currentChar_counter = 0
    otherCharStore = {}
    #Loop end through all chars of the string.
    for end in range(len(s)):
      #Update otherCharStore and otherChar_counter according to current char, and check if current char in store.
      current_char = s[end]
      if current_char in otherCharStore:
        currentChar_counter = otherCharStore.pop(current_char) 
        otherChar_counter -= currentChar_counter
      else:
        currentChar_counter = 0
      #Update currentChar_counter with current char.
      currentChar_counter += 1
      #If valid, widen window until substring is no longer valid.
      while otherChar_counter <= k and start > 0:
        start -= 1
        #Update otherCharStore if start char is not current char.
        if s[start] != current_char:
          if s[start] not in otherCharStore:
            otherCharStore[s[start]] = 1
          else:
            otherCharStore[s[start]] += 1
          #Update otherChar_counter
          otherChar_counter += 1
        #Update currentChar_counter if s[start] == current char
        else:
          currentChar_counter += 1
      #If invalid, shorten window until substring is once more valid.
      while otherChar_counter > k and start <= end:
        #Remove start char from otherCharStore if it is not the current char.
        if s[start] != current_char:
          otherCharStore[s[start]] -= 1
          otherChar_counter -= 1
        #Update currentChar_counter if s[start] == current char.
        else:
          currentChar_counter -= 1
        #Update start pointer.  
        start += 1
      #Biggest substring with current char. Adjusted for changes made further down until k, or until end of string.
      current_max = end - start + 1 + k - otherChar_counter
      #If the whole string is valid, exit early and return the whole string.
      if current_max >= len(s):
        return len(s)
      #Update maxLength if needed.
      maxLength = max(maxLength, current_max)
      #Update otherCharStore and otherChar_counter with current char, before moving on the next char.
      otherCharStore[current_char] = currentChar_counter
      otherChar_counter += currentChar_counter

    return maxLength

s = "AAABABB"
k = 2

if __name__ == "__main__":
  solution = Solution()
  print(solution.characterReplacement(s, k))