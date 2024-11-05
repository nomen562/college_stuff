#include <stdio.h>
int main() 
{
    int c;
    int bc;
    
    while ((c = getchar()) != EOF) {
        if (c == ' ')
        bc++;
        else {
            if (bc > 0) {
              putchar(' ');
              bc = 0;
            }
            else  putchar(c);
            
        }
    }
        
}
