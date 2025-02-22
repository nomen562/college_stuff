#include <stdio.h>
#include <stdbool.h>

#define PI 3.14159

int main()
{
    int numberes[] = { 10, 29, 32 };
    unsigned a = 1;
    printf("");
    bool active = false,
         status = true;

    unsigned* ptr = &a;
    *ptr = 10;
    printf("%d", *ptr);
    char A = 'A';

    struct person
    {
        char firstName[25];
        char lastName[25];
        unsigned  age;
    };

    return 0;
}
