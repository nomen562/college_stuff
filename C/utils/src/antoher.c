#include <stdbool.h>
#include <stdio.h>
#include <string.h>

#define TABLE_SIZE 10
#define MAX_NAME 100

typedef struct
{
    char name[MAX_NAME];
    int age;
} Person;

Person* hash_table[TABLE_SIZE];
unsigned int size;

void init_hash_table();
void print_hash_table();
bool hash_table_insert(Person*);
int getIndexToInsert(const char*);
bool hash_table_remove(const char*);
int getIndexToLookup(const char*);
int hash(const char*);

int main()
{
    Person person1 = { .name = "Natalie", .age = 18 };
    Person person2 = { .name = "Sam", .age = 16 };
    Person person3 = { .name = "Rony", .age = 17 };
    Person person4 = { .name = "Datalie", .age = 18 };

    init_hash_table();

    

    hash_table_insert(&person1);
    hash_table_insert(&person4);

    print_hash_table();

    printf("Enter the name of the person to search: ");
    char givenName[MAX_NAME];
    scanf("%s",givenName);
    
    if (getIndexToLookup(givenName) == -1)
        printf("Name not found!\n");
    else
        printf("Name found at index %d\n", getIndexToLookup(givenName));

    printf("Enter name to delete: ");
    scanf("%s",givenName);
    hash_table_remove(givenName);
    print_hash_table();


}

void init_hash_table()
{
    size = 0;

    for(int i = 0; i < TABLE_SIZE; i++)
        hash_table[i] = NULL;
    
}

void print_hash_table()
{   
    printf("\n\tSTART\n");
    printf("-------------------------------------\n");

    for (int i = 0; i < TABLE_SIZE; i++)    
        if (hash_table[i] != NULL)
            printf("\t%i\t======>\t%s (Age is %d)\n", i, hash_table[i]->name, hash_table[i]->age);
        else
            printf("\t%i\t======>\tNULL\n", i);
    
    printf("-------------------------------------\n");
    printf("\n\tEND\n");

}

bool hash_table_insert(Person* person)
{
    if (size == TABLE_SIZE) return false;

    int index = getIndexToInsert(person->name);

    hash_table[index] = person;
    size++;
    return true;
        
}

bool hash_table_remove(const char* name)
{
    if (size == 0) return false;

    int index = getIndexToLookup(name);

    hash_table[index] = NULL;
    size--;

    printf("\nDeleted %s\n",name);

    return true;
        
} 

int getIndexToLookup(const char* name)
{
    int hashValue = hash(name);
    int currentIndex = hashValue % TABLE_SIZE;

    for(int i = 0; i < TABLE_SIZE; i++)
    {
        currentIndex = (currentIndex + i) % TABLE_SIZE;

        if (strcmp(hash_table[currentIndex]->name, name) == 0)
            return currentIndex;
    }

    return -1;
}

int getIndexToInsert(const char* name)
{
    int hashValue = hash(name);
    int currentIndex = hashValue % TABLE_SIZE;

    for(int i = 0; i < TABLE_SIZE; i++)
    {
        currentIndex = (currentIndex + i) % TABLE_SIZE;

        if (hash_table[currentIndex] == NULL)
            return currentIndex;
    }

    return hashValue % TABLE_SIZE;
}

int hash(const char* name)
{
    return strlen(name);
}