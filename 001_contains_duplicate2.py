'''Contains Duplicate
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.'''

class Solution:
  def hasDuplicate(self, nums: list[int]) -> bool:
    seen=set()
    for i in nums:
      if i in seen:
        return True
      seen.add(i)
      
    return False
    
inp_array: list[str] = input("Input the array to test, seperated by spaces.").split()
nums: list[int] = [int(num) for num in inp_array]
    
if __name__ == "__main__":
  solution=Solution()
  if solution.hasDuplicate(nums):
    print("The list has duplicates.")
  else:
    print("The list has no duplicates.")