#include <stdio.h>

int main()
{
    char ch = 65;
    printf("%c", ch);
    printf("\n%c", 48);

    typedef enum {
    false = 0, true = 1
    } bool;

    bool a = true;
    printf("%c", a);

    return 0;
}

