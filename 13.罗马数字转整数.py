#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:

    def romanToInt(self, s: str) -> int:
        """
        算法说明：
            该算法相当于 12 题的逆运算
            从所给罗马数字中，依次截取：
            1. 两个字符，查找该两个字符表示的阿拉伯数字
            2. 如 1 未找到，则截取一个字符，查找该字符表示的阿拉伯数字
            将每步所得的阿拉伯数字相加，即得到最终结果

        Args:
            s(str): 输入的罗马数字

        Returns:
            int: 转化后的整数
        """
        roma_nums = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }
        res = 0
        n = 0
        while n < len(s):
            ps = s[n:n+2]
            if len(ps) == 2 and ps in roma_nums:
                res += roma_nums[ps]
                n += 2
            else:
                ps = s[n]
                res += roma_nums[ps]
                n += 1

        return res
# @lc code=end
