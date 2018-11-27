#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include "libEulerUtil.h"


int IsPrime(int n)
{
  //printf("IsPrime, n=%d\n", n);
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


/* function to swap array elements */
void swap (int v[], int i, int j) {
  int	t;

  t = v[i];
  v[i] = v[j];
  v[j] = t;
}

int factorial(int n)
{
  if (n == 0)
    return 1;
  else
    return(n * factorial(n-1));
}

/* int to an array of digits */
IntArrWithSize toArray(int number)
{
    int n = log10(number) + 1;
    int i;
    int *numberArray = calloc(n, sizeof(int));
    for (i = n - 1; i >= 0; i--, number /= 10 )
    {
        numberArray[i] = number % 10;
    }

    IntArrWithSize r;
    r.arr = numberArray;
    r.size = n;
    return r;
}

IntArrWithSize toArray2(int number)
{
  /* count number of digits */
  int c = 0; /* digit position */
  int n = number;

  while (n != 0)
    {
      n /= 10;
      c++;
    }

  int *numberArray = calloc(c, sizeof(int));

  c = 0;
  n = number;

  /* extract each digit */
  while (n != 0)
    {
      numberArray[c] = n % 10;
      n /= 10;
      c++;
    }
  IntArrWithSize r;
  r.arr = numberArray;
  r.size = c;
  return r;
}


int toInt(IntArrWithSize a){
  int i, n = 0;
  for(i = 0; i < a.size; i++){
    n += (int)pow(10, a.size - i - 1) * a.arr[i];
  }
  return n;
}


/* recursive function to generate permutations */
void perm (int v[], int n, int i) {
  int	j;

  /* if we are at the end of the array, we have one permutation
   * we can use (here we print it; */
  if (i == n) {
    for (j=0; j<n; j++) printf ("%d ", v[j]);
    printf ("\n");
  } else
    /* recursively explore the permutations starting
     * at index i going through index n-1
     */
    for (j=i; j<n; j++) {

      /* try the array with i and j switched */

      swap (v, i, j);
      perm (v, n, i+1);

      /* swap them back the way they were */

      swap (v, i, j);
    }
}
