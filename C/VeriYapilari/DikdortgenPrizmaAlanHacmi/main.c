#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a,b,h,sonuc;
    printf("Lutfen a , b ve h degerlerini giriniz");
    scanf("%d%d%d",&a,&b,&h);
    char *tanim;
    for(int i=1;i<5;i++){
    switch(i){
        case 1:TabanAlani(a,b,&sonuc);tanim="Taban Alani"; break;
        case 2:YanalAlanToplami(a,b,h,&sonuc);tanim="Yanal Alani"; break;
        case 3:ToplamAlan(a,b,h,&sonuc);tanim="Toplam Alani"; break;
        case 4:Hacim(a,b,h,&sonuc);tanim="Hacim"; break;
            }
            printf("%s:%d\n",tanim,sonuc);
    }

    /*
    TabanAlani(a,b,&sonuc);
    printf ("Taban Alani :%d ",sonuc);

    YanalAlanToplami(a,b,h,&sonuc);
    printf ("Yanal Alani :%d ",sonuc);

    ToplamAlan(a,b,h,&sonuc);
    printf ("Toplam Alan :%d ",sonuc);

    Hacim(a,b,h,&sonuc);
    printf ("Hacim :%d ",sonuc);
    */
    return 0;
}
void ToplamAlan(int a, int b,int h, int *sonuc){
    *sonuc=2*(a*h)+2*(b*h)+2*a*b;
}
void Hacim(int a, int b,int h, int *sonuc){
    *sonuc=a*b*h;
}
void TabanAlani(int a, int b, int *sonuc){
    *sonuc=a*b;
}
void YanalAlanToplami(int a, int b,int h, int *sonuc){
    *sonuc=2*(a*h)+2*(b*h);
}
