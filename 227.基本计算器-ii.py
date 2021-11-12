#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#

# @lc code=start
class Solution:
    ZERO = ord('0')

    def calculate(self, s: str) -> int:
        """
        算法思路:
            1. 由于没有括号，不考虑表达式优先级
            2. 对于'+', '-'号之后的数字，入栈
            3. 对于'*', '/'号之后的数字，和栈顶元素进行运算
        Args:
            s(str): 输入的表达式

        Returns:
            int: 返回的表达式结果
        """
        stack = []
        num = 0
        sign = ''
        i = 0

        for i in range(len(s)):
            c = s[i]

            if c == ' ' and i < len(s) - 1:  # 除最后一个字符外，跳过空格
                continue

            if c.isdigit():  # 除最后一个字符外，保存数字并跳过
                num = (num * 10) + (ord(c) - self.ZERO)
                if i < len(s) - 1:
                    continue

            # 计算运算符
            if sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack[-1] *= num
            elif sign == '/':
                # 模拟 c 语言整除运算
                stack[-1] = - \
                    (-stack[-1] // num) if stack[-1] < 0 else stack[-1] // num
            else:
                stack.append(num)

            num = 0
            sign = c

        return sum(stack)
# @lc code=end
