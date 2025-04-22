class Solution:
#Products of Array Except Self
#Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
#Each product is guaranteed to fit in a 32-bit integer.
# O(n) time without using the division operation?
  def productExceptSelf(self, nums: list[int]) -> list[int]:
    n = len(nums)
    res: list[int] = [1] * n
    prefix: list[int] = [1] * n
    suffix: list[int] = [1] * n
    
    for i in range(1, n):
      prefix[i] = nums[i-1] * prefix[i-1]
      res[i] = prefix[i]

    for i in range(2, n+1):
      suffix[-i] = nums[-(i-1)] * suffix[-(i-1)]
      res[-i] *= suffix[-i] 
    print(prefix)
    print(suffix)
    return res

Input = [-1,0,1,2,3]
if __name__ == "__main__":
  solution = Solution()
  print(solution.productExceptSelf(Input))