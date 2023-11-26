#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x=1,y=1,r=1;
    printf("Usslu sayi hesaplamaya hos geldiniz!\n");

    while(x!=0 || y!=0){
    printf("Ussu alinacak sayiyi giriniz!\n");
    scanf("%d",&x);
    if(x==0) break;
    printf("Sayininn Ussunu giriniz!\n");
    scanf("%d",&y);
    if(y==0) break;
    UstunuAl(x,y,&r);
    printf("%d \n",r);
    }

}
void UstunuAl(int x, int y, int *r){
    int i;
    for (i=0;i<y;i++){
        *r=*r*x;
}
}
