#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <glib.h>

int comp(const void *a,const void *b) {
  char *x = (char *) a;
  char *y = (char *) b;
  return *x - *y;
}

int main()
{
  long i = 0, c = 0;
  char k[30];
  GHashTable *hash = g_hash_table_new(g_str_hash, g_str_equal);
  GSList *list = NULL;

  while (1) {
    i++;
    c = i * i * i;
    sprintf(k, "%ld", c);
    qsort(k, strlen(k), sizeof(char), comp);



    list = g_hash_table_lookup(hash, k);
    if(list == NULL){
      g_hash_table_insert(hash, k, g_slist_append(NULL, GINT_TO_POINTER(c)));
    }
    else{
      list =g_slist_append(list, GINT_TO_POINTER(c));
    }

    if (g_slist_length(list) >= 5) {
      break;
    }
  }

  GSList *iter = NULL;
  for (iter = list; iter; iter = iter -> next) {
    printf("k: %s, c: %ld\n", k, (long)iter -> data);
  }

  return 0;
}
