#include <iostream> // one of the file in the standard c++ library responsible for inputoutput
#include <cmath>
#include <iomanip>

using namespace std;

int main()
{
    int arr[100] {0};
    for (int i = 0; i < sizeof(arr) / sizeof(arr[0]); i++)
    {
        printf("%d ", i);
    }
}