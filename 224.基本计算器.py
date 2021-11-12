#
# @lc app=leetcode.cn id=224 lang=python3
#
# [224] 基本计算器
#


# @lc code=start
class Solution:
    ZERO = ord('0')

    def calculate(self, s: str) -> int:
        """
        算法思路:
            1. 由于只有'+', '-'号，所以无需考虑运算符优先级
            2. 对于'()'内的结果，可以通过结合律将括号系数算入括号内，以消除括号优先级，例如 1 - (1 + 2 - 3) => 1 - 1 - 2 + 3

        Args:
            s(str): 输入的表达式

        Returns:
            int: 返回的表达式结果
        """
        res = 0

        sign = 1  # 初始化符号
        opts = [1]  # 初始化栈顶元素

        i = 0
        while i < len(s):
            c = s[i]
            if c == ' ':  # 跳过空格
                i += 1
            elif c == '+':
                sign = opts[-1]  # 若 '(' 前为 '+' 号，则括号中所有符号不变
                i += 1
            elif c == '-':
                sign = -opts[-1]  # 若 '(' 前为 '-' 号，则括号中所有符号取反
                i += 1
            elif c == '(':
                opts.append(sign)  # 把括号前的符号入栈
                i += 1
            elif c == ')':  # 把括号前的符号出栈
                opts.pop()
                i += 1
            else:
                # 计算一组数字和前一个符号的结果
                n = 0
                while i < len(s) and s[i].isdigit():
                    n = n * 10 + (ord(s[i]) - self.ZERO)
                    i += 1

                # 计算和
                res += sign * n
        return res
# @lc code=end
