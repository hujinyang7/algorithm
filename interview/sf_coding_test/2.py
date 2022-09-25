# coding:utf-8

import simpy


from random import seed, randint
seed(23)

import simpy



# 描述一个汽车驾驶一段时间后停车充电， 汽车驾驶进程和电池充电进程通过事件的激活来相互影响
class EV:
    def __init__(self, env):
        self.env = env
        self.drive_proc = env.process(self.drive(env))
        self.bat_ctrl_proc = env.process(self.bat_ctrl(env))
        self.bat_ctrl_reactivate = env.event()
        self.bat_ctrl_sleep = env.event()


    def drive(self, env):
        """驾驶进程"""
        while True:
            # 驾驶 20-40 分钟
            print("开始驾驶 时间: ", env.now)
            yield env.timeout(60)
            print("停止驾驶 时间: ", env.now)

            # 停车 1-6 小时
            print("开始停车 时间: ", env.now)
            self.bat_ctrl_reactivate.succeed()  # 激活充电事件
            self.bat_ctrl_reactivate = env.event()
            yield env.timeout(60) & self.bat_ctrl_sleep # 停车时间和充电程序同时都满足
            print("结束停车 时间:", env.now)

    def bat_ctrl(self, env):
        """电池充电进程"""
        while True:
            print("充电程序休眠 时间:", env.now)
            yield self.bat_ctrl_reactivate  # 休眠直到充电事件被激活
            print("充电程序激活 时间:", env.now)
            yield env.timeout(60)
            print("充电程序结束 时间:", env.now)
            self.bat_ctrl_sleep.succeed()
            self.bat_ctrl_sleep = env.event()



if __name__ == '__main__':
    env = simpy.Environment()
    ev = EV(env)
    env.run(until=600)

