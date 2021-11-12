#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:

    def convert(self, s: str, numRows: int) -> str:
        """
        Args:
            s(str): 输入的字符串
            rows(int): 转换后的行数

        Returns:
            str: 转换后的字符串
        """
        if numRows == 1:
            return s

        result = []
        n, cycle_len = len(s), 2 * numRows - 2

        for i in range(numRows):
            j = 0

            while j + i < n:
                result.append(s[j + i])
                if i != 0 and i != numRows - 1 and j + cycle_len - i < n:
                    result.append(s[j + cycle_len - i])
                j += cycle_len

        return ''.join(result)
# @lc code=end
