//soma de impares soma= 1+3+5+...+(2n-1)

#include <stdio.h>
int soma(int n)
{
    if (n==1) //n=quantidade de termos
        return (1);
    else
        return (soma(n-1)+(2*n-1));
}

void main()
{
    int n;
    scanf("%d", &n);
    printf("%d\n", soma(n));
}

