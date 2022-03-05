class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = "IVXLCDM"
        values  = [1, 5, 10, 50, 100, 500, 1000]
        sum = 0
        old_i = len(values)
        
        for c in s:
            i = symbols.index(c)
            val = values[i]
            sum += val
            if old_i < i:
                sum -= 2*values[old_i]
            old_i = i
            
        return sum
    
# O(n)
# Algorithm adds value of roman symbol to sum
#
# For IV and special cases, it adds 1 + 5 = 6, and then subtracts two times the first value
# IV = 1 + 5 - 2(1) = 4