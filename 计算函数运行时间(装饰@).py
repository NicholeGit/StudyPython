# 装饰器   
import time
def timer(func):
    def wrapper(*args,**kwargs):
        start_time=time.clock()
        res=func(*args,**kwargs)
        stop_time=time.clock()
        print('函数[%s],运行时间[%s]' %(getattr(func,'__name__'),stop_time-start_time))
        return res
    return wrapper
    
@timer  #@timer就等同于cal=timer(cal)    
def cal(array):
    res=0
    for i in array:
        res+=i
    return res

cal(range(10))   #函数[cal],运行时间是[4.23721332603591e-06]