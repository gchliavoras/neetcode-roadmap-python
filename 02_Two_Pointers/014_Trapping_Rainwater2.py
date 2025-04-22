class Solution:
#Trapping Rain Water
#You are given an array non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.
#Return the maximum area of water that can be trapped between the bars.
#You should aim for a solution as good or better than O(n) time and O(n) space, where n is the size of the input array.
  def trap(self, height: list[int]) -> int:
    len(height) = n
    trappedWater = 0
    
    if n < 3: #At least 3 elements required to form a lake.
      return trappedWater

    left = 0 #Initialize left pointer. Left will stay at left bank of first lake.
    while left < n - 2: #Left pointer bounded by n - 2, as the last possible lake would have a width of at least 1.
      if height[left] <= height[left + 1]: #Skip elements that cannot be on the edge of a lake from the left.
        left += 1
        continue
#Left now either at left bank or the loop ran through all elements without any valid candidates.    
    if left == n - 3 and height[left] <= height[left + 1]: #If no candidates found.
        return trappedWater  #Return 0.

    right = n - 1 #Initialize right pointer. Right will stay at right bank of last lake.
    while right > left: 
      if height[right] <= height[right - 1]: #Skip elements that cannot be on the edge of a lake from the right.
        right -= 1
        continue
#Right is now either at right bank or the loop ran through all elements without any valid candidates.    
    if right == left + 1: #If right ended up next to left, no valid candidates found.
        return trappedWater  #Return 0.

    lakebed = [] #Initialize array for measuring contributions of the lakebed. Contains indexes of the elements between peaks.
    peaks = [] #Initialize array for storing peak indexes.
    for i in range(left + 1, right): 
      
        if height[i] <= height[i + 1]: #If i is not a peak, then it is part of a lakebed.
          lakebed.append(i)
        else: 
          peaks.append([height[i], i])
    
    lakeLevel = min(height[left], height[right])
    if peaks == []: #If there were no internal peaks, then left and right form the only lake.
      trappedWater = lakeLevel * (right - left - 1) - sum(lakebed)
      return trappedWater
    
    else:
      peaks.sort() #Sort peaks by height
      for peak in peaks:
        if peak[1] >= lakeLevel: #peak[0] and peak[1] are the height, and index of each peak respectively.
          
    return trappedWater