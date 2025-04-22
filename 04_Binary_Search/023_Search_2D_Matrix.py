class Solution:
#You are given an m x n 2-D integer array matrix and an integer target.
#Each row in matrix is sorted in non-decreasing order.
#The first integer of every row is greater than the last integer of the previous row.
#Return true if target exists within matrix or false otherwise.
#Write a solution that runs in O(log(m * n)) time?
  def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
    n = len(matrix)
    left = 0
    
    if target < matrix[0][0] or target > matrix[-1][-1]: #Preliminary check
      return False
    
    if n == 1: #Edge case handling.
      return self.binarySearch(matrix[left], target)
    
    while left < n: #If dealing with a normal matrix and target, find if there is a possible column containing the target.
      if matrix[left][0] == target:
        return True
        
      elif matrix[left][0] > target:
        left -= 1
        return self.binarySearch(matrix[left], target)
        
      left += 1
    
    left -= 1 #If code reached here, left = n.
    return self.binarySearch(matrix[left], target) #Search last column.
  
  def binarySearch(self, nums: list[int], target: int) -> bool:
    n = len(nums)
    left, right = 0, n - 1
      
    while left <= right:
      mid = left + (right - left) // 2
      
      if nums[mid] == target:
        return True
      
      elif nums[mid] > target:
        right = mid - 1
        
      else:
        left = mid + 1
    
    return False

matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
targets = [10, 15]

if __name__ == "__main__":
  solution = Solution()
  for target in targets:
    print(solution.searchMatrix(matrix, target))