"""
related topic: hashtable
time complexity: O(n)
space complexity: O(1)

計算全部的字母數量，最少的字母數量（注意：`l` 及 `o` 各重複兩次）即為可組成的 `balloon` 數量。
"""


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        str_list = {"a": 0, "b": 0, "l": 0, "n": 0, "o": 0}

        for char in text:
            if char in str_list:
                str_list[char] += 1

        str_list["l"] //= 2
        str_list["o"] //= 2

        return str_list[min(str_list, key=str_list.get)]
