#include <stdio.h>
#include <stdlib.h>

void dinamik_matris_olustur(int ***dizi, int satir, int sutun){
    int i,j;
    *dizi=(int**)malloc(satir*sizeof(int*));
    for(i=0; i<satir; i++){
        *(*dizi+i)= (int*)malloc(sutun*sizeof(int));
        for(j=0; j<sutun; j++)
            *(*(*dizi+i)+j)= rand()%100;
    }
}
int main() {
int **A;
dinamik_matris_olustur(&A, 10, 15);

matris_geri_ver(&A,10);
}

void matris_geri_ver(int ***matris, int satir){

    for (int i=0;i<satir;i++)
    {
    free((void*)*(*matris+i));
    }
    free((void*)(*matris));
    printf("matris temizleme basarili ");
}
void matris_geri_ver_lan(int ***matris, int satir){
 	int i = 0;
    	for (i = 0; i < satir; i++)
        		free(*(*matris + i));
    	free(*matris);
    	printf("matris temizleme basarili %d",sizeof(*matris));
}

