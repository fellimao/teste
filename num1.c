#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main () {
	int vet[10];
	int i;
	for (i=0; i<10; i++) 
		vet[i]=rand()%10;
	printf("Os numeros sao: ");
	for (i=0; i<10; i++)
		printf("%d ", vet[i]);
	printf("\n");
	printf("A ordem inversa eh: ");
	for (i=9; i>=0; i--)
		printf("%d ", vet[i]);
	return (0);
}