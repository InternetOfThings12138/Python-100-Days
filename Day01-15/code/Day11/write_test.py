from math import sqrt

def is_prime(n):
    assert n > 0
    for factor in range(2,int(sqrt(n))+1):
        if n % factor == 0:
            return False
    return True if n != 1 else False

def main():
    filenames = ('a.txt','b.txt','c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename,'w',encoding='utf-8'))
        for i in range(1,10000):
            if is_prime(i):
                if i<100:
                    fs_list[0].write(str(i)+'\n')
                elif i<1000:
                    fs_list[1].write(str(i)+'\n')
                else:
                    fs_list[2].write(str(i)+'\n')
    except IOError as e:
        print(e)
        print("写文件时发生错误！")
    finally:
        for fs in fs_list:
            fs.close()
    print("操作完成！")

def copy_image():
    try:
        with open('mm.jpg','rb') as fs1:
            data = fs1.read()
            print(type(data))
        with open("mm_copy.jpg",'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print("指定的文件无法打开")
    except IOError as e:
        print('读写文件时出现错误')
    print("程序执行结束")


if __name__ == '__main__':
    # main()
    copy_image()