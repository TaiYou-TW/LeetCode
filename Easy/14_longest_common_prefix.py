"""
related topic: string
time complexity: O(len(strs[0]) * len(strs))
space complexity: O(1)

遍歷 strs[0]，並同時去找當前的字元是否與後面每一個皆相符，若不符即可返回結果，反之則再確認下一個字元。

"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for idx, char in enumerate(strs[0]):
            for i in range(len(strs)):
                if len(strs[i]) <= idx or strs[i][idx] != char:
                    return strs[0][:idx]

        return strs[0]
