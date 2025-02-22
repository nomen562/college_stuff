#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

long I_MAX = 1<<31;

int divide(int dividend, int divisor) {

    if (dividend == INT_MIN) {
        if (divisor == -1) return INT_MAX;  // Avoid overflow
        if (divisor == 1) return INT_MIN;
    }

    int sign = (dividend < 0) == (divisor < 0);    
    unsigned int a = abs(dividend);
    unsigned int b = abs(divisor);  
    unsigned long ans = 0;
    while(a >= b)
    { 
        short q = 0;
        while (a >= (b << (q + 1)))
        {
            q++;
        }
            
        ans += 1 << q;  // add the power of 2 found to the answer
        a -= b << q;  // reduce the dividend by divisor * power of 2 found
    }
    if(ans == I_MAX && sign > 0)   // if ans cannot be stored in signed int
        return INT_MAX;
    return sign ? ans : -ans;
}

int main()
{
    printf("%d", divide(-10, 2));
    return 0;
}
