from ctypes import *

if __name__ == '__main__':
    # dll = CDLL("./liba.so")			# 加载dll方式一
    # dllj=cdll.a
    dll = cdll.LoadLibrary("./liba.so")  # 加载dll方式二
    print(dir(dll))
    print(dll.add(2, 6))			# 调用dll中add方法
    dll.print_sum(10)				# 调用dll中print_sum方法
