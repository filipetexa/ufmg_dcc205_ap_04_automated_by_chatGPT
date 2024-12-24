#include <stdio.h>
#include <stdlib.h>

int inc(int a) {
  return a+1;
}

int main(int argc, char** argv) {
  for(int i=1; i < 5; i++) {
     int a = 1;
     a = inc(a);
  }

  return 0; // Corrigido para retornar 0 ao invés de argc
}