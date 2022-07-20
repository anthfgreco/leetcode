class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealths = []
        for account in accounts:
            wealths.append(sum(account))
        return max(wealths)
        