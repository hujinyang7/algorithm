'''
假设 Andy 和 Doris 想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。
你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设答案总是存在。


示例 1:
输入: list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]，list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
输出: ["Shogun"]
解释: 他们唯一共同喜爱的餐厅是“Shogun”。

示例 2:
输入:list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]，list2 = ["KFC", "Shogun", "Burger King"]
输出: ["Shogun"]
解释: 他们共同喜爱且具有最小索引和的餐厅是“Shogun”，它有最小的索引和1(0+1)。
'''


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        return_list = []
        common_interest = set(list1) & set(list2)
        if len(common_interest) == 1:
            return list(common_interest)
        map_dict = {}
        for each in common_interest:
            map_dict[each] = list1.index(each) + list2.index(each)
        sorted_dict = sorted(map_dict.items(), key=lambda x: x[1])
        return_list.append(sorted_dict[0][0])
        min_index = sorted_dict[0][1]
        tmp_index = 1
        while tmp_index <= len(sorted_dict) - 1:
            if sorted_dict[tmp_index][1] == min_index:
                return_list.append(sorted_dict[tmp_index][0])
            tmp_index += 1
        return return_list
