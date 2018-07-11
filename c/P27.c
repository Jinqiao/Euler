#include <stdio.h>
#include "libEulerUtil.h"

int NumP27Primes(int a, int b);

int main(){
  int max = 0;

  printf("started\n");

  for (int a = -999; a < 1000; a++)
    for (int b = -1000; b < 1001; b++)
      {
        int n = NumP27Primes(a, b);
        // printf("n: {%d}, a: {%d}, b: {%d}\n", n, a, b);
        if (n <= max) continue;
        max = n;
        printf("max: {%d}, a: {%d}, b: {%d}\n", max, a, b);
      }

  printf("finished\n");

  return 0;
}

int NumP27Primes(int a, int b){
  int n = 0;
  while(IsPrime(n * n + a * n + b )){
    n++;
  }
  return n;
}
