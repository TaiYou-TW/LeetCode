"""
related topic: array, two pointer
time complexity: O(n)
space complexity: O(1)

此題要求用 in-place 的解法，因此用 k 來紀錄最後一個已移除指定元素的 array index，遇到正確的值時才將 k + 1，並將其放入。

"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for idx in range(0, len(nums)):
            if nums[idx] != val:
                nums[k] = nums[idx]
                k += 1
        return k
