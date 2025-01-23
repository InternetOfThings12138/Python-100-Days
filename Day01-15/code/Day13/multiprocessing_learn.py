from multiprocessing import Pool, Process
import os


def f(x):
    return x * x


def f2(name):
    print("hello", name)


def f3(name):
    info('function f')
    print('hello',name)


def pool_test():
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))


def info(title):
    print(title)
    print('module name:',__name__)
    print('parent process:',os.getppid())
    print('process id:',os.getpid())


def process_test(func,args):
    p = Process(target=func, args=args)
    p.start()  # 生成进程
    p.join()

def process_id():
    info('main line')
    process_test(f3,("wsh",)) # 子进程

if __name__ == '__main__':
    # process_test(f2,("wsh",))
    process_id()