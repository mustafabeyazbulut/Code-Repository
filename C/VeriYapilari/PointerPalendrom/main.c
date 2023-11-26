
#include <stdio.h>
#include <stdlib.h>

int main()
{
    char cumle[100];
    char *p1,*p2;
    int kontrol;
    printf("Lutfen Maksimum 100 karakterli cumle giriniz :");
    gets(cumle);

    for(p2=cumle;*p2;p2++) printf("%c\n",*p2);//cümlede 0'a gelince for döngüsü for oluyor. 0ı silmek için p2-- yapıyoruz
    p2--;
    for(p1=cumle,kontrol=1;kontrol && p1<p2;p1++,p2--){
            printf("%c : %c \n",*p1,*p2);
            if(*p1!=*p2) kontrol=0;
    }

    if(kontrol) printf("Girilen Kelime %s, polindromdur.",cumle);
        else printf ("Girilen Kelime %s, polindrom degildir.",cumle);
    return 0;
}
