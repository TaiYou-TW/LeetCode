"""
related topic: math
time complexity: O(1)
space complexity: O(1)

如果將數字轉成字串一行就可以解決，但是 Follow Up 不希望用此方法解題，因此先計算出 x 的長度，再利用此資訊去對照前半與後半是否一樣。

"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x_length = 0
        for i in range(9, -1, -1):
            if x // (10 ** i) > 0:
                x_length = i + 1
                break

        for i in range(0, x_length // 2 + 1):
            reversed_exp = x_length - i - 1
            if (x % (10 ** (i + 1)) // (10 ** i)) != (
                x % (10 ** (reversed_exp + 1)) // (10 ** reversed_exp)
            ):
                return False
        return True
