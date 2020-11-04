"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组[3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。

来源：力扣
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

示例 1：
输入：[3,4,5,1,2]
输出：1

示例 2：
输入：[2,2,2,0,1]
输出：0
"""
from typing import List


def min_array(self, numbers: List[int]) -> int:
    while True:
        if numbers[0] < numbers[-1]:
            return numbers[0]
        if len(numbers) <= 3 or numbers[0] == numbers[-1]:
            return min(numbers)

        numbers = numbers
        index = len(numbers) // 2 - 1
        if numbers[0] < numbers[index]:
            numbers = numbers[index + 1:]
        elif numbers[0] == numbers[index]:
            for i in numbers[0:index]:
                if numbers[0] > i:
                    return i
            numbers = numbers[index + 1:]
        else:
            numbers = numbers[0:index + 1]
