# Python和C++交互的几种方式
* ctypes
* swig
* cffi
* 直接使用Python.h：Python语言有多种实现如Jython（用Java语言实现的python）、IronPython（用C#实现的Python）、CPython（用C语言实现的Python），直接使用CPython提供的API可以使用C/C++写Python扩展。
* boost.python：boost是C++中包罗万象的大库，它基于Python.h头文件，对Python C API包装了一层
* pybind11：与boot.python类似，但是pybind11使用更为广泛。没有理由用boost.python而不用pybind11
* cython：numpy、scipy等库都是基于cython实现的

其中，只有cython和pybind11这两种方式是值得考虑的，其余方式了解即可。cython和pybind11不仅简单而且高效，完全没有用ctypes、swig、boost.python等库的必要。  


# ctypes
如例子001所示，直接运行build.sh即可生成一个动态链接库，基于python中的ctypes包直接加载这个动态链接库并运行即可。  

如例子002-ctype浮点数所示，如果使用其它数据类型，需要使用ctypes中的类型进行指明。  
