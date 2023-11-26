#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct{
float xekseni;
float yekseni;
}nokta;


int main()
{
    nokta mustafa;

    mustafa.xekseni=3;
    mustafa.yekseni=2;

    printf("X eksenimiz %.2f Y eksenimiz %.2f \n",mustafa.xekseni,mustafa.yekseni);
    return 0;
}
