class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = [2,7,11,15], target = 9
        # nums - target = [-7, -2, 2, 6]
        d = {}
        for i, num in enumerate(nums):
            if -1*num in d:
                return [d[-1*num], i]
            d[num - target] = i
            