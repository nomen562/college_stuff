#include <stdio.h>

//#define MACRO_TEMPLATE MACRO_Expansion
#define LIMIT 5

//Macros with argumentns/parameters
#define func(l, b) l * b

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

int main()
{


    return 0;
}
