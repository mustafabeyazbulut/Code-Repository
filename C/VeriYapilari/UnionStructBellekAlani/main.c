#include <stdio.h>
#include <stdlib.h>

struct kontrol1{
    int x;
    char y;
    long z;
    };

    union kontrol2{
    int a;
    char b;
    long c;
    };

int main()
{
    /*Aþaðýda verilen struct ve union un bellekte ne kadar alan kapladýðýný bulan C programýný yazýnýz.
    */
   /* printf("%d\n",sizeof(char));
    printf("%d\n",sizeof(int));
    printf("%d\n",sizeof(float));
    printf("%d\n",sizeof(double));*/

    printf("struct =%d byte\n",sizeof(struct kontrol1));
    printf("union = %d byte",sizeof(union kontrol2));
    return 0;
}
