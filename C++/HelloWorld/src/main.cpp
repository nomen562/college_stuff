#include <iostream>

using namespace std;

int main()
{
    int numbers[] = { 1, 2, 3 };

    for (int i = 0; i < sizeof(numbers) / sizeof(int); i++)
        cout << numbers[i] << " ";
}