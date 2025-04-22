#Find the Duplicate Number
#You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.
#Every integer appears exactly once, except for one integer which appears two or more times. Return the integer that appears more than once.
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
      seen = [0] * (len(nums) - 1)
      for num in nums:
        if seen[num - 1] == 1:
          return num
        else:
          seen[num - 1] = 1
          
nums = [1, 2, 3, 4, 3]

if __name__ == "__main__":
  sol = Solution()
  print(sol.findDuplicate(nums))
