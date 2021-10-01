"""
related topic: string, dynamic programming
time complexity: O(len(text1) * len(text2))
space complexity: O(len(text1) * len(text2))

dp[i][j] = longest common subsequence of text1[0..j] and text2[0..i]

最後右下角即為答案

"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text1) + 1)] for __ in range(len(text2) + 1)]

        for i in range(len(text2)):
            for j in range(len(text1)):
                dp[i + 1][j + 1] = (
                    dp[i][j] + 1
                    if text2[i] == text1[j]
                    else max(dp[i][j + 1], dp[i + 1][j])
                )

        return dp[len(text2)][len(text1)]
