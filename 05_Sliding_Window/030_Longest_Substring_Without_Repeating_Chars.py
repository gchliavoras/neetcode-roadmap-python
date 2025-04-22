#Longest Substring Without Repeating Characters
#Given a string s, find the length of the longest substring without duplicate characters.
#A substring is a contiguous sequence of characters within a string.
class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    seen = set()
    start = 0
    maxLength = 0
    
    for end in range(len(s)):
      #Advance start of sliding window until there are no duplicates.
      while s[end] in seen:
        seen.remove(s[start])
        start += 1
      #Test length of current window, add current element to seen and advance end.
      maxLength = max(maxLength, end - start + 1)
      seen.add(s[end])
    
    return maxLength

s = "abcabc"

if __name__ == "__main__":
  solution = Solution()
  print(solution.lengthOfLongestSubstring(s))