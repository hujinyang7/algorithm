# 进程中断的实现
import simpy
from simpy import Interrupt, Environment

env = Environment()

def interrupter(env, victim_proc):
    yield env.timeout(1)
    victim_proc.interrupt('Spam')

def victim(env):
    try:
        yield env.timeout(10)
    except Interrupt as interrupt:
     cause = interrupt.cause
