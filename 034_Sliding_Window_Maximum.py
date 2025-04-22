#Sliding Window Maximum
#You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.
#Return a list that contains the maximum element in the window at each step.
class Solution:
  def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
    #Initialize variables.
    start, end = 0, 0
    res, deque = [], []
    #Start moving sliding window.
    while end < len(nums):
      #Pop elements in deque that are smaller then the new number.
      while deque and nums[end] > deque[-1]:
        deque.pop()
      #Add new number to deque.
      deque.append(nums[end])
      #Move start pointer to shrink window back to the correct size.
      if end - start == k - 1:
        #Update result array.
        res.append(deque[0])
        #Remove out-of-range element, if still in deque...
        if deque[0] == nums[start]:
          deque.pop(0)
        #...and advance start pointer.
        start += 1
      #Advance end pointer and restart loop.
      end += 1
    #Return filled result array.
    return res

nums = [1,2,1,0,4,2,6]
k = 3

if __name__ == "__main__":
  solution = Solution()
  print(solution.maxSlidingWindow(nums, k))