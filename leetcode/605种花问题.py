'''
假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
给你一个整数数组 flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n ，能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false 。

示例 1：
输入：flowerbed = [1,0,0,0,1], n = 1
输出：true

示例 2：
输入：flowerbed = [1,0,0,0,1], n = 2
输出：false
'''



class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        index = 0
        while index < length:
            if flowerbed[index] == 0:
                # 边界情况[0]
                if (index == length - 1):
                    n -= 1
                    break
                # [0,0]当前可以种，下标+2
                if flowerbed[index+1] == 0:
                    n -= 1
                    index += 2
                # [0,1]当前不能种，下下个也不能，下标+3
                elif flowerbed[index+1] == 1:
                    index += 3
            elif flowerbed[index] == 1:
                index += 2
        return n <= 0
