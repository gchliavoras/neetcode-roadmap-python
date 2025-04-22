class Solution:
#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
#The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
#You should aim for a solution with O(n^2) time and O(1) space, where n is the size of the input array.
  def threeSum(self, nums: list[int]) -> list[list[int]]:
    output = []
    nums.sort()
    #Iterate through nums, run an exhaustive twoSum algorithm for the remaining elements of the list.
    for i in range(len(nums)):
      if i > 0 and nums[i] == nums[i-1]: #Skip duplicates from the first element of each triplet.
        continue
#Exhaustive twoSum algorithm
      target_i = -nums[i]
      left, right = i + 1, len(nums) - 1 #Two pointers setup 
      while left < right:
        twoSum = nums[left] + nums[right]
        if twoSum == target_i:
          output.append([nums[i], nums[left], nums[right]])
          #Duplicate checks
          while left < right and nums[left] == nums[left+1]: #Skip duplicates from the second element of each triplet.
            left += 1
          while left < right and nums[right] == nums[right-1]: #Skip duplicates from the third element of each triplet.
            right -= 1
          #Advance two pointers following valid triplet
          left += 1 
          right -= 1
          
        elif twoSum > target_i:
          right -= 1
        else:
          left += 1        

    return output

nums = [0,0,0,0,0]
if __name__ == "__main__":
  solution = Solution()
  print(solution.threeSum(nums))
      