class Solution:
#Valid Palindrome
#Given a string s, return true if it is a palindrome, otherwise return false.
#A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
#You should aim for a solution with O(n) time and O(1) space, where n is the length of the input string.
  def isPalindrome(self, s: str) -> bool:
    s_filt = "".join(char.lower() for char in s if char.isalnum())
    left = 0
    right = len(s_filt) - 1
    while left < right:
      if s_filt[left] != s_filt[right]:
        return False
      left += 1
      right += -1
    return True

inputStrings = ["a caT% 5tac A", "a cat is here", "", "0"]

if __name__ == "__main__":
  solution = Solution()
  for inputString in inputStrings:
    print(f"'{inputString}' is palindrome: {solution.isPalindrome(inputString)}")
    