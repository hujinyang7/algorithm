# coding:utf-8
# @Time: 2023/08/09
# @Author: hujinyang
# @Email: hujinyang4@163.com
from typing import Dict, List, Optional

DependencyTree = Dict[str, List[str]]
ComputeOrderList = List[str]



def parse_compute_order(tp: str, dep: DependencyTree) -> Optional[ComputeOrderList]:
    if not dep.get(tp):
        return None
    return_list = [tp]
    node_queue = dep.get(tp).copy()
    count = 0
    while node_queue:
        for i in range(len(node_queue)):
            current_node = node_queue.pop(0)
            if current_node not in return_list:
                return_list.append(current_node)
            # 追加子节点到队列
            if dep.get(current_node):
                node_queue.extend(dep.get(current_node))
        count += 1
        if count == 1000:
            return None   # 存在循环引用, 直接返回 None
    return_list.reverse()
    return return_list



if __name__ == '__main__':
    # dep = {
    #     'B': ['A'],
    #     'A': [],
    #     'D': ['B'],
    #     'E': ['B'],
    #     'C': ['A'],
    #     'F': ['C', 'E'],
    #     'G': ['C', 'D', 'E'],
    #     'H': ['G', 'E']
    #     }
    # print(parse_compute_order('D', dep))   # ['A', 'B', 'D']
    # print(parse_compute_order('F', dep))   # ['B', 'A', 'E', 'C', 'F']
    # print(parse_compute_order('K', dep))   # None

    # case 1
    dep = {
        'G': ['I'],
        'I': [],
        'L': ['G'],
        'K': ['G'],
        'M': ['K'],
        'N': ['M', 'K'],
        'O': ['N', 'M', 'L'],
        'P': ['N', 'L']
    }
    print(parse_compute_order('I', dep))   # 元素值为空列表直接返回 None
    print(parse_compute_order('L', dep))   # ['I', 'G', 'L']
    print(parse_compute_order('O', dep))   # ['I', 'G', 'K', 'L', 'M', 'N', 'O']

    # case 2
    # dep = {
    #     'U': ['V'],
    #     'V': ['U'],
    #     'W': ['X'],
    #     'X': [],
    #     'Y': ['W', 'U'],
    # }
    # print(parse_compute_order('U', dep))   # 循环引用直接返回 None
    # print(parse_compute_order('V', dep))   # 循环引用直接返回 None
    # print(parse_compute_order('W', dep))   # ['X', 'W']
    # print(parse_compute_order('X', dep))   # 元素值为空列表直接返回 None
    # print(parse_compute_order('Y', dep))   # 元素存在循环引用, 直接返回 None
