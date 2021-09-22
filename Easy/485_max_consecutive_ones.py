"""
related topic: array
time complexity: O(n)
space complexity: O(1)

遍歷 array，用一個 counter 計算目前連續的 1 的長度，並紀錄下目前最大之數。

"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max, counter = 0, 0
        for ele in nums:
            if ele == 1:
                counter += 1
            else:
                if counter > max:
                    max = counter
                counter = 0
        if counter > max:
            max = counter
        return max
