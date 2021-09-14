"""
related topic: two pointers
time complexity: O(n) 遍歷一次即可
space complexity: O(n) 額外構造出一個新的字串，與原本等長，可以改用原地交換優化為 O(1)

用兩個 index 分別從頭尾往另一側遍歷，左側負責檢查是否有不應被 reverse 的符號出現，右側負責檢查是否有需要跳過的符號。
"""


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        result = ""
        left, right = 0, len(s) - 1
        while left < len(s):
            if not s[left].isalpha():
                result += s[left]
                left += 1
            elif s[right].isalpha():
                result += s[right]
                right -= 1
                left += 1
            else:
                right -= 1
        return result
