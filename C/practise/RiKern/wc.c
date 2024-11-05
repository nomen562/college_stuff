#include <stdio.h>

#define IN 1
#define OUT 0

int main()
{
    int c;
    int cc,wc,lc;
    
    cc = wc = lc = 0;
    int state = OUT;
    int pstate = OUT;
    
    while ((c = getchar()) != EOF) {
        cc++;
        if (c == '\n') lc++;
        if (c == '\n' || c == '\t' || c == ' ') {
            pstate = state;
            state = OUT;
            
        }
        
        else {
            pstate = state;
            state = IN;
        }
        
        if (pstate == IN && state == OUT) wc++;
            
    }
    printf("%d", wc);
}
