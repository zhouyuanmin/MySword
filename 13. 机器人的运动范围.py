"""
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，
它每次可以向左、右、上、下移动一格（不能移动到方格外），
也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。
但它不能进入方格 [35, 38]，因为3+5+3+8=19。
请问该机器人能够到达多少个格子？

示例 1：
输入：m = 2, n = 3, k = 1
输出：3

示例 2：
输入：m = 3, n = 1, k = 0
输出：1

提示：
1 <= n,m <= 100
0 <= k <= 20

来源：力扣
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import Set, Tuple


def moving_count(self, m: int, n: int, k: int) -> int:
    points: Set = set()

    def count_point(point: Tuple[int, int]):
        count = 0
        i, j = point
        while i:
            count += i % 10
            i = i // 10
        while j:
            count += j % 10
            j = j // 10
        if count <= k:
            return True
        else:
            return False

    def get_points(point: Tuple[int, int]) -> None:
        i, j = point
        if not (0 <= i < m and 0 <= j < n):
            return None
        if count_point(point):
            if point in points:
                return None
            points.add(point)
            get_points(point=(i + 1, j))
            get_points(point=(i, j + 1))
        return None

    get_points(point=(0, 0))

    return len(points)
