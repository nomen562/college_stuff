
#include <stdio.h>

int (*fpComparer)(int, int);

int compare(int, int);

int main()
{
    int result;
    int a = 20, b = 30;

    fpComparer = &compare;

    result = (*fpComparer)(a, b);

    printf("Result: %d", result);

    return 0;
}

int compare(int x, int y)
{
    if (x > y)
        return 1;
    if (x < y)
        return -1;
    return 0;
}


