# coding:utf-8
# @Time: 2022/9/25
# @Author: hujinyang
# @Email: hujinyang4@163.com
# @File: Q2.py
# @Project: sf_coding_test

import simpy

'''
# Todo
由于时间仓促，只有半天时间学习了 simpy 模块的简单使用，所以这里的代码只能完成到一半
我大概写一下我理解的解题思路
1.加油车的加油状态和在路上行驶的状态需要通过 event 控制
2.只有三辆加油车可供加油，所以加油车需要抽象为 Resource 对象
3.中途有一辆加油车被紧急调走,这里涉及到资源的动态调整，所以这里的资源创建需要使用 PriorityResource 对象实现，预先设置最大资源数为3
当4个小时之后，使用一个优先级为 -1 的 request 去占用资源，而之前的进程则默认还是用优先级为0去使用资源。
'''
def source(env, number, res):
    count = 1
    for i in range(number):
        if i and i % 3 == 0:
            yield env.timeout(20)
        env.process(airplane(env, f'plane_{i+1}', res, 20*count, 60))

def airplane(env, name, res, driving_time, oil_time):
    # 等待加油车到达服务站
    yield env.timeout(driving_time)
    print(f'加油车已到达服务站, 开始给飞机 {name} 加油! 时间: {env.now}')
    with res.request() as req:
        yield req
        print(f'飞机 {name} 开始加油! 时间: {env.now}')
        yield env.timeout(oil_time)
        print(f'飞机 {name} 完成加油! 时间:{env.now}')



if __name__ == '__main__':
    plane_nums = 25
    env = simpy.Environment()
    res = simpy.PriorityResource(env, capacity=3)

    env.process(source(env, plane_nums, res))
    env.run()
