from ctypes import *

if __name__ == "__main__":
    # dll = CDLL("./liba.so")			# 加载dll方式一
    dll = cdll.LoadLibrary("./liba.so")  # 加载dll方式二
    print(dll.add(2, 6))  # 调用dll中add方法
    dll.print_sum(10)  # 调用dll中print_sum方法
    dll.print_love(b"live", 0)
    dll.print_love(b"cool", 1)
    dll.print_love(b"have", 2)
    dll.print_love(b"none", 3)
    god=c_int.in_dll(dll,'GOD_NUMBER')
    print(god)
    print(dir(god))
    print(god.value)

    int10=c_int*10
    ar=int10()
    for i in range(10):
        ar[i]=c_int(i)
    print(f"sum of {ar}",dll.sum_of_array(ar,10))
    for i in ar:
        print(i,end=',')
