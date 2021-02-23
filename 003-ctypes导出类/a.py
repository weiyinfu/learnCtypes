# coding=utf-8

import ctypes
from ctypes import *

##加载库文件
ll = ctypes.cdll.LoadLibrary
lib = ll("./liba.so")

##call
fun = lib.init  ###类似C/C++函数指针
fun.restype = c_int  ##设置函数返回值类型
print(fun(8))
print("*" * 20)

##call
fun = lib.is_inited
fun.restype = c_bool
print(fun())
print("*" * 20)

##call
fun = lib.str2
src = "hello world "
dest = "*" * 30  ###申请buf, 用于保存返回结果
num = fun(src, dest, len(dest))  ###传递指针作为参数
if num != 0:
    print(dest[:num])
else:
    print("buf is not ok")
print("*" * 20)

##call
print(lib.add(1, 2))
print("*" * 20)
