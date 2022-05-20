#include<stdio.h>
#include <stdlib.h>


// A*x = v
int main( int argc, char *argv[]) {
    
    // Inicializar variáveis
    int n = atoi(argv[1]);
    int A[n][n];
    int x[n];
    int r; // valor de um elemento de v

    // Popular A e x com valores aleatórios
    for (int i = 0; i < n; i++) {
        
        x[i] = rand() % 10;

        for (int j = 0; j < n; j++) {

            A[i][j]  = rand() % 100;
        }
    }

    
    // Calcular produto A*x
    // Para cada linha de A
    for (int i = 0; i < n; i++) {
        
        r = 0;

        // Para cada elemento da linha
        for (int j = 0; j < n; j++) {
            
            r = r + A[i][j] * x[j];
        }
        
    }

    return 0;
}
