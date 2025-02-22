#include <stdio.h>

int main()
{
//    typedef struct
//    {
//    ...
//    } address
//
//    or this for declaration
//
//    typedef struct address
//    {
//    ...
//    }

struct Person
{
    unsigned int house_number;
    char street[120];
    char city[50];
    char state[3];
    int zip_code;
    char country[50];
} ;

struct Person preson = {
        3960,
        "North 1st Street",
        "San Jose",
        "CA",
        95134,
        "USA"
};
// or this

// Person = (typeof(Person))
// {
//        3960,
//        "North 1st Street",
//        "San Jose",
//        "CA",
//        95134,
//        "USA"
//};

struct
{
    unsigned int house_number;
    char street[120];
    char city[50];
    char state[3];
    int zip_code;
    char country[50];
} employee;

employee = (typeof(employee)){
        3960,
        "North 1st Street",
        "San Jose",
        "CA",
        95134,
        "USA"
};


typedef struct we // here the identifier we is not reequired and should not be placed with typedef
{
    unsigned int house_number;
    char street[120];
    char city[50];
    char state[3];
    int zip_code;
    char country[50];
} neww;

neww sdafsdf = {
        3960,
        "North 1st Street",
        "San Jose",
        "CA",
        95134,
        "USA"
};


typedef struct {
char name[50];

} Person;


Person person;
strcpy(person.name, "Hello World!");



    return 0;
}
