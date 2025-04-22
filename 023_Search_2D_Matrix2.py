class Solution:
#You are given an m x n 2-D integer array matrix and an integer target.
#Each row in matrix is sorted in non-decreasing order.
#The first integer of every row is greater than the last integer of the previous row.
#Return true if target exists within matrix or false otherwise.
#Write a solution that runs in O(log(m * n)) time?
  def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
    m = len(matrix)
    n = len(matrix[0])
    left, right = 0, m * n - 1
      
    while left <= right:
      mid = left + (right - left) // 2
      mid_value = matrix[mid // n][mid % n]
      
      if  mid_value == target:
        return True
      
      elif mid_value > target:
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