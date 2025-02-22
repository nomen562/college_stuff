#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    int index;
    int value;
} Node;


int hash(const int* value, int numsSize)
{
    return abs(*value) % numsSize;

}


int getIndexToLookup(int value, Node* nodes, int numsSize)
{
    int hashValue = hash(&value, numsSize);
    int currentIndex = hashValue;

    for(int i = 0; i < numsSize; i++)
    {
        if (nodes[currentIndex].value == value && nodes[currentIndex].index != -1)
            return currentIndex;

        currentIndex = (currentIndex + 1) % numsSize;

    }

    return -1;
}


int getIndexToInsert(int value, Node* nodes, int numsSize)
{
    int hashValue = hash(&value, numsSize);
    int currentIndex = hashValue;

    for(int i = 0; i < numsSize; i++)
    {
        if (nodes[currentIndex].value == -1)
            return currentIndex;

        currentIndex = (currentIndex + 1) % numsSize;

    }

    return -1;
}


int* twoSum(int* nums, int numsSize, int target, int* returnSize)
{

    if (numsSize < 2)
    {
        *returnSize = 0;
        return NULL;
    }

    Node* nodes = (Node* )malloc(numsSize * sizeof(Node));
    int* answer = (int* )malloc(2 * sizeof(int));
    
    for (int i = 0; i < numsSize; i++)
    {
        nodes[i].index = -1;
        nodes[i].value = -1;
    }

    for (int i = 0; i <numsSize; i++)
    {
        int index = getIndexToInsert(nums[i], nodes, numsSize);
        nodes[index].index = i;
        nodes[index].value = nums[i];
    }

    for (int i = 0; i < numsSize; i++)
    {
        int index = getIndexToLookup(target - nums[i], nodes, numsSize);
        if (index != -1 && nodes[index].index != i)
        {
            answer[0] = i;
            answer[1] = nodes[index].index;
            *returnSize = 2;
            return answer;
        }

    }

    return NULL;
}

int main() {
    int nums[] = {2, 3, 3, 15};
    int target = 6;
    int returnSize;

    int* result = twoSum(nums, 4, target, &returnSize);

    if (returnSize == 2) {
        printf("Indices: %d, %d\n", result[0], result[1]);
        free(result);
    } else {
        printf("No solution found.\n");
    }

    return 0;
}