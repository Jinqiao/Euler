#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "libEulerUtil.h"

int IsCirPrime(IntArrWithSize v){

  int i, j, k, n, numP = 0;

  for(i = 0; i < v.size; i++){
    int d = v.arr[i];
    if(d == 0 || d % 2 == 0 || d == 5){
      return 0;
    }
  }

  for(i = 0; i < v.size; i++){
    n = 0;
    for(j = 0; j < v.size; j++){
      k = (i + j) % v.size;
      n += (int)pow(10, v.size - j - 1) * v.arr[k];
    }
    // printf("n is %d\n", n);
    if(IsPrime(n)){
      numP++;
    }
  }
  return numP == v.size ? 1 : 0;
}


int main(int argc, char* argv[]){
  int i =0 , r = 13;
  for(i = 101; i < 1000000; i=i+2){
    IntArrWithSize a = toArray(i);
    if(IsCirPrime(a)) {
     r++;
     //printf("found one: %d\n", i);
    }
  }

  printf("there are %d Cir Primes before 1,000,000", r);

  return 0;
}
