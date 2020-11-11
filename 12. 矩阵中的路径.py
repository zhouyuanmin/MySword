"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。
如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。
例如，在下面的3×4的矩阵中包含一条字符串“abc”的路径（路径中的字母用加粗标出）。
[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]
但矩阵中不包含字符串“case”的路径。

来源：力扣
链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

提示：
1 <= board.length <= 200
1 <= board[i].length <= 200
"""

# 解法思路:回溯法
from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    def dfs(_i, _j, _k):
        if not 0 <= _i < len(board) or not 0 <= _j < len(board[0]) or board[_i][_j] != word[_k]:
            return False

        if _k == len(word) - 1:
            return True

        tmp, board[_i][_j] = board[_i][_j], '/'  # 标明已占领
        res = dfs(_i + 1, _j, _k + 1) or dfs(_i - 1, _j, _k + 1) or dfs(_i, _j + 1, _k + 1) or dfs(_i, _j - 1, _k + 1)
        board[_i][_j] = tmp  # 还原标明
        return res

    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, 0):
                return True
    return False
