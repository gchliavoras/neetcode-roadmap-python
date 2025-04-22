class Solution:
#Largest Rectangle In Histogram
#You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.
#Return the area of the largest rectangle that can be formed among the bars.
  def largestRectangleArea(self, heights: list[int]) -> int:
    asc_stack = []
    maxArea = 0
    n = len(heights)

    for i in range(n):
      while asc_stack and heights[i] < heights[asc_stack[-1]]:
        height = heights[asc_stack.pop()]
        width = i if not asc_stack else i - asc_stack[-1] - 1
        maxArea = max(height * width, maxArea)
      
      asc_stack.append(i)
      
    while asc_stack:
      height = heights[asc_stack.pop()]
      width = n if not asc_stack else n - asc_stack[-1] - 1
      maxArea = max(height * width, maxArea)
        
    return maxArea
    
heights = [8,7,1,7,2,2,4]

if __name__ == "__main__":
  solution = Solution()
  print(solution.largestRectangleArea(heights))
