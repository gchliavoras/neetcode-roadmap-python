class Solution:
#Valid Palindrome
#Given a string s, return true if it is a palindrome, otherwise return false.
#A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
#You should aim for a solution with O(n) time and O(1) space, where n is the length of the input string.
  def isPalindrome(self, s: str) -> bool:
    s = s.replace(" ","")
    for i in range(len(s) // 2):
      left_char = s[i].lower()
      right_char = s[-i-1].lower()
      if left_char != right_char:
        return False
    return True

inputStrings = ["a caT tac A", "a cat is here"]

if __name__ == "__main__":
  solution = Solution()
  for inputString in inputStrings:
    print(solution.isPalindrome(inputString))
    