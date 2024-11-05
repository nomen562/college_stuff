#include <stdio.h>

#define MAXLINE 50000  // Maximum characters in a line

int metline(char[]);

int main()
{
    int len;
    int max;
    char line[MAXLINE];
    char longest[MAXLINE];

    max = 0;
    while ((len = metline(line)) > 0)
    {
        if (len > max)
        {
            max = len;
            for (int i = 0; i < max; i++)
                longest[i] = line[i];
            longest[max] = '\0';  // Null-terminate the longest line
        }
    }

    if (max > 0) {
        printf("Longest line: %s\n", longest);
    }

    return 0;
}

int metline(char s[])
{
    int c, i = 0;

    while ((c = getchar()) != EOF && c != '\n' && i < MAXLINE - 1)
    {
        s[i] = c;
        i++;
    }
    if (c == '\n') {
        s[i] = c;
        i++;
    }
    s[i] = '\0';  // Null-terminate the string

    return i;
}

