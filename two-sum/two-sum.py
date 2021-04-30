class Solution:
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
      
    