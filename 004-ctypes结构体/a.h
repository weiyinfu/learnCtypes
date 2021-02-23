#define ARRAY_NUMBER 20
#define STR_LEN 20

struct StructTest
{
 int number;
 char* pChar;
 char str[STR_LEN];
 int iArray[ARRAY_NUMBER];
};

extern "C"
{
 //HELLO_API int IntAdd(int , int);
  char* GetStructInfo(struct StructTest* pStruct);
}
