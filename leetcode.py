from typing import List

class Solution:
  
  def containsDuplicate(self, nums: List[int]) -> bool:
    """
    O(n) time complexity, one pass
    O(n) space, dictionary holds list of all elements
    1.  Algorithm iterates over all items in the list and adds them one-by-one
        to dictionary.
    2.  If item is already in dictionary, return True because there's a duplicate
    3.  If all items were looped through, return False because there's no duplicates
    Takes advantage of dictionary lookup being O(1)
    """
    dict = {}
    for n in nums:
      if n in dict:
        return True
      else:
        dict[n] = 1
    return False

  def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
    """
    Bruteforce solution O(n^2)

    Tries every combination of pairs
    """
    for i in range(len(nums)):
      for j in range(len(nums)):
        if (nums[i]+nums[j] == target):
          return [i, j]

  def twoSum(self, nums: List[int], target: int) -> List[int]:
    """
    Two pass solution, O(n) time complexity
    O(n) space complexity, dictionary holds all elements of list

    1.  Algorithm iterates over all #'s in nums and adds them to dictionary with
        the key = nums[i] and value = i
    2.  Subtracts target from every nums[i], 
          ex. [2,7,11,15] - 9 -> [-7, -2, 2, 6]
    3.  Iterates over nums again and searches the dictionary for nums[i] * -1
    """
    dict = {}

    for i in range(len(nums)):
      dict[nums[i]] = i
      nums[i] -= target
  
    for i in range(len(nums)):
      tmp = nums[i] * -1
      if (tmp in dict) and (dict[tmp] != i):
        return sorted([dict[tmp], i])

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






sol = Solution()
#print(  sol.containsDuplicate([1,2,3,4,5,6,2])     )
#print(  sol.twoSum([2,7,11,15], 9)                 )
#print(  sol.twoSum([3,2,4], 6)                     )
print(  sol.maxProfit([7,1,5,3,6,4])    )

