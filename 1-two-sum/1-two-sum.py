class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        [2,7,11,15], target = 9
        list - target
        dictionary = [-7, -5, 2, 6]
        At i=1 (7) we want to search the dictionary for -7 which will return the correct answer.
        
        [3,2,4], target = 6
        list - target
        dictionary = [-3,-4,-2]
        At i=1 (7) we want to search the dictionary for -7 which will return the correct answer.
        
        Subtract target from nums
        Create dictionary where nums-target -> index
        Search dictionary for num*-1, if found, return both indices
        """
        d = {}

        for i, num in enumerate(nums):
            # Covers [X, X] case
            if num-target not in d:
                d[num-target] = i
            if num*-1 in d and i != d[num*-1]:
                return sorted([i, d[num*-1]])
        