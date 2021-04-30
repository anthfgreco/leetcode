class Solution:
  def maxSubArrayBruteForce(self, nums: List[int]) -> int:
    """
    Bruteforce solution, O(n^2) time complexity

    Tries every permutation of subarrays
    """
    maxSum = 0

    # Get sum of all subarray permutations
    for i in range(len(nums)):
      for j in range(i, len(nums)):
        tmpsum = sum(nums[i:j])
        if tmpsum > maxSum:
          maxSum = tmpsum
    
    return maxSum

  def maxSubArray(self, nums: List[int]) -> int:
    """
    O(n) time complexity
    Kadane's Algorithm
    """
    for i in range(1, len(nums)):
      if nums[i-1] > 0:
        nums[i] += nums[i-1]
   
    return max(nums)
    
        