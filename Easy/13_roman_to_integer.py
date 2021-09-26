"""
related topic: hash table, math, array
time complexity: O(n)
space complexity: O(1)

一次檢查兩個符號，如果後方大於前方代表要加（後減前），不是的話就直接加

"""


class Solution:
    symbol_table = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def romanToInt(self, s: str) -> int:
        sum = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and self.symbol_table[s[i + 1]] > self.symbol_table[s[i]]:
                sum += self.symbol_table[s[i + 1]] - self.symbol_table[s[i]]
                i += 2
            else:
                sum += self.symbol_table[s[i]]
                i += 1
        return sum
