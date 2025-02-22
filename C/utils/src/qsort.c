#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int comparator_int(const void*, const void*);

int main()
{   
    int arr[] = {12, 13, 51, -12, 0, INT_MIN};
    int numberOfElements = sizeof(arr) / sizeof(int);
    const int sizeOfElement = sizeof(int);

    qsort(arr, numberOfElements, sizeOfElement, comparator_int);

    for (int i = 0; i < numberOfElements; i++)
        printf("%d ", arr[i]);

    return 0;
}

int comparator_int(const void* a, const void* b)
{   
    int arg1 = *(const int*)a;
    int arg2 = *(const int*)b;

    return (arg1 > arg2) - (arg1 < arg2);
}

