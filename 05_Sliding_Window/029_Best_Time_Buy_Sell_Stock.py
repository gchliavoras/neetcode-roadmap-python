#Best Time to Buy and Sell Stock
#You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
#You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
#Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
class Solution:
  def maxProfit(self, prices: list[int]) -> int:
    minPrice = float("inf")
    maxProfit = 0
    
    for price in prices:
      minPrice = min(price, minPrice)
      maxProfit = max(price - minPrice, maxProfit)
    
    return maxProfit
        