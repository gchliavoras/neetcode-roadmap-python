class Solution:
#Trapping Rain Water
#You are given an array non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.
#Return the maximum area of water that can be trapped between the bars.
#You should aim for a solution as good or better than O(n) time and O(n) space, where n is the size of the input array.
  def trap(self, height: list[int]) -> int:
    len(height) = n
    trappedWater = 0
    if n < 3:
      return trappedWater

    left = 0 #Initialize left pointer. Left will stay at a left bank of a lake, while right advances to find the right bank.
    while left < n - 2: #Left pointer bounded by n - 2, as the last possible lake would have a width of at least 1.
  
      if height[left] <= height[left + 1]: #Skip elements that cannot be on the edge of a lake from the left.
        left += 1
        continue #After end of this loop, left will be positioned at a left bank.
      
      lakebed = 0 #Initialize variable for measuring contributions of the lakebed. Initialized for each new lake.  
      right = left + 1 #Initialize right pointer, next to the left pointer.
      while right < n - 1: #Initialize search for right bank.
      
        if height[left] <= height[right]: #Arrived at right bank.
          left = right + 1
          break #Search for next lake and left bank.
          
        elif height[right] <= height[right + 1]: #Skip middle elements of the lake. 
        #possibly start at right = left+2 and check right-1, instead of right+1.
          lakebed += height[right]
          right += 1  
          continue
          
        else: #Arrived at local peak. Calculate water and check if global.
          lakeWater = height[right] * (right - left - 1) - lakebed
          localPeak = right 
          
      trappedWater += lakeWater
    
    return trappedWater