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
    return (node1->value > node2->value) - (node1->value < node2->value);
}

int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes)
{   
    if (nums == NULL || numsSize < 3)
    {
        *returnSize = 0;
        return NULL;
    }

    Node* nodes = (Node*)malloc(numsSize * sizeof(Node));
    for(int i = 0; i < numsSize; i++)
    {
        nodes[i].index = i;
        nodes[i].value = nums[i];
    }

    qsort(nodes, numsSize, sizeof(Node), comparator);

    int** result = (int**)malloc(1000 * sizeof(int*));
    *returnColumnSizes = (int*)malloc(1000 * sizeof(int));
    *returnSize = 0;

    for (int i = 0; i < numsSize - 2; i++)
    {   
        if (i > 0 && nodes[i].value == nodes[i - 1].value) continue;

        int left = i + 1, right = numsSize - 1;
        while(left < right)
        {
            int sum = nodes[i].value + nodes[left].value + nodes[right].value;
            if (sum == 0)
            {
                result[*returnSize] = (int*)malloc(3 * sizeof(int)); 
                result[*returnSize][0] = nodes[i].value;
                result[*returnSize][1] = nodes[left].value;
                result[*returnSize][2] = nodes[right].value;
                (*returnColumnSizes)[*returnSize] = 3;
                (*returnSize)++;

                // Skip duplicates
                while (left < right && nodes[left].value == nodes[left + 1].value) left++;
                while (left < right && nodes[right].value == nodes[right - 1].value) right--;
                
                left++;
                right--;
            }
            else if (sum < 0)
                left++;
            else 
                right--;
        }
    }

    free(nodes);
    return result;
}


    int main()
    {

        int elements[] = {1, 2, 3, 4, 5, 6};
        int size = 6;
        int data = 3;
        qsort(elements, size, sizeof(int), comparator_int);

        int index = binary_search(elements, size, data);
        printf("index is %d", index);

        return 0;
    }
