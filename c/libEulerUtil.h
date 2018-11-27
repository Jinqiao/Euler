#include <math.h>

typedef struct intArrWithSize {
  int* arr;
  int size;
} IntArrWithSize;

int IsPrime(int n);
void swap(int[], int, int);
IntArrWithSize toArray(int number);
IntArrWithSize toArray2(int number);
int toInt(IntArrWithSize a);
