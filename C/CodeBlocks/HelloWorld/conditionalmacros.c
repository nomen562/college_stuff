#include <stdio.h>

//conditonal compilation
#ifdef macro_name
    // Code to be executed if macro_name is defined
#endif // macro_name
#ifndef macro_name
   // Code to be executed if macro_name is not defined
#endif // macro_name
#if constant_expr
    // Code to be executed if constant_expression is true
#elif another_constant_expr
    // Code to be excuted if another_constant_expression is true
#else
    // Code to be excuted if none of the above conditions are true
#endif

#define PI 3.14159

#define AREA(r) PI * r * r
 //You can use \ to printf in mutliple lines but in same line

#line 20 "file_name"
#define PrintLineNum
    printf("Line number is in file named %s",__FILE)
#warning "Pi is not defined"

#pragma message("Hello how are you guys doing")
int main()
{
    float area = AREA(3);
    printf("%.3f", AREA(4));
    printf("asdf\
    afadsfasdf");

    return 0;
}
