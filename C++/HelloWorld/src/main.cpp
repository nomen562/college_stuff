#include <climits>
#include <cstddef>
#include <ios>
#include <iostream>
#include <iterator>
#include <limits>

using namespace std;

int find(int array[], int size, int target) {
    
    for (int i = 0; i < size; i++) 
        if (array[i] == target)
            return i;

    return -1;

}

int main() {
    int numbers[] { 10, 20 , 30};
    cout << find(numbers, size(numbers), 20);
    
}

