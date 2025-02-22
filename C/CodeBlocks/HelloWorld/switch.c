#include <stdio.h>

int main()
{
    switch (1) {
    case 1:
    printf("Asd");
    break;

    case 2:
    printf("32423");
    break;
    }

    #include <stdio.h>

int main()
{
    // prompt for a weekday number
    int day;
    printf("Enter a day (1-7): ");
    scanf("%d", &day);

    // display the weekend or working day
    switch (day)
    {
        case 1:
        case 7:
            printf("It's weekend!\n");
            break;
        case 2:
        case 3:
        case 4:
        case 5:
        case 6:
            printf("It's a working day.\n");
            break;
        default:
            printf("Please enter a valid weekday number.\n");
    }
    return 0;
}

    return 0;
}
