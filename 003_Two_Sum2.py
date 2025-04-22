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
      seen = {}
      for i in range(0,len(nums)-1):
        seen[i] = nums[i]
        offset = target - nums[i+1]
        for index, val in seen.items(): #Hashtable lookup
          if val == offset:
            return [index, i+1]
      print("No such combination.")

nums = [2, 5, 234, 34, 46, 234, 12, 4, 6, 8, 4, 6, 5, 1, 8, 9, 10, 35, 37, 457, 345]
print(nums)

while True:
  try:
    target = int(input("What's the target? \n"))
    break
  except:
    print("Input must be a number")
  
if __name__ == "__main__":
  solution = Solution()
  print(solution.twoSum(nums, target))