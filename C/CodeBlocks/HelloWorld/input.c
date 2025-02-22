#include <stdio.h>
#include <string.h>

int main()
{
    char message[100];

    message[0] = 'H';
    message[1] = 'e';
    message[2] = 'l';
    message[3] = 'l';
    message[4] = '\n';

    printf("Message: ");
    fgets(message, sizeof(message), stdin);

    for (int i = 0; i < strlen(message); i++)
    {
        if (message[i] == '\0')
            printf("message[%d] = NULL", i);

        else if(message[i] == '\n')
            printf("message[%d] = New line\n", i);

        else
            printf("message[%d] = %c\n", i, message[i]);
    }

    // length is till before the first null \0 character is encountered
    printf("%ld\n", strlen(message));

    message[strlen(message) - 1] = '\0'; // last character becomes null
    printf("%s", message);

    return 0;
}
