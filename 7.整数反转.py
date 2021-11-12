#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:

    def reverse(self, x: int) -> int:
        """
        Args:
            x(int): 输入的整数值

        Returns:
            int: 翻转后的整数值
        """
        MAX = 2147483648
        sig = 1 if x >= 0 else -1
        x = abs(x)

        res = 0
        while x != 0:
            res = res * 10 + x % 10
            x //= 10
            if (sig > 0 and res > MAX - 1) or (sig < 0 and res > MAX):
                return 0

        return res * sig
# @lc code=end
