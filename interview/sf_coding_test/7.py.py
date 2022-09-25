# 多段进程模拟按时间安排的开关
import simpy

PROCESS_TIME = 3

def put_item(env, store):
    for i in range(20):
        yield env.timeout(0.5)
        store.put(f"{i}_item")

def process(i, env, store, start, end):

    yield env.timeout(start)
    while True:
        item = yield store.get()
        # 判断 item 到达时间是否超出本进程关闭时间
        if env.now > end:
            print(f"{env.now} - process {i} - end")
            store.put(item)
            env.exit()
        else:
            print(f"{env.now} - {item} - start")
            yield env.timeout(PROCESS_TIME)
            print(f"{env.now} - {item} - end")

env = simpy.Environment()
store = simpy.Store(env)

env.process(put_item(env, store))

for i, (start, end) in enumerate([(20, 30), (40, 50), (60, 90)]):
    env.process(process(i, env, store, start, end))

env.run()
