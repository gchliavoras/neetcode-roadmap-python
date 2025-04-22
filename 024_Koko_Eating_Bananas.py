import math
class Solution:
#You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.
#You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.
#Return the minimum integer k such that you can eat all the bananas within h hours.
  def minEatingSpeed(self, piles: list[int], h: int) -> int:
    def totalTime(k: int) -> int:
      time = 0
      for pile in piles:
        time += math.ceil(pile / k)
        
      return time    
    
    if h < len(piles):
      return -1
      
    elif h == len(piles):
      return max(piles)
      
    left, right = 1, max(piles)
    while left < right:
      mid = left + (right - left) // 2
      midTime = totalTime(mid)
      
      if midTime <= h:
        right = mid
        
      else:
        left = mid + 1
        
    return right
      
piles = [1,4,3,2]
h = 9

if __name__ == "__main__":
  solution = Solution()
  print(solution.minEatingSpeed(piles, h))