'''
Two Sum
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first.
Constraints:
2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000
'''
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
      print(nums)
      sorted_nums=sorted(nums)
      print(sorted_nums)
      twoSum: int = 0
      i: int = 0
      while i < len(nums) - 1:
        for j in range(i+1,len(sorted_nums)):
          twoSum = sorted_nums[i] + sorted_nums[j]
          print(f"twoSum: {twoSum}, i: {i}, j: {j}")
          if twoSum == target:
            if sorted_nums[i] == sorted_nums[j]:
              a = nums.index(sorted_nums[i])
              nums[a] = "_"
              b = nums.index(sorted_nums[j])
              return [a,b]
            return sorted([nums.index(sorted_nums[i]),nums.index(sorted_nums[j])])
          if twoSum > target:
            break
        i += 1
nums = [2, 5, 234, 34, 46, 234, 12, 4, 6, 8, 4, 6, 5, 1, 8, 9, 10, 35, 37, 457, 345]
print(nums)
while True:
  try:
    target = int(input("What's the target"))
    break
  except:
    print("Input must be a number")
  
if __name__ == "__main__":
  solution = Solution()
  print(solution.twoSum(nums, target))