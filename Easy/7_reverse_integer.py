"""
related topic: math
time complexity: O(n) n 為數字轉成字串後的長度
space complexity: O(1) 

先構造出一個原本的數字 reversed 後的新字串，接著判斷是否超出邊界

"""


class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        result = "-" if s[0] == "-" else ""
        index = len(s) - 1
        while s[index] == "0" and index != 0:
            index -= 1
        while index >= 0:
            if s[index] != "-":
                result += s[index]
            index -= 1
        if self.is_invalid(
            result[1:] if result[0] == "-" else result,
            True if result[0] == "-" else False,
        ):
            return 0
        return int(result)

    def is_invalid(self, x: str, negetive: bool) -> bool:
        border = "2147483648" if negetive else "2147483647"
        if len(x) < 10:
            return False
        for i in range(len(border)):
            if border[i] < x[i]:
                return True
            elif border[i] > x[i]:
                return False
        return False
