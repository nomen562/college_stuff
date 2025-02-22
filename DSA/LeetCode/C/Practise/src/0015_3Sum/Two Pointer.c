#include <stdlib.h>
#include <stdio.h>

typedef struct
{
    int index;
    int value;
} Node;

static int comparator(const void* a, const void* b)
{
    const Node* node1 = (const Node*)a;
    const Node* node2 = (const Node*)b;

    int arg1 = node1->value;
    int arg2 = node2->value;

    return (arg1 > arg2) - (arg1 < arg2);
}


int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes)
{   
    if (nums == NULL || numsSize < 3)
    {
        *returnSize = 0;
        return NULL;
    }

    Node* nodes = (Node* )malloc(numsSize * sizeof(Node));
    for(int i = 0; i < numsSize; i++)
    {
        nodes[i].index = i;
        nodes[i].value = nums[i];
    }

    qsort(nodes, numsSize, sizeof(Node), comparator);

    int** result = (int**)malloc(100000 * sizeof(int));
    *returnColumnSizes = (int*)malloc(100000 * sizeof(int));
    *returnSize = 0;
    int left = 1;
    int right = numsSize - 1;

    for (int i = 0; i < numsSize - 2; i++)
    {   
        if (i > 0 && nodes[i].value == nodes[i - 1].value) continue;

        left = i + 1;
        right = numsSize - 1;
        while(left < right)
        {
            int sum = nodes[left].value + nodes[right].value + nodes[i].value;
            if (sum == 0)
            {
                while (left < right && nodes[left].value == nodes[left + 1].value)
                left++;
                while (left < right && nodes[right].value == nodes[right - 1].value)
                right--;
                
                result[*returnSize] = (int*)malloc(3 * sizeof(int)); 
                result[*returnSize][0] = nodes[i].index;
                result[*returnSize][1] = nodes[left].index;
                result[*returnSize][2] = nodes[right].index;
                (*returnSize)++;

            }
               
            else if (sum < 0)
                left++;
            else 
                right--;
        }
    }

    return result;
    
}

int main()
{
    
    
    return 0;
}