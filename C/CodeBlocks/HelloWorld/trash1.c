#include <stdio.h>
#include <limits.h>

int main()
{
    struct name
    {
        int s;
    };

    enum STATUS
    {
        open = 1,
        closed = 3
    };

    enum STATUS
    {
        open = 1,
        drive = 3;
    };

    printf("(%d, %d)", INT_MIN, INT_MAX);
    unsigned asdf = -12;
    printf("%d", asdf);
}
