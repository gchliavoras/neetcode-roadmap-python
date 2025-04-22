class Solution:
#Valid Parentheses
#You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
#The input string s is valid if and only if:
#Every open bracket is closed by the same type of close bracket.
#Open brackets are closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.
#Return true if s is a valid string, and false otherwise.
  def isValid(self, s: str) -> bool:
    stack: list[str] = []
    bracketPairing: dict[str, str] = {
      ")": "(",
      "]": "[",
      "}": "{"
    }
    for char in s:
      if char not in bracketPairing:
        stack.append(char)
      
      else:
        if not stack:
          return False
        elif bracketPairing[char] != stack[-1]:
          return False
        else:
          stack.pop()
    
    return not stack
    
test = ["{[()]}", "{[()()][()()]}", "{[}]"]

if __name__ == "__main__":
  solution = Solution()
  for s in test:
    print(solution.isValid(s))