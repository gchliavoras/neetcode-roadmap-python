class Solution:
#Longest Consecutive Sequence
#Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
#A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.
#You must write an algorithm that runs in O(n) time.
  def longestConsecutive(self, nums: list[int]) -> int:
    numsSet = set(nums) #for faster lookups
    longestSeq = 0
    seen = set()
    for num in nums:
      if num in seen:
        continue
      seen.add(num)
      i = 1
      while True:
       if num + i in numsSet:
         seen.add(num + i)
         i += 1
         continue
       break
      if i > longestSeq:
        longestSeq = i
    return longestSeq
Input = [1, 5, 6 ,7, 9, 2, 11, 10, 12, 4] 
if __name__ == "__main__":
  solution = Solution()
  print(solution.longestConsecutive(Input))