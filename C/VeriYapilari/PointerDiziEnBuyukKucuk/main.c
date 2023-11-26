#include <stdio.h>
#include <stdlib.h>
#define n 10
#define N 10
int main()
{

    int dizi[n];
    int enBuyuk,enKucuk,*pointer;
    enBuyuk=dizi;

    printf("%d kadar deger giriniz\n",n);
    for(pointer=dizi;pointer<dizi+n;pointer++)
    {
        scanf("%d",pointer);
        printf("%d\n",pointer);
    }

enBuyuk=enKucuk=dizi[0];
    for(pointer=dizi+1;pointer<dizi+N;pointer++)
    {
        if(*pointer>enBuyuk)
        {
            enBuyuk=*pointer;
        }
        if(*pointer<enKucuk)
        {
            enKucuk=*pointer;
        }
    }
    printf("Dizimizin maksimum degeri: %d\n",enBuyuk);
    printf("Dizimizin enKucuk degeri : %d\n",enKucuk);

    return 0;
}
