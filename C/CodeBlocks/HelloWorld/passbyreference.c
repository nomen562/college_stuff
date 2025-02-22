#include <stdio.h>

void swap(int* a, int* b);

int main()
{
    int x = 10, y = 20;

    swap(&x, &y);

    printf("x = %d\n\
y = %d\n", x, y);

    return 0;
}

void swap(int* a, int* b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}


