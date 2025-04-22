class Solution:
#Products of Array Except Self
#Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
#Each product is guaranteed to fit in a 32-bit integer.
# O(n) time without using the division operation?
  def productExceptSelf(self, nums: list[int]) -> list[int]:
    n = len(nums)
    res: list[int] = [1] * n
    prefix = 1
    for i in range(n): #Prefix
      res[i] = prefix
      prefix *= nums[i]
    suffix = 1
    for i in range(1, n+1): #Suffix
      res[-i] *= suffix
      suffix *= nums[-i]
    return res

Input = [1,2,3,4]
if __name__ == "__main__":
  solution = Solution()
  print(solution.productExceptSelf(Input))