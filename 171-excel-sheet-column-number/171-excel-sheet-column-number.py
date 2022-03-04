class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        output = 0
        power = 0
        for letter in reversed(columnTitle):
            output += (alpha.index(letter) + 1) * 26**power
            power += 1
        return output

# Problem is essentially converting base 26 to base 10
# "A"  (1 * 26**0) = 1
# "AB" (2 * 26**0) + (1 * 26**1) = 2 + 26 = 28
# "ZY" (25 * 26**0) + (26 * 26**1) = 701
        