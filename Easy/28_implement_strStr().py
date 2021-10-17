"""
related topic: two pointers, string, string matching
time complexity: O(n)
space complexity: O(1)

"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        for i in range(len(haystack)):
            if haystack[i : i + len(needle)] == needle:
                return i

        return -1
