#include <stdio.h>
#include <stdlib.h>
#include "libEulerUtil.h"


int ways(int, int);
int coins[8] = {1, 2, 5, 10, 20, 50, 100, 200};

int main(int argc, char **argv){
  if(argc <= 1){
    printf("Please enter amount\n");
    return 1;
  }

  int amount = atoi(argv[1]);

  printf("Result is %d\n", ways(amount, 7));
  return 0;
}

// t is target amount, i is current index in coins array(start from end)
int ways(int t, int i){
  if(i <= 0 || t == 0) return 1;

  int r = 0;
  while(t >= 0){
    r = r + ways(t, i - 1);
    t = t - coins[i];
  }
  return r;
}
