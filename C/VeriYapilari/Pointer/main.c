#include <stdio.h>
#include <stdlib.h>

int main()
{
    char dizi[100]="canan";
    char *pointer;

    pointer=dizi;

    printf("dizi degiskenimin 5. karakteri %c\n",dizi[4]);
    printf("pointer degiskenimin 4. karakteri %c\n",*(pointer+3));


    return 0;
}
