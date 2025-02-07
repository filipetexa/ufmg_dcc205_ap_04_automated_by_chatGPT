#include <stdlib.h>

struct Matrix
{
    int rows, cols;
    int** data;
};

int main(){
    int i;
    struct Matrix * rotation3D = (struct Matrix*) malloc(sizeof(struct Matrix)); // Alocando memória para a struct Matrix

    rotation3D->rows = 4;
    rotation3D->cols = 4;
    rotation3D->data = (int**) malloc(sizeof(int*) * rotation3D->rows);
    
    for(i = 0; i < rotation3D->rows; i++) {
        rotation3D->data[i] = (int*) malloc(sizeof(int) * rotation3D->cols);
    }
    
    // Liberando a memória alocada para cada linha de dados
    for(i = 0; i < rotation3D->rows; i++) {
        free(rotation3D->data[i]);
    }
    
    free(rotation3D->data); // Liberando a memória alocada para os ponteiros das linhas
    free(rotation3D); // Liberando a memória alocada para a struct Matrix
    
    return 0;
}