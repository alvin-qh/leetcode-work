#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:

    def isPalindrome(self, x: int) -> bool:
        """
        Args:
            n(int): 输入的整数

        Returns:
            bool: 输入整数是否为回文数
        """
        if x < 0:
            return False

        return str(x) == str(x)[::-1]
# @lc code=end

# 另一种解法
# class Solution:
# 
#     def isPalindrome(self, x: int) -> bool:
#         """
#         Args:
#             n(int): 输入的整数
# 
#         Returns:
#             bool: 输入整数是否为回文数
#         """
#         if x < 0:
#             return False
# 
#         sn, pn = x, 0
#         while x != 0:
#             pn = pn * 10 + (x % 10)
#             x //= 10
# 
#         return sn == pn
