/*Questão 4*/
#include <stdio.h>
#include <limits.h>

//O protótipo da função é da seguinte forma: void maior_menor(int *v, int n);
void maior_menor(int *v, int n);
int main()
{
    int tamanho;
    printf("Digite o tamanho do vetor: ");
    scanf("%d", &tamanho);
    int vetor[tamanho];

    for (int i = 0; i < tamanho; ++i)
    {
        printf("Digite um valor para a posicao %d do vetor: ", i+1);
        scanf("%d", &vetor[i]); //Lẽ os valores
    }
    maior_menor(vetor, tamanho);

}
void maior_menor(int *v, int n) //Função que mostra o maior e menor valores do vetor
{
    int maior = INT_MIN; // Inicializa o maior com menor valor inteiro
    int menor = INT_MAX; // Inicializa o menor com maior valor inteiro

    for (int i = 0; i < n; i++){ // Seleciona o menor e maior valor
        if (v[i] > maior){ 
            maior = v[i];
        }
        if (v[i] < menor){
            menor = v[i];
        }
    }

    printf("Maior número: %d, Menor número:  %d", maior, menor);

}