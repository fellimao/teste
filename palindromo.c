#include<stdio.h>

int verif(char v[100], int n, int i)
{
    
    if(n!=0 && n!=1)
    {
        if(i!=n/2)
        {
            if(v[i]==v[n-(i+1)])
                return 0+verif(v, n, i+1);
            else
                return 1;
        }
        else 
        {
            if(v[i]==v[n-(i+1)])
                return 0;
            else
                return 1;
        }
    }
    else
        return 0;
    
}
void main()
{
    char v[100];
    int n, i, retorno=0;
    printf("Digite o tamanho da palavra: ");
    scanf("%d", &n);
    printf("Digite a palavra: ");
    scanf("%s", v);
    retorno=verif(v, n, 0);
    if(retorno==0)
    {
        printf("\nEh palindrome\n");
    }
    else
    {
        printf("\nNao eh palindrome\n");
    }
}
