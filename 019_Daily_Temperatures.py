class Solution:
#Daily Temperatures
#You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.
#Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.
  def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
    res = [0] * len(temperatures)
    stack = []
    
    for i in range(len(temperatures)):
      if not stack or temperatures[i] <= temperatures[stack[-1]]:
        stack.append(i)
        
      else:
        while stack and temperatures[i] > temperatures[stack[-1]]:
          res[stack[-1]] = i - stack[-1]
          stack.pop()
          
        stack.append(i)
        
    return res
    
temperatures = [30,38,30,36,35,40,28]

if __name__ == "__main__":
  solution = Solution()
  print(solution.dailyTemperatures(temperatures))