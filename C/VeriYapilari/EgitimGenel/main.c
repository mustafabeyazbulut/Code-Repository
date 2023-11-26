#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define degiskendefine 4

int main()
{
    int i=5;
    float f=4.55;
    char c='h';
    char cd[10];
    cd[0]='A';
    printf("%d %c %.2f %s\n",i,c,f,cd);

    printf("Lutfen Bir Sayi Giriniz :");//asdasdads
    scanf("%d",&i);
    printf("Girmis oldugunuz sayi:%d \n",i);

    int dizi[]={1,2,3,4,5,6,7};


    for (int i=0;i<sizeof (dizi)/sizeof (int);i++)
        printf("M %d\n",dizi[i]);

    //Matris Kullanýmý
    int matris[degiskendefine][3]={{1,2,3},{2,3,4},{3,4,5},{4,5,6}};
    int nrows = sizeof(matris) / sizeof(matris[0]);
    int ncols = sizeof(matris[0]) / sizeof(matris[0][0]);
    for (int i=0;i<nrows;i++){
            for (int j=0;j<ncols;j++){
                printf("%d ",matris[i][j]);
    }
    printf("\n");
    }//Matris Kullanýmý

    char can[100]="abcde";
    char canan[100];

    strcpy(canan,can);
    strncpy(canan,can,5);
    strcat(canan,"Merhaba");
    printf("%s",canan);
    tekmiciftmi(canan);

    return 0;
}
void tekmiciftmi(int canan){

}
