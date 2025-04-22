class Solution:
#You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
#Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.
#Your solution must run in O(logn) time.
  def search(self, nums: list[int], target: int) -> int:
    n = len(nums)
    left, right = 0, n - 1
    
    if target < nums[0] or target > nums[-1]:
      return -1
      
    while left <= right:
      mid = left + (right - left) // 2
      
      if nums[mid] == target:
        return mid
      
      elif nums[mid] > target:
        right = mid - 1
        
      else:
        left = mid + 1
    
    return -1
  
nums = [-1,0,2,4,6,8]
target = 1

if __name__ == "__main__":
  solution = Solution()
  print(solution.search(nums, target))