#include <stdio.h>

int main()
{
    int arr[] = {9, 8, 7, 6, 5, 4};
    int size = 6;

    for (int i = 1; i < size; i++)
    {
        int elementToPlace = arr[i];
        int j = i - 1;

        while (j >= 0 && elementToPlace < arr[j])
        {
            arr[j + 1] = arr[j];
            j--;
        }

        arr[j + 1] = elementToPlace; 
    }

    for(int i = 0; i < size; i++)
        printf("%d\n", arr[i]);

    return 0;

}