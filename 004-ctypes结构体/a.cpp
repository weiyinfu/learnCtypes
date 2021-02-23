#include <string.h>
#define EXPORT_HELLO_DLL
#include "a.h"

char* GetStructInfo(struct StructTest* pStruct) {
  for (int i = 0; i < ARRAY_NUMBER; i++) pStruct->iArray[i] = i;
  pStruct->pChar = "hello python!";
  strcpy(pStruct->str, "hello world!");
  pStruct->number = 100;
  return "just OK";
}
