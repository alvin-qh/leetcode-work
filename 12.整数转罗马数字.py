#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:

    def intToRoman(self, num: int) -> str:
        """
        算法思路：
            从大到小列举所有已知罗马数字
            求所给数字和罗马数字的倍数关系，从而计算罗马数字的转换规则
            余数进入下次迭代，例如：

            58
                58 // 1000 = 0
                58 //  900 = 0
                58 //  500 = 0
                58 //  100 = 0
                58 //   90 = 0
                58 //   50 = 1 => L,   余 8
                8 //   40 = 0
                8 //   10 = 0
                8 //    9 = 0
                8 //    5 = 1 => V,   余 3
                3 //    4 = 0
                3 //    1 = 3 => III, 余 0

            1994
                1994 // 1000 = 1 => M， 余 994
                994 //  900 = 1 => CM，余 94
                94 //  500 = 0
                94 //  100 = 0
                94 //   90 = 1 => XC，余 4
                4 //   50 = 0
                4 //   40 = 0
                4 //   10 = 0
                4 //    9 = 0
                4 //    5 = 0
                4 //    4 = 1 => IV, 余 0

        Args:
            num(int): 输入的整数

        Returns:
            str: 罗马数字
        """
        roma_nums = [
            (1000, 'M'), (900, 'CM'),
            (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'),
            (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'),
            (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        res = []

        for n, rn in roma_nums:
            c = num // n
            for _ in range(0, c):
                res.append(rn)
            num %= n

        return ''.join(res)
# @lc code=end
