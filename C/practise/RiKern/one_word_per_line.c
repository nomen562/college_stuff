#include <stdio.h>

#define IN 1
#define OUT 0

//1-12
int main() 
{
    int c;
    int state, pstate;
    state = pstate = OUT;
    
    while ((c = getchar()) != EOF) {
        if (c == ' ' || c == '\t' || c == '\n') {
            pstate = state;
            state = OUT;
        }
        else {
            pstate = state;
            state = IN;
        }
        if (pstate == OUT && state == IN || pstate == IN && state == IN )
            putchar(c);
        else
            printf("\n");
    }
    
}
