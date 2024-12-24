#include <stdlib.h>
#include <stdio.h>

int main(void)
{
        int *p;
        while(1)
        {
                p = malloc(128);
                if(p == NULL) // Verifica se a alocação de memória foi bem sucedida
                {
                    printf("Erro ao alocar memória\n");
                    break; // Encerra o loop caso a alocação falhe
                }
                printf("%p\n", (void*)p); // Corrigido para imprimir um ponteiro como endereço
        }
        free(p); // Libera a memória alocada antes de encerrar o programa
        return (0);
}
