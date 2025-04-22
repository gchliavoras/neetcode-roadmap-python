class Solution:
#Find Minimum in Rotated Sorted Array
#You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:
#[3,4,5,6,1,2] if it was rotated 4 times.
#[1,2,3,4,5,6] if it was rotated 6 times.
#Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.
#Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.
#A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?
  def findMin(self, nums: list[int]) -> int:
    
    if nums[0] < nums[-1]: #Check if array rotated n times, and is sorted.
      return nums[0]
    
    n = len(nums)  
    left, right = 0, n - 1
    while left <= right:
      
      mid = left + (right - left) // 2
      if nums[mid] < nums[right]:
        right = mid 
      
      else:
        left = mid + 1
    
    return nums[mid]

nums=[[3,4,5,6,1,2], [4,5,0,1,2,3]]

if __name__ == "__main__":
  solution = Solution()
  for num in nums:
    print(solution.findMin(num))