import io
import time

def except_test():
    f = None
    try:
        f = open('致橡树.txt','w',encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print("无法打开指定的文件！")
    except LookupError:
        print("制定了未知的编码！")
    except UnicodeDecodeError:
        print("读取文件时解码错误！")
    except io.UnsupportedOperation:
        print("文件不支持此类操作")
    finally:
        # 无论正常异常都会执行
        if f:
            f.close()

def with_test():
    try:
        with open('致橡树.txt','r',encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print("无法打开指定的文件！")
    except LookupError:
        print("制定了未知的编码！")
    except UnicodeDecodeError:
        print("读取文件时解码错误！")

def read_test():
    with open('致橡树.txt','r',encoding='utf-8') as f:
        print(f.read())
    with open('致橡树.txt',mode='r',encoding='utf-8') as f:
        for line in f:
            print(line,end='')
            time.sleep(0.3)
    print()
    with open("致橡树.txt",'r',encoding='utf-8') as f:
        lines = f.readlines()
    print(lines)

if __name__ == '__main__':
    # except_test()
    # with_test()
    read_test()