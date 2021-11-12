#
# @lc app=leetcode.cn id=395 lang=python3
#
# [395] 至少有 K 个重复字符的最长子串
#
from test.test_threading import Counter


# @lc code=start
class Solution:
    A = ord('a')

    def longestSubstring(self, s: str, k: int) -> int:
        """
        Args:
            s(str): 输入的字符串
            k(int): 期望的最小字符出现次数

        Returns:
            int: 符合条件的字符串长度
        """
        if len(s) < k:
            return 0

        def _dfs(l, r):
            fraq = Counter()
            for i in range(l, r + 1):
                fraq[ord(s[i]) - self.A] += 1

            split = ''
            for i in range(0, 26):
                if fraq[i] > 0 and fraq[i] < k:
                    split = chr(i + self.A)
                    break

            if split == '':
                return r - l + 1

            i = l
            res = 0
            while i <= r:
                while i <= r and s[i] == split:
                    i += 1

                if i > r:
                    break

                start = i
                while i <= r and s[i] != split:
                    i += 1

                length = _dfs(start, i - 1)
                res = max((res, length))

            return res

        return _dfs(0, len(s) - 1)
# @lc code=end

# 解法 2
# class Solution:
#
#     def longestSubstring(self, s: str, k: int) -> int:
#         """
#         Args:
#             s(str): 输入的字符串
#             k(int): 期望的最小字符出现次数
#
#         Returns:
#             int: 符合条件的字符串长度
#         """
#         if len(s) < k:
#             return 0
#
#         def _dfs(_s):
#             """
#             分治算法，分段计算
#             """
#             for c in set(_s):  # 遍历字符串中不重复的每个字符
#                 if _s.count(c) < k:
#                     return max(_dfs(t) for t in _s.split(c))
#
#             return len(_s)
#
#         return _dfs(s)
