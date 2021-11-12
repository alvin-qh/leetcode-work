#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#
from functools import lru_cache

# @lc code=start
class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        """
        算法思路:
            该算法需要解决 '*' 和多少个字符匹配的问题，例如：
            s = aac
            p = a*ac
            则 aa 可以匹配 a* 和 a*a，且后者才能完成正确的匹配

            所以需要用动态规划方式尝试所有匹配情况，并找到最恰当的一组匹配

        Args:
            s(str): 输入的字符串
            p(str): 要匹配的模式字符串

        Returns:
            bool: 输入字符串是否匹配模式
        """
        cache = {}

        @lru_cache  # with cache enable
        def is_match(sn: int, pn: int) -> bool:
            if pn == len(p):
                return sn == len(s)

            key = (sn, pn)

            if key in cache:
                return cache[key]

            first_match = False
            if sn < len(s):
                first_match = p[pn] in {s[sn], '.'}

            if pn + 1 < len(p) and p[pn + 1] == '*':
                # 如果模式包含 '*' 后缀，则递归遍历如下两种情况
                # 1. 当前模式匹配 0 个字符，则从下一个模式继续匹配
                # 2. 当前模式匹配到字符，且看是否能匹配后续重复字符
                r = is_match(sn, pn + 2) or (first_match and is_match(sn + 1, pn))
                cache[key] = r
                return r

            # 匹配下一个模式和字符
            r = first_match and is_match(sn + 1, pn + 1)
            cache[key] = r
            return r

        return is_match(0, 0)
# @lc code=end

