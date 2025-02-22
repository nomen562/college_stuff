#include <stdio.h>

int main()
{
    int arr[3] = {1, 2};

    for (int i = 0; i < sizeof(arr) / sizeof(int); i++)
        printf("%2d", arr[i]);

    return 0;
}
