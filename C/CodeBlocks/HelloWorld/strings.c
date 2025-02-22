#include <stdio.h>
#include <string.h>
// Why lol????
// strcat, strcpy, strlen, strcmp, fgets(name, sizeof(name), stdin), strcmp

int main()
{
    // "Hello" <- String literal
    char h[] = "Hello\0";

//    printf("%d", sizeof(h) / sizeof(char));

//    for (int i = 0; i < sizeof(h) / sizeof(char); i++)
//        printf("%c", h[i]);
//
//    printf("%s", h);
    char asd[5] = "12345";
    printf("%s", asd);
// if we give asd[5] or asd[6] rest of the elements are filled with null or \0 character



    char cs[] = {'a'};
    printf(" %s    ", cs);
// %s means prints the elements of the character array until you encounter \0

    printf("\n\n\n");

    char another[5];
    strcpy(another, "Helo");
    strcat(another, " World");
    printf("%s", another);

// reading from the stdin
    char name[5];
    fgets(name, sizeof(name), stdin);
    printf("%s", name);




    return 0;
}
