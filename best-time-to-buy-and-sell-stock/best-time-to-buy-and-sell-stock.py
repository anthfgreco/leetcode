
class Solution:
  def maxProfitBruteForce(self, prices: List[int]) -> int:
    """
    Bruteforce solution O(n^2)

    Tries every combination of pairs
    """
    maxProfit = 0
    for i in range(len(prices) - 1):
      for j in range(i+1, len(prices)):
        profit = prices[j] - prices[i]
        if (profit > maxProfit):
          maxProfit = profit
    return maxProfit

  def maxProfit(self, prices: List[int]) -> int:
    """
    O(n) time complexity, one pass
    O(1) space complexity, only two variables used

    1.  Set minimum price to maximum int and max profit to 0
    2.  Iterate through prices
        a. Update minimum price if old minimum price is greater
        b. Update max profit if old max profit is lower
    3. Return max profit
    """
    minPrice = 10**10   # or set to max size of int
    maxProfit = 0

    for i in range(len(prices)):
      if prices[i] < minPrice:
        minPrice = prices[i]
      elif (prices[i] - minPrice > maxProfit):
        maxProfit = prices[i] - minPrice

    return maxProfit