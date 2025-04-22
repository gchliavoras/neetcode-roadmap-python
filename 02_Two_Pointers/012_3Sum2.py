class Solution:
#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
#The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
#You should aim for a solution with O(n^2) time and O(1) space, where n is the size of the input array.
  def threeSum(self, nums: list[int]) -> list[list[int]]:
    Output = []
    nums.sort()
    nums_seen = []
    for i, num1 in enumerate(nums): #Iterate through nums, and running an exhaustive twoSum algorithm for the remaining elements of the list.
      if num1 in nums_seen: #Skip duplicate checks. Target_temp was previous -num1.
        continue
      nums_seen.append(num1)
      nums_temp = nums[i+1:]
      target_temp = -num1
      left, right = 0, len(nums_temp) - 1 #Exhaustive twoSum algorithm. 
      seen_temp = []
      while left < right:
        twoSum = nums_temp[left] + nums_temp[right]
        if twoSum == target_temp:
          if nums_temp[left] not in seen_temp:
            Output.append([num1, nums_temp[left], nums_temp[right]])
            seen_temp.append(nums_temp[left])
          left += 1
          right += -1
        elif twoSum > target_temp:
          right += -1
        else:
          left += 1        
    return Output
nums = [_ - 5 for _ in range(11)]
if __name__ == "__main__":
  solution = Solution()
  print(solution.threeSum(nums))
      