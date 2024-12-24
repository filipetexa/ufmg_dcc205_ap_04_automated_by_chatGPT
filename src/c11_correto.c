#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(void)
{
    char *msg = malloc(9); // Correção: Alocar espaço para 9 caracteres, incluindo o caractere nulo
    strcpy(msg, "Holberton");
    msg[0] = 'R';
    printf("%ld, %s\n", (long)getpid(), msg);
    free(msg); // Correção: Liberar a memória alocada
    return (0);
}
