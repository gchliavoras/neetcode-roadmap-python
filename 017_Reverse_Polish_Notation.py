class Solution:
#Evaluate Reverse Polish Notation
#You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
#Return the integer that represents the evaluation of the expression.
#The operands may be integers or the results of other operations.
#The operators include '+', '-', '*', and '/'.
#Assume that division between integers always truncates toward zero.
#tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100].
  def evalRPN(self, tokens: list[str]) -> int:
    stack = []
    
    for token in tokens:
      if token not in "+-*/":
        stack.append(int(token))
      
      elif len(stack) < 2:
        raise ValueError("Invalid RPN expression: not enough operands.")
      
      else:
        b = stack.pop()
        a = stack.pop()
          
        if token == "+":
          stack.append(a + b)
        elif token == "-":
          stack.append(a - b)
        elif token == "*":
          stack.append(a * b)
        else:
          stack.append(int(a / b))
    
    if len(stack) != 1:
      raise ValueError("Invalid RPN expression: too many numbers left.")
      
    return stack.pop()
    
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
if __name__ == "__main__":
  solution = Solution()
  print(solution.evalRPN(tokens))