class Solution:
#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
#The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
#You should aim for a solution with O(n^2) time and O(1) space, where n is the size of the input array.
  def threeSum(self, nums: list[int]) -> list[list[int]]:
    Output = []
    nums.sort()
    n = len(nums)
    for i, num1 in enumerate(nums): #Iterate through nums, and running an exhaustive twoSum algorithm for the remaining elements of the list.
      nums_temp = nums[:i] + nums[i+1:]
      target_temp = -num1
      left, right = 0, n - 2 #twoSum algorithm. n - 2 = (n - 1) - 1 because the algorithm runs on the nums_temp list, with length n-1
      while left < right:
        twoSum = nums_temp[left] + nums_temp[right]
        if twoSum == target_temp:
          current_triplet = sorted([num1, nums_temp[left], nums_temp[right]])
          if current_triplet not in Output:
            Output.append(current_triplet)
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
      