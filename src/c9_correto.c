#include <stdlib.h>

void f(void) {
    int* x = malloc(10 * sizeof(int));
    x[9] = 0; // Corrigido o índice para acessar a última posição do array
    free(x); // Liberando a memória alocada
}

int main(void) {
    f();
    return 0;
}
