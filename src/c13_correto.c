
#include <stdio.h>
#include <stdlib.h>

int main()
{
  char *p;

  p = (char *) malloc(19);
  free(p); // Liberando a memória alocada anteriormente
  p = (char *) malloc(16);

  return 0;
}