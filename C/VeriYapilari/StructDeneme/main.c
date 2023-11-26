#include <stdio.h>
#include <stdlib.h>
#include <string.h>
struct ogrenci{
char ad[20];
char soyad[20];
int yas;
};

int main()
{



    struct ogrenci can;

    strcpy(can.ad,"Can");
    strcpy(can.soyad,"Boz");
    can.yas=27;
    struct ogrenci canan={"Mustafa","BEYAZBULUT",29};;

    printf("%s %s %d \n",can.ad,can.soyad,can.yas);
    printf("%s %s %d \n",canan.ad,canan.soyad,canan.yas);




    return 0;
}
