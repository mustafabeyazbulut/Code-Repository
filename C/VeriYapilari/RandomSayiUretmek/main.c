#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    int dizi[100];
    printf("Random uretilecek sayi miktarini giriniz:");
    scanf("%d",&n);

    srand(time(0));
    for(int i=0;i<n;i++){

        dizi[i]=rand()%10;
        printf("%d\n",dizi[i]);
    }

    return 0;
}
