#include <stdio.h>

int fibonacci(int number); // Function prototype declaration

int main()
{
    int number;
    printf("Enter the number: ");
    scanf("%d", &number);

    // Print the Fibonacci sequence up to the nth number
    printf("Fibonacci Sequence up to %d:\n", number);
    for (int i = 0; i <= number; i++) {
        printf("%d ", fibonacci(i));
    }
    printf("\n");

    return 0;
}

int fibonacci(int number)
{

    return (number <= 1) ? 
    number : 
    fibonacci(number - 1) + fibonacci(number - 2);
}
