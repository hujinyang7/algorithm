'''
读取txt文件字符，并放入列表中，然后将连续的字母作为一个字符串，按照长度从大到小排列，value包含字符串以及其长度存入字典
例如：
Hello_1234,p.Hello/asdg,5ddsaAD!dsa0,world!
输出：
{0: {'value': 'p', 'len': 1},
1: {'value': 'dsa', 'len': 3},
2: {'value': 'asdg', 'len': 4},
3: {'value': 'Hello', 'len': 5},
4: {'value': 'Hello', 'len': 5},
5: {'value': 'world', 'len': 5},
6: {'value': 'ddsaAD', 'len': 6}}
'''

def solution(s):
    return_dict = {}
    s = s.replace(',', ' ').replace('.', ' ').replace('/', ' ').replace('.', ' ').replace('!', ' ').strip()
    each_list = s.split(' ')
    tmp_list = []
    for each in each_list:
        tmp_str = ''
        for item in each:
            if not item.isalpha():
                tmp_str += item
        if tmp_str:
           each = each.replace(tmp_str, '')
        tmp_list.append(each)
    tmp_list.sort(key=lambda each: len(each))
    for index, each_str in enumerate(tmp_list):
        return_dict[index] = {'value': each_str, 'len': len(each_str)}
    return return_dict

def solution2(s):
    import re
    return_dict = {}
    str_list = re.split('[\s._()!-?]+', s)
    str_list.pop()
    str_list.sort(key=lambda each: len(each))
    for index, each_str in enumerate(str_list):
        return_dict[index] = {'value': each_str, 'len': len(each_str)}
    return return_dict


if __name__ == '__main__':
    print(solution('Hello_1234,p.Hello/asdg,5ddsaAD!dsa0,world!'))
    print(solution2('Hello_1234,p.Hello/asdg,5ddsaAD!dsa0,world!'))
