#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:

    def myAtoi(self, s: str) -> int:
        """
        Args:
            s(str): 输入的字符串

        Returns:
            int: 输入字符串转换成的整数
        """
        MAX = 2147483648
        res, sta, sig = 0, False, 1

        for c in s:
            n = 9 - (57 - ord(c))
            if n < 0 or n > 9:
                if res > 0:
                    break
                elif c == ' ' and not sta:
                    continue
                elif c in {'-', '+'} and not sta:
                    sig = -1 if c == '-' else 1
                else:
                    return 0
            else:
                res = res * 10 + n

                if sig > 0 and res > MAX - 1:
                    res = MAX - 1
                    break
                elif sig < 0 and res > MAX:
                    res = MAX
                    break

            sta = True

        return res * sig
# @lc code=end

