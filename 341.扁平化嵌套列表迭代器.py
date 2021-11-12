#
# @lc app=leetcode.cn id=341 lang=python3
#
# [341] 扁平化嵌套列表迭代器
#
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
from typing import List, Union


class NestedInteger:
    """
    定义可嵌套整数类型。（题目中无需定义）
    """

    def __init__(self, n: Union[int, List["NestedInteger"]]):
        self._n = n
        self._is_int = isinstance(n, int)  # 根据类型设置是否整数

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return self._is_int

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        return self._n if self._is_int else None

    def getList(self) -> List["NestedInteger"]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        return self._n if not self._is_int else None


# @lc code=start
class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        """
        初始化迭代器
        算法结束后，所有嵌套的元素均被平铺开，逆序存放在 self._list 列表中
        """
        nested_list = nestedList[:]
        self._list = []

        while len(nested_list) > 0:  # 将 nested_list 看作为栈结构，开始深度优先遍历
            n = nested_list.pop()  # 出栈
            if n.isInteger():  # 判断出栈元素是否为整数，如果是整数，则加入到结果列表中，否则将其内容全部压栈
                self._list.append(n)
            else:
                nested_list += n.getList()

    def next(self) -> int:
        n = self._list.pop()
        return n

    def hasNext(self) -> bool:
        return len(self._list) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end
