#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
from typing import List


# cspell: ignore pqrs wxyz
# @lc code=start
class Solution:

    def __init__(self):
        self._pad = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

    def letterCombinations(self, digits: str) -> List[str]:
        """
        算法说明：
            利用回溯法（backtracking method），每轮迭代后，回溯到前一个状态，用于穷举所有状态
            相当于在一棵树上，每到到达最后一个叶子或穷举完所有的叶子，则回溯到上一个节点继续进行

        Args:
            digits(str): 输入的号码

        Returns:
            List[str]: 返回的字母组合集合
        """
        res = []
        comb = []

        def _cal(i):
            if i == len(digits):
                if len(comb) > 0:  # 一条支线的情况枚举完成，保存 comb 集合中的结果并结束
                    res.append(''.join(comb))
                return

            # 穷举该号码表示的所有字母
            for c in self._pad[digits[i]]:
                comb.append(c)  # 字母添加到 comb 集合中
                _cal(i + 1)  # 处理下一个号码
                comb.pop()  # 下一个号码处理完毕，回溯到 c 未添加的状态，处理下一个字母

        _cal(0)
        return res
# @lc code=end
