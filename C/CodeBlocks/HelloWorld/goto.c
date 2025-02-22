#include <stdio.h>

int main()
{
    int c = 0;
    here:

    if (c == 10)
        return 0;
    printf("1");
    printf("2");
    printf("3");
    printf("\n");
    c++;

    goto here;

    return 0;
}
