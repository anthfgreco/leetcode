# Bruteforce solution O(n^2)
"""
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
      for i in range(len(nums)):
          for j in range(len(nums)):
              if (nums[i]+nums[j] == target):
                  return [i, j]
"""
​
# Notes
"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Subtract 9 from nums = [-7,-2,2,6]
​
nums = [3,2,4]
target = 6
output = [1,2]
dict = {3:0, 2:1, 4:2}
target - nums[i] = [3,4,2]
Once second loop hits i=2, it will search for dict[2] and return indices 1 and 2
"""
​
# Linear Solution, two passes O(n)
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    dict = {}
    
    for i in range(len(nums)):
      dict[nums[i]] = i
    
    for i in range(len(nums)):
      diff = target - nums[i]
      if (diff in dict and dict[diff] != i):
        return [i, dict[diff]]
      
    
