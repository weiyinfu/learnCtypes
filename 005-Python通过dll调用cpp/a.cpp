#include <stdio.h>
/*
因为当前Python的设定中只能调用C函数，而不能直接调用C++的方法。
所以此处需要使用extern "C"来把C++用C重写。
 */
extern "C" {
int GOD_NUMBER = 19;
int add(int a, int b) { return a + b; }

void print_sum(unsigned long ulNum) {
  while (ulNum != 0) {
    printf("The ulNum is : %u\n", ulNum--);
  }
}
void print_love(char* s, int pos) { printf("%c", s[pos]); }
int sum_of_array(int *a, int n) {
  int s = 0;
  for (int i = 0; i < n; i++) {
    s += a[i];
    a[i]=-a[i];
  }
  return s;
}

}
