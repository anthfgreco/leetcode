# Brute force (n^2)
"""
class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    maxProfit = 0
    for i in range(len(prices) - 1):
      for j in range(i+1, len(prices)):
        profit = prices[j] - prices[i]
        if (profit > maxProfit):
          maxProfit = profit
    return maxProfit
"""
​
# Linear solution
# O(n) time, one pass used
# O(1) space, two variables used
class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    maxProfit = 0
    minPrice = 10**6
    
    for i in range(len(prices)):
      if (prices[i] < minPrice):
        minPrice = prices[i]
      elif (prices[i] - minPrice > maxProfit):
        maxProfit = prices[i] - minPrice
        
    return maxProfit
