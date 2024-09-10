#include <stdio.h>
/* Program to convert celcius
   to fahrenheit using
   C=(5/9)*(F-32) */
#define LOWER 0
#define UPPER 300
#define STEP 20

int main() 
{
	
    float fahr, celcius;

    printf("Fahreneit to Celcius:\n----------------------\n"); 
    fahr = LOWER;
    while (fahr <= UPPER) {
    celcius = (5.0/9) * (fahr - 32);
    printf("%3.0f%6.1f\n", fahr, celcius);
    fahr = fahr + STEP;
    }    

    
    printf("Celcius to Farenheit:\n----------------------\n"); 
    celcius = fahr = 0;
    for (; celcius <= UPPER; celcius+=30) {
    fahr = (9/5.0) * celcius + 32;
    printf("%3.0f%6.1f\n", celcius, fahr);
    }

    printf("Reverse order F to C:\n----------------\n");
    celcius = 0;
    for (int fahr = 300; fahr >= 0; fahr-=20) 
	    printf("%3d%6.1f\n", fahr, (5.0/9.0)*(fahr-32));

}
