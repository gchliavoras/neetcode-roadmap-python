class Solution:
#Generate Parentheses
#You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.
  def generateParenthesis(self, n: int) -> list[str]:
    stack = []
    res = []
    def backtrack(n_open, n_closed):
      if n_open == n_closed == n:
        res.append("".join(stack))
        return
      
      if n_open < n:
        stack.append("(")
        backtrack(n_open + 1, n_closed)
        stack.pop()
        
      if n_open > n_closed:
        stack.append(")")
        backtrack(n_open, n_closed + 1)
        stack.pop()
        
    backtrack(0, 0)
    return res

n = int(input("Input n:"))

if __name__ == "__main__":
  solution = Solution()
  print(solution.generateParenthesis(n))