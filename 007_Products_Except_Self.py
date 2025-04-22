class Solution:
#Products of Array Except Self
#Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
#Each product is guaranteed to fit in a 32-bit integer.
# O(n) time without using the division operation?
  def productsExceptSelf(self, nums: list[int]) -> list[int]:
    res: list[int] = [[] for _ in nums]
    asc_prods: list[int] = [[] for _ in nums]
    desc_prods: list[int] = [[] for _ in nums]
    asc_prods[0] = nums[0]
    desc_prods[0] = nums [-1]
    for i in range(1, len(nums)):
      asc_prods[i] = asc_prods[i-1] * nums[i]
      desc_prods[i] = desc_prods[i-1] * nums[-1 - i]
    for i in range(1, len(nums) - 1):
      res[i] = asc_prods[i-1] * desc_prods[-2 - i]
    res[0] = desc_prods[-2]
    res[-1] = asc_prods[-2]
    return res

Input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if __name__ == "__main__":
  solution = Solution()
  print(solution.productsExceptSelf(Input))