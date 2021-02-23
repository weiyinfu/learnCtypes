#include <stdio.h>
#include <stdlib.h>
#include <string.h>

class PythonTest{
public:
    PythonTest():_is_inited(false), _num(0){
    
    }   

    int init(int num){
        _num = num;
        _is_inited = true;
        printf("inited ok\n");
        return 0;
    }   
    
    int str2(char *src, char* dest, int len){
        if (src == NULL || len <= 0){ 
            return 0;
        }   

        int src_len = strlen(src);
        int num = snprintf(dest, len, "%s%s", src, src);
        return (num < len -1)? num:0;
    }   

    bool is_inited(){
        printf("_num = %d\n", _num);
        return _is_inited;
    }   

private:
    bool _is_inited;
    int _num;
};
