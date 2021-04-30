"""
O(n) time complexity, one pass
O(n) space, dictionary holds list of all elements

1.  Algorithm iterates over all items in the list and adds them one-by-one
    to dictionary.
2.  If item is already in dictionary, return True because there's a duplicate
3.  If all items were looped through, return False because there's no duplicates

Takes advantage of dictionary lookup being O(1)
"""

class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    dict = {}
    for n in nums:
      if n in dict:
        return True
      else:
        dict[n] = 1
    return False
        