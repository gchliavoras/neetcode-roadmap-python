'''Contains Duplicate
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.'''

class Solution:
  def hasDuplicate(self, nums: list[int]) -> bool:
    for i in range(len(nums)):
      for j in range(i+1,len(nums)):
        if nums[i] == nums[j]:
          return True
          
    return False
    
inp_array: list[str] = input("Input the array to test, seperated by spaces.").split()
nums: list[int] = [int(num) for num in inp_array]
    
if __name__ == "__main__":
  solution=Solution()
  if solution.hasDuplicate(nums):
    print("The list has duplicates.")
  else:
    print("The list has no duplicates.")