#include "pycall.h"

extern "C" {

PythonTest py; 

int init(int num){
    return py.init(num);
}

bool is_inited(){
    return py.is_inited();
}

int str2(char* src, char* dest, int len){
    return py.str2(src, dest, len);
}

int add(int a, int b){ 
    return a + b;
}

}
