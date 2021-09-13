"""
related topic: hashtable
time complexity: O(n)
space complexity: O(n)? 最差狀況應為最後一個才找到，因此會有一個擁有 n-1 個元素的 dict

題目要求須找出 target - {陣列中的其中一數} = {陣列中的另一數}，因此一邊遍歷 list，一邊用 hashtable 紀錄前述等式右邊的值。

若發現目前的值出現在 hashtable 的 key 中，也就是說，目前的值為等式左邊的值，即可透過 hashtable 得出右邊的值，並得出答案。
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookUpTable = {}

        for i in range(len(nums)):
            if target - nums[i] in lookUpTable:
                return [lookUpTable[target - nums[i]], i]

            lookUpTable[nums[i]] = i
