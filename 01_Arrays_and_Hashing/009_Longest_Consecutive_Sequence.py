class Solution:
#Longest Consecutive Sequence
#Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
#A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.
#You must write an algorithm that runs in O(n) time.
  def longestConsecutive(self, nums: list[int]) -> int:
    numsSet = set(nums) #for easier lookups
    consecutiveSeqs = [[] for _ in range(len(nums))]
    for num in nums:
      i = 1
      consecutiveSeq = [num]
      while True:
       if num + i in numsSet:
         consecutiveSeq.append(num + i)
         i += 1
         continue
       break
      consecutiveSeqs[i-1].append(consecutiveSeq)
    Output = [list for list in consecutiveSeqs if list != []]
    return len(Output)
Input = [1, 5, 6 ,7, 9, 2, 11, 10, 12, 4] 
if __name__ == "__main__":
  solution = Solution()
  print(solution.longestConsecutive(Input))