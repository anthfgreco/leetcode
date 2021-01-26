# O(n) time, one pass
# O(n) space, dictionary
class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    dict = {}
    for n in nums:
      if n in dict:
        return True
      else:
        dict[n] = 1
    return False
        
