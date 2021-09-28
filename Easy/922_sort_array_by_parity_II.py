"""
related topic: array, hash table, sorting
time complexity: O(n)
space complexity: O(n)

紀錄最後一個奇數以及偶數的位置，並且在遍歷 array 的同時，一邊將對應的數字放入新的陣列的正確位置。

"""


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        next_even_index, next_odd_index = 0, 1
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                result[next_odd_index] = nums[i]
                next_odd_index += 2
            else:
                result[next_even_index] = nums[i]
                next_even_index += 2
        return result
