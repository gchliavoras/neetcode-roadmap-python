class Solution:
#Trapping Rain Water
#You are given an array non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.
#Return the maximum area of water that can be trapped between the bars.
#You should aim for a solution as good or better than O(n) time and O(n) space, where n is the size of the input array.
  def trap(self, height: list[int]) -> int:
    n = len(height)
    trappedWater = 0
    
    if n < 3: #At least 3 elements required to form a lake.
      return trappedWater

    leftMaximum: list[int] = [0] * n 
    rightMaximum: list[int] = [0] * n
    
    for i in range(1, n - 1): #Populate the two maximum lists. First and last elements ignored, as they can't hold water.
      leftMaximum[i] = max(leftMaximum[i - 1], height[i - 1])
      rightMaximum[-1 - i] = max(rightMaximum[-i], height[-i])
      
    for i in range(1, n - 1):
      waterLevel = min(leftMaximum[i], rightMaximum[i])
      if waterLevel < height[i]:
        continue
      trappedWater += waterLevel - height[i]
    return trappedWater

height = [0,2,0,3,1,0,1,3,2,1]    
if __name__ == "__main__":
  solution = Solution()
  print(solution.trap(height))