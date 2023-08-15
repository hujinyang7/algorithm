'''
两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。
给你两个整数 x 和 y，计算并返回它们之间的汉明距离。
示例 1：
输入：x = 1, y = 4
输出：2
解释：
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
上面的箭头指出了对应二进制位不同的位置。

示例 2：
输入：x = 3, y = 1
输出：1
'''


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bin_num_x = bin(x)[2:]
        bin_num_y = bin(y)[2:]
        length_x = len(bin_num_x)
        length_y = len(bin_num_y)
        if length_x != length_y:
            fill_count = abs(length_x - length_y)
            if length_x > length_y:
                for i in range(fill_count):
                    bin_num_y = '0' + bin_num_y
            else:
                for i in range(fill_count):
                    bin_num_x = '0' + bin_num_x
        index = count = 0
        while index <= max(length_x, length_y) - 1:
            if bin_num_x[index] != bin_num_y[index]:
                count += 1
            index += 1
        return count
