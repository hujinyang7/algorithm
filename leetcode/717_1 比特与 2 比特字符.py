'''
有两种特殊字符：
第一种字符可以用一比特 0 表示
第二种字符可以用两比特（10 或 11）表示
给你一个以 0 结尾的二进制数组 bits ，如果最后一个字符必须是一个一比特字符，则返回 true 。

示例 1:
输入: bits = [1, 0, 0]
输出: true
解释: 唯一的解码方式是将其解析为一个两比特字符和一个一比特字符。
所以最后一个字符是一比特字符。

示例 2:
输入：bits = [1,1,1,0]
输出：false
解释：唯一的解码方式是将其解析为两比特字符和两比特字符。
所以最后一个字符不是一比特字符。
'''



class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        str_bits = ''.join([str(each) for each in bits])
        double_bits = ['10', '11']
        single_bits = ['0']
        item_list = []
        index = 0
        while index < len(str_bits):
            double_str = str_bits[index: index+2]
            single_str = str_bits[index]
            if double_str in double_bits:
                item_list.append(double_str)
                index += 2
            elif single_str in single_bits:
                item_list.append(single_str)
                index += 1
        return item_list[-1] == '0'
