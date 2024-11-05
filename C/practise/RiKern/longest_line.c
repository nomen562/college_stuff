#include<stdio.h>

#define MAXLINE 50000 //maximum characters in a line

int metline(char[]);
int main() 
{
    int len;
    int max;
    char line[MAXLINE];
    char longest[MAXLINE];
    
    max = 0;
    while ((len = metline(line)) > 0) 
        if (len > max) {
            max = len;
            for (int i = 0; i < max; i++)
                longest[i] = line[i];   
        }
    if (max > 0)
	printf("Longest line is %s\n", longest);    
    
}

int metline(char s[])
{
    int c;
    int i;
    
    i = 0;
    
    while ((c = getchar()) != EOF && c != '\n' && i != MAXLINE) {
        s[i] = c;
        i++;
    }
    if (c == '\n')
        s[i] = c;
        
    return i+1;
}

