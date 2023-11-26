void dinamik_matris_olustur(int ***dizi, int satir, int sutun){
    int i,j;
    *dizi=(int**)malloc(satir*sizeof(int*));
    for(i=0; i<satir; i++){
        *(*dizi+i)= (int*)malloc(sutun*sizeof(int));
        for(j=0; j<sutun; j++)
            *(*(*dizi+i)+j)= rand()%100;
    }

}

int main(int argc, char** argv) {
int **A;

dinamik_matris_olustur(&A, 10, 15);

}
