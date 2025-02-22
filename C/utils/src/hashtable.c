#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define MAX_NAME 256
#define TABLE_SIZE 10

typedef struct {
        char name[MAX_NAME];
        int age;
    } person;

person * hash_table[TABLE_SIZE];

unsigned hash(const char* name) 
{
    unsigned hash_value = 0;
    for (int i = 0; i < strnlen(name, MAX_NAME); i++)
    {
        hash_value += name[i];
        hash_value *= name[i]; 
    }

    return hash_value % TABLE_SIZE;
}

void init_hash_table()
{
    for (int i = 0; i < TABLE_SIZE; i++)
        hash_table[i] = NULL;
}

void print_table()
{   
    printf("\nSTART\n");

    for (int i = 0; i < TABLE_SIZE; i++)
        if (hash_table[i] != NULL)
            printf("\t%i\t======>\t%s\n", i, hash_table[i]->name);
        else
            printf("\t%i\t======>\t\n", i);
    
    printf("END\n");
}

bool hash_table_insert(const person *p)
{
    if (p == NULL) return false;

    int index = hash(p->name);
    if (hash_table[index] == NULL)
        hash_table[index] = p;
    else
        return false;

    return true;
}

bool hash_table_delete(const person* p)
{
    if (p == NULL) return false;

    int index = hash(p->name);
    if (hash_table[index] != NULL &&
        strncmp(p->name, hash_table[index]->name, TABLE_SIZE) == 0)
        {
            person* tmp = hash_table[index];
            hash_table[index] = NULL;
        }
    else
        return false;

    return true;
}

person* hash_table_lookup(const char* name)
{
    int index = hash(name);
    if (hash_table[index] != NULL &&
        strncmp(name, hash_table[index]->name, TABLE_SIZE) == 0)
        return hash_table[index];
    else
        return NULL;
}



int main()
{
    init_hash_table();
    print_table();

    person jacob = {.name = "Jacob", .age = 17};
    person mary = {.name = "Mary", .age = 16};

    hash_table_insert(&jacob);
    hash_table_insert(&mary);

    print_table();

    hash_table_delete(&jacob);
    printf("Is name found?\t===>\t%s", hash_table_lookup("Mary") ? "True" : "False");

    print_table();
    // printf("Natalie => %u\n", hash("Natalie"));
    // printf("Ron => %u\n", hash("Ron"));
    // printf("Bob => %u\n", hash("Natalie"));
    // printf("Natalie => %u\n", hash("Natalie"));

    return 0;
}