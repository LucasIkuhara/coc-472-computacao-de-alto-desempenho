#include<stdio.h>
#include <stdlib.h>


// A*x = b
int main( int argc, char *argv[]) {
    
    // Inicializar variáveis
    int n = atoi(argv[1]);
    float A[n][n];
    float x[n];
    float b[n];

    // Popular A e x com valores aleatórios
    for (int i = 0; i < n; i++) {
        
        x[i] = (float)rand()/RAND_MAX;

        for (int j = 0; j < n; j++) {

            A[i][j]  =  (float)rand()/RAND_MAX;
        }
    }   

    
    // Calcular produto A*x
    // Para cada linha de A
    for (int i = 0; i < n; i++) {
        
        b[i] = 0;

        // Para cada elemento da linha
        for (int j = 0; j < n; j++) {
            
            b[i] = b[i] + A[j][i] * x[j];
        }

    }

    printf(" %f", b[n-1]);

    return 0;
}
