class Solution:
#You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:
#[3,4,5,6,1,2] if it was rotated 4 times.
#[1,2,3,4,5,6] if it was rotated 6 times.
#Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.
#You may assume all elements in the sorted rotated array nums are unique.
#A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?
  def search(self, nums: list[int], target: int) -> int:
    
    n = len(nums)
    left, right = 0, n - 1
    while left <= right:
      
      mid = (right + left) // 2
      if nums[mid] == target:
        return mid
        
      if nums[mid] < nums[right]: 
      #Right sorted subarray
        if nums[mid] > target or nums[right] < target:
          right = mid - 1
        
        else:
          left = mid + 1
      else:
      #Left sorted subarray
        if nums[mid] < target or nums[left] > target:
          left = mid + 1
        
        else:
          right = mid - 1
        
    return -1

nums = [3,4,5,6,1,2]
target = 7

if __name__ == "__main__":
  solution = Solution()
  print(solution.search(nums, target))