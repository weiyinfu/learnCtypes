from ctypes import cdll,c_float,c_double

a=cdll.LoadLibrary("./liba.so")
print(dir(a))
ans=a.sum(c_float(3.14),c_double(5.28))
print(ans)
a.sum.argtypes=[c_float,c_double]
a.sum.restype=c_float
print(a.sum(3.14,5.28))
