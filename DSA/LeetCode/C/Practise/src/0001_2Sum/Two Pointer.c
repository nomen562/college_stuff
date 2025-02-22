#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    int value;
    int index;
} Node;

static int comparator(const void* a, const void* b)
{
    const Node* node1 = (const Node*)a;
    const Node* node2 = (const Node*)b;

    int arg1 = node1->value;
    int arg2 = node2->value;

    return (arg1 > arg2) - (arg1 < arg2);
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize)
{
    Node* nodes = (Node* )malloc(numsSize * sizeof(Node));
    if (!nodes) {
        *returnSize = 0;
        return NULL; 
    }

    for(int i = 0; i < numsSize; i++)
    {
        nodes[i].index = i;
        nodes[i].value = nums[i];
    }

    qsort(nodes, numsSize, sizeof(*nodes), comparator);

    int* results = (int *)malloc(2 * sizeof(int));
    int i = 0;
    int j = numsSize - 1;

    while (i < j)
    {
        int sum = nodes[i].value + nodes[j].value;

        if (sum < target)
            i++;
        else if (sum > target)
            j--;
        else
        {
            results[0] = nodes[i].index;
            results[1] = nodes[j].index;
            *returnSize = 2;

            free(nodes);
            return results;
        }
    }

    *returnSize = 0;
    free(nodes);
    free(results);
    return NULL;
}

int main()
{
    
}