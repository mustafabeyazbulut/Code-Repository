#include <stdio.h>
#include <stdlib.h>



union test
{
    int x,y;
};


int main()
{
    union test t;

    t.x=2;
    printf("%d\n",t.x);

    printf("Union imizin tuttugu alan %d byte tir\n",sizeof(t));

    t.y=10;
    printf("%d",t.y);
    return 0;
}
