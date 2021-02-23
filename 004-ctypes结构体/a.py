from ctypes import *

ARRAY_NUMBER = 20;
STR_LEN = 20;
# define type
INTARRAY20 = c_int * ARRAY_NUMBER;
CHARARRAY20 = c_char * STR_LEN;


# define struct
class StructTest(Structure):
    _fields_ = [
        ("number", c_int),
        ("pChar", c_char_p),
        ("str", CHARARRAY20),
        ("iArray", INTARRAY20)
    ]


# load dll and get the function object
dll = cdll.LoadLibrary('./liba.so');
GetStructInfo = dll.GetStructInfo;
# set the return type
GetStructInfo.restype = c_char_p;
# set the argtypes
GetStructInfo.argtypes = [POINTER(StructTest)];
objectStruct = StructTest();
# invoke api GetStructInfo
retStr = GetStructInfo(byref(objectStruct));
# check result
print("number: ", objectStruct.number);
print("pChar: ", objectStruct.pChar);
print("str: ", objectStruct.str);
for i, val in enumerate(objectStruct.iArray):
    print('Array[i]: ', val);
print(retStr);
