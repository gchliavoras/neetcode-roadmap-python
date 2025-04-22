class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0  # Frequency of the most common character in the current window
        count = {}  # Dictionary to store the frequency of characters in the window
        start = 0  # Start of the sliding window
        max_length = 0  # Result: maximum length of the substring
        #Loop end through string characters.
        for end in range(len(s)):
          #Add current character to count, and update max_freq accordingly.
          count[s[end]] = count.get(s[end], 0) + 1
          max_freq = max(max_freq, count[s[end]])
          #If invalid, shorten window until it is valid again.
          while end - start + 1 - max_freq > k:
            count[s[start]] -= 1
            start += 1
          #Biggest substring with given endpoint. Update max_length accordingly.
          max_length = max(max_length, end - start + 1)

        return max_length

s = "AAABABB"
k = 2

if __name__ == "__main__":
  solution = Solution()
  print(solution.characterReplacement(s, k))