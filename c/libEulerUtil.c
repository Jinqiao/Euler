#include <math.h>

int IsPrime(int n)
{
  n = n > 0 ? n : -n;
  if(n == 0 || n == 1 || n == 2 || n == 3)
    return 1;
  int i = 2;
  int ceil = sqrt(n);
  while(i <= ceil){
    if(n % i == 0) return 0;
    i++;
  }
  return 1;
}
