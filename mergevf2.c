#include <stdio.h>
#include <stdlib.h>

/*funções */
void merge(int v[], int esq, int m, int dir);
void mergeSort(int v[], int esq, int dir);

int main() 
{ 
    int v[5];//vetor
    int i;//contador
    int v_size = sizeof(v)/sizeof(v[0]); 
    int o;//criar ou não um arquivo
    int c;
    int A[i];
    int size;
    
    printf ("Escolha uma opcao:\n 1-Criar um arquivo \n 2-Visualizar um arquivo pre-existente\n 3-Sair\n");
    scanf("%d", &o);
  	
  	FILE *arq;
    arq = fopen("mergesort","r");
    if(o==1){
    	FILE *arq;
        arq = fopen("mergesort","w");
	   	
		   printf("MergeSort\n");
    	printf("Digite 5 numeros:\n");
		
		for (i=0; i<v_size; i++){
			scanf("%d", &v[i]);
		}
		
		for (i=0; i<v_size; i++){
			printf("%d |", v[i]);
		}
		
  
   		mergeSort(v, 0, v_size - 1); 
  
    	printf("\n Ordenado: \n");
    	for (i=0; i < v_size; i++) {
        	printf("%d ", v[i]); 
        	fprintf(arq, "%d ", v[i]);
		}
        fclose(arq);
        
        printf("\nDados gravados com sucesso");

        getch();
   		printf( "\n");
   		
    	return main(); 
	}
    
    else if( o == 2){
        if(arq == NULL){
            printf("Erro na abertura do arquivo");
            return 0;
        }else{
            while((c = getc(arq)) != EOF)
          
            printf("%c", c);
            fclose(arq);
            printf("\nFim do programa!\n");
            return main();
        }
    }
  
	else {
		system("exit");
	}
} 

void merge(int v[], int esq, int m, int dir) 
{ 
    int i, j, k; 
    int n1 = m - esq + 1; 
    int n2 =  dir - m; 
  
    int E[n1], D[n2]; //array temporarios
  
    /* copia dados do array temporario E[] e D[] */
    for (i = 0; i < n1; i++) 
        E[i] = v[esq + i]; 
    for (j = 0; j < n2; j++) 
        D[j] = v[m + 1+ j]; 
  
    i = 0; // indice inicial do primeiro subarray
    j = 0; // indice segundo do primeiro subarray
    k = esq; // indice terceiro do primeiro subarray
    
    while (i < n1 && j < n2) 
    { 
        if (E[i] <= D[j]) //combina os vetores ordenadamente
        { 
            v[k] = E[i]; 
            i++; 
        } 
        else
        { 
            v[k] = D[j]; 
            j++; 
        } 
        k++; 
    } 
  
    /* Copia os elementos restantes de E[], se houver algum */
    while (i < n1) 
    { 
        v[k] = E[i]; 
        i++; 
        k++; 
    } 
  
    /* Copia os elementos restantes de D[], se houver algum */
    while (j < n2) 
    { 
        v[k] = D[j]; 
        j++; 
        k++; 
    } 
} 
  
/* E é o índice esquerdo e D é o índice direito do subarray de arr para ser classificado */
void mergeSort(int v[], int esq, int dir) 
{ 
    if (esq < dir) 
    { 
        int m = esq+(dir-esq)/2; 
  
        mergeSort(v, esq, m); 
        mergeSort(v, m+1, dir); 
  
        merge(v, esq, m, dir); 
    } 
} 
  


