# coding:utf-8
# @Time: 2022/9/25
# @Author: hujinyang
# @Email: hujinyang4@163.com
# @File: Q1.py
# @Project: sf_coding_test
import pandas as pd

def find_operation_time(operation_info, action):
    for each in operation_info:
        if action in each:
            return each[6:].strip()

def create_new_df(df):
    new_df_data = {
        '航班日期': [],
        '机型': [],
        '机尾号': [],
        '起飞机场': [],
        '计划落地时间': [],
        '实际落地时间': [],
        '卸机开始时间': [],
        '卸机结束时间': [],
        '落地机场': [],
        '装机开始时间': [],
        '装机结束时间': [],
        '计划起飞时间': [],
        '实际起飞时间': [],
    }
    # 获取机尾号列表
    aircraft_tail_nums = list(set([_d['机尾号'] for idx, _d in df.iterrows()]))
    aircraft_tail_nums.sort()
    for each_num in aircraft_tail_nums:
        each_aircraft_info = df.loc[df["机尾号"] == each_num, :]
        for inx, _d in each_aircraft_info.iterrows():
            operation_info = _d['装卸机操作'].split(';')
            if _d['航班日期'].day == 1:
                # 1号数据
                if _d['航班类型'] == '进港':
                    # 1号进港数据
                    new_df_data['航班日期'].append(_d['航班日期'])
                    new_df_data['机型'].append(_d['机型'])
                    new_df_data['机尾号'].append(_d['机尾号'])
                    new_df_data['起飞机场'].append(_d['起飞机场'])
                    new_df_data['计划落地时间'].append(_d['计划落地'])
                    new_df_data['实际落地时间'].append(_d['实际落地'])
                    new_df_data['卸机开始时间'].append(find_operation_time(operation_info, '卸机开始'))
                    new_df_data['卸机结束时间'].append(find_operation_time(operation_info, '卸机结束'))
                else:
                    # 1号离港数据
                    new_df_data['落地机场'].append(_d['落地机场'])
                    new_df_data['装机开始时间'].append(find_operation_time(operation_info, '装机开始'))
                    new_df_data['装机结束时间'].append(find_operation_time(operation_info, '装机结束'))
                    new_df_data['计划起飞时间'].append(_d['计划起飞'])
                    new_df_data['实际起飞时间'].append(_d['实际起飞'])
            else:
                # 2号数据
                if _d['航班类型'] == '进港':
                    # 2号进港数据
                    new_df_data['航班日期'].append(_d['航班日期'])
                    new_df_data['机型'].append(_d['机型'])
                    new_df_data['机尾号'].append(_d['机尾号'])
                    new_df_data['起飞机场'].append(_d['起飞机场'])
                    new_df_data['计划落地时间'].append(_d['计划落地'])
                    new_df_data['实际落地时间'].append(_d['实际落地'])
                    new_df_data['卸机开始时间'].append(find_operation_time(operation_info, '卸机开始'))
                    new_df_data['卸机结束时间'].append(find_operation_time(operation_info, '卸机结束'))
                else:
                    # 2号离港数据
                    new_df_data['落地机场'].append(_d['落地机场'])
                    new_df_data['装机开始时间'].append(find_operation_time(operation_info, '装机开始'))
                    new_df_data['装机结束时间'].append(find_operation_time(operation_info, '装机结束'))
                    new_df_data['计划起飞时间'].append(_d['计划起飞'])
                    new_df_data['实际起飞时间'].append(_d['实际起飞'])
    return pd.DataFrame(data=new_df_data)

def related_count(df):
    # 因之前没有接触过相关性的概念，所以不确定这样解是否正确
    # 将各机尾号两天的延误数据创建为一个新的df，然后通过 corr 函数计算相关性
    data={'进港延误(s)': [], '离港延误(s)': []}
    aircraft_tail_nums = list(set([_d['机尾号'] for idx, _d in df.iterrows()]))
    aircraft_tail_nums.sort()
    for each_num in aircraft_tail_nums:
        each_aircraft_info = df.loc[df["机尾号"] == each_num, :]
        for inx, _d in each_aircraft_info.iterrows():
            arrival_delay = _d['进港延误'].total_seconds()
            leave_delay = _d['离港延误'].total_seconds()
            data['进港延误(s)'].append(arrival_delay)
            data['离港延误(s)'].append(leave_delay)
        related_df = pd.DataFrame(data=data)
        relate_rate = related_df['进港延误(s)'].corr(related_df['离港延误(s)'])
        print(f'飞机尾号为: {each_num} 的进港延误与离港延误相关性为: {relate_rate}')
        data = {'进港延误(s)': [], '离港延误(s)': []}



if __name__ == '__main__':
    # 读取 excel 数据
    df = pd.read_excel('.\source_data.xlsx', engine='openpyxl', skiprows=1, skipfooter=7,
                       usecols=list(range(11)))
    # 1.按照机尾号，对进港实际落地时间先后排序
    df.sort_values(by=["机尾号", "航班类型", "实际落地", "实际起飞"], ascending=[True, False, True, True], inplace=True)
    # print(df)

    #2.建立新的数据表
    new_df = create_new_df(df)
    # print(new_df)
    # 写入到 cleaned_data.xlsx
    writer = pd.ExcelWriter('cleaned_data.xlsx', engine='openpyxl', index='航班日期')
    new_df.to_excel(writer)
    writer.save()

    # 3.新增进港延误和离港延误字段
    new_df.loc[:, "进港延误"] = new_df["实际落地时间"] - new_df["计划落地时间"]
    new_df.loc[:, "离港延误"] = new_df["实际起飞时间"] - new_df["计划起飞时间"]
    print(new_df)

    # 4.计算进港延误与离岗延误相关性
    related_count(new_df)



