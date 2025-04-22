class Solution:
#Container With Most Water
#You are given an integer array heights where heights[i] represents the height of the ith bar.
#You may choose any two bars to form a container. Return the maximum amount of water a container can store.
  def maxArea(self, heights: list[int]) -> int:
    maxArea = 0
    left, right = 0, len(heights) - 1 #Set up two pointers
    while left < right:
      currentArea = (min(heights[left], heights[right])) * (right - left)
      maxArea = max(currentArea, maxArea)
      
      print(currentArea, left, right)
      if heights[left] < heights[right]:
        left += 1
      elif heights[left] > heights[right]:
        right -= 1
      else:
        left += 1
        right -= 1
    return maxArea
      

heights = [1,7,2,5,12,3,500,500,7,8,4,7,3,6]

if __name__ == "__main__":
  solution = Solution()
  print(solution.maxArea(heights))