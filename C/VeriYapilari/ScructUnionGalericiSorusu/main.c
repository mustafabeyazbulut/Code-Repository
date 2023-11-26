#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
   /*
    1-Galeri sahibi için araba adlı bir yapı tipi tanımlayınız.Bu yapıdaki ilk eleman
    arabanın satılıp satılmadığını tutmalıdır.Eğer araba satıldıysa 1 değerini,satılmadıysa
    0 değerini alacaktır.İkinci eleman ise birleşim tipinde tanımlanmalı ve eğer araba satıldıysa
    satış değeri,satılmadıysa arabanın markası tutulmalıdır.
    2-araba_A değişkenini araba yapı tipinende tanımlayınız.
    3-araba_A değişkenine satılmamış olan "Anadol" marka arabanın blgilerini atayınız.
    4-"Anadol" marka araba 20000 tl ye satılınca araba_A değişkeninde gereken
    güncellemeleri yapınız.
*/

    struct araba{

    int satis;
    union{
    double fiyat;
    char marka[20];
    }bilgi;

    };


    struct araba araba_A;


    araba_A.satis=0;
    strcpy(araba_A.bilgi.marka,"Anadol");


    araba_A.satis=1;
    araba_A.bilgi.fiyat=20000;

    return 0;
}
