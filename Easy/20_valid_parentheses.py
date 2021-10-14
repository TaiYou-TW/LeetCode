"""
related topic: string, stack
time complexity: O(n)
space complexity: O(n)

遇到「開」符號就放入 stack，而遇到「閉」符號就檢查 stack 頂端的符號是否相符，不符或是 stack 為空皆為 False。

另外若結束時，stack 還留有剩下的符號時，也是 False。

"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            elif (
                (char == ")" and (len(stack) == 0 or stack.pop() != "("))
                or (char == "]" and (len(stack) == 0 or stack.pop() != "["))
                or (char == "}" and (len(stack) == 0 or stack.pop() != "{"))
            ):
                return False
        return len(stack) == 0
