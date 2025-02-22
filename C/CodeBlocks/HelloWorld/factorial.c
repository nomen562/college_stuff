#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("Enter Number: ");
    int number;
    scanf("%d", &number);

    // Factorial logic
    int product = 1;
    for (int i = 1; i <= number; i++)
        product *= i;

    printf("Factorial is: %d\n", product);
    return 0;
}
