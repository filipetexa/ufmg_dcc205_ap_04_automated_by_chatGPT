#include<stdlib.h>
#include<stdio.h>
#include<time.h>

const int ARR_SIZE = 1000;

int main() {
    // create an array of ARR_SIZE ints
    int *intArray = malloc(sizeof(int) * ARR_SIZE);

    // check if memory allocation was successful
    if(intArray == NULL) {
        printf("Erro ao alocar memória.\n");
        return 1;
    }

    // populate them
    for (int i=0; i < ARR_SIZE; i++) {
        intArray[i] = i;
    }

    // print one out
    // first, seed the random number generator
    srand(time(NULL));
    int randNum = rand() % ARR_SIZE;

    printf("intArray[%d]: %d\n", randNum, intArray[randNum]);

    // free the allocated memory
    free(intArray);

    return 0;
}