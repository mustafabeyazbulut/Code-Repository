#include <stdio.h>
#include <stdlib.h>


void listele(int sayi) //sayi=5
{

    if(sayi==0)
    {
        printf("%d",sayi);

    }
    else
    {
        printf("%d\n",sayi);
        listele(sayi-1);
    }
}







int main()
{
   /*Klavyeden girilen bir N positif tamsayısından 0 a kadar sayıların ekrana gösterilmesini
    sağlayan c programını yazınız*/

   int n;
   printf("Lutfen bir sayi giriniz");
   scanf("%d",&n);
   listele(n);
    return 0;
}
