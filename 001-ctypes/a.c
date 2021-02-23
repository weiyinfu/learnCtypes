#include <stdio.h>
/*
因为当前Python的设定中只能调用C函数，而不能直接调用C++的方法。
 */
int add(int a, int b) { return a + b; }

void print_sum(unsigned long ulNum) {
  while (ulNum != 0) {
    printf("The ulNum is : %u\n", ulNum--);
  }
}
