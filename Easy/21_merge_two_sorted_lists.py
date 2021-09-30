"""
related topic: linked list, recursion
time complexity: O(len(l1) + len(l2) = n)
space complexity: O(len(l1) + len(l2) = n)

用兩個 pointer 遍歷 list，並將較小的接在 prev 後面。

"""


class Solution:
    def mergeTwoLists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        ptr1, ptr2 = l1, l2
        head = ListNode()
        prev = head

        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                prev.next = ptr1
                prev = ptr1
                ptr1 = ptr1.next
            else:
                prev.next = ptr2
                prev = ptr2
                ptr2 = ptr2.next

        # directly append last list to list's end
        if ptr1:
            prev.next = ptr1
        if ptr2:
            prev.next = ptr2

        return head.next
