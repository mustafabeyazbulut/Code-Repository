#include <stdio.h>
#include <stdlib.h>

int main()
{
   char dizi[5][50];
   char *ilk;
   char *ikinci;
   int i;
   char gecici;

   printf("Lutfen 5 adet kelime giriniz:  \n");

   for(i=0;i<5;i++)
   {
       printf("%d. kelime ",i);
       scanf("%s",dizi[i]);
   }

   for(i=0;i<5;i++)
   {
      ilk=ikinci=dizi+i;

          for(;*ikinci;ikinci++);//*ikinci bo� karaktere geldi�inde yani s�f�r oldu�unda durur
          ikinci--; // 0 diznin son karakterden sonras�s�d�r. -1 olunca son karakter olur
          for(;ilk<ikinci;ilk++,ikinci--){
              gecici=*ilk;
              *ilk=*ikinci;
              *ikinci=gecici;
          }
   }

   for(i=0;i<5;i++)
   {
       printf("%s \n",*(dizi+i));
   }








    return 0;
}
