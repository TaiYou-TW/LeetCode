"""
related topic: linked list
time complexity: O(n)
space complexity: O(n)

1. 計算出 linked list 長度
2. 填入長度為 k + 1 的 linked list
3. 填入長度為 k 的 linked list

"""


class Solution:
    def getLength(self, head: Optional[ListNode]) -> int:
        length = 0
        ptr = head
        while ptr != None:
            ptr = ptr.next
            length += 1
        return length

    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        result = []

        length = self.getLength(head)

        ptr = head
        for i in range(length % k):
            result.append(ptr)
            for j in range(length // k):
                ptr = ptr.next
            next = ptr.next
            ptr.next = None
            ptr = next
        for i in range(k - length % k):
            result.append(ptr)
            for j in range(length // k - 1):
                ptr = ptr.next
            if ptr != None:
                next = ptr.next
                ptr.next = None
                ptr = next

        return result
