"""
related topic: array, two pointer
time complexity: O(n)
space complexity: O(1)

此題要求用 in-place 的解法，因此用 k 來紀錄最後一個已移除重複元素的 array index，遇到不重複的值時才將 k + 1，並將其放入。

"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for idx in range(1, len(nums)):
            if nums[k] != nums[idx]:
                k += 1
                nums[k] = nums[idx]
        return k + 1
