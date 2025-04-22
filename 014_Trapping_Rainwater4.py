class Solution:
#Trapping Rain Water
#You are given an array non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.
#Return the maximum area of water that can be trapped between the bars.
#You should aim for a solution as good or better than O(n) time and O(n) space, where n is the size of the input array.
  def trap(self, height: list[int]) -> int:
    
    n = len(height)
    if n < 3: #At least 3 elements required to form a lake.
      return trappedWater
    
    trappedWater = 0
    leftMax, rightMax = 0, 0
    left, right = 0, n - 1
    while left < right:
      
      if height[left] < height[right]:
        if height[left] >= leftMax:
          leftMax = height[left] 
        else:
          trappedWater += max(leftMax - height[left], 0)
        
        left += 1      
        
      else:
        if height[right] >= rightMax:
          rightMax = height[right]
        else:
          trappedWater += max(rightMax - height[right], 0)
        
        right -= 1
    
    return trappedWater

height = [2,1,2,1,2,1,2,1,2,1,2]
if __name__ == "__main__":
  solution = Solution()
  print(solution.trap(height))