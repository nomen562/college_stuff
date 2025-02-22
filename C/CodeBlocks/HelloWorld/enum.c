#include <stdio.h>

int main()
{
    enum Bool {
    False, True
    };

    enum Bool var = False;

    enum Day {
    Sun, Mon, Tue, Wed, Thu, Fri, Sat
    };

    enum Day day = Fri;

    enum Point {
    X = 3,
    Y, Z
    } point;

    point = Y;
    printf("%d", point);

    int x = 4;
    point = (enum Point) x;

    return 0;
}

