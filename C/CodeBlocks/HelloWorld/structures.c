
#include <stdio.h>
#include <string.h>


int main()
{
    struct address
    {
        unsigned house_number;
        char street_name[100];
        char city[50];
        char state_name[30];
        int zip_code;
        char country[50];
    }  work_address;

    struct address friends_address;
    struct address home_address = { // We cant initialize this without declaring at the same time.
        3960,
        "North 1st Street",
        "San Jose",
        "CA",
        95134,
        "USA"
    };

    struct customer
    {
        char name[100];
        struct address shipping_address;
        struct address billing_address;
    } john;

    strcpy(john.shipping_address.city, "San Fransisco");

    size_t size = 0;


// another way to declare a struct wihout its name
//    struct
//    {
//        unsigned house_number;
//        char street_name[100];
//        char city_name[50];
//        char state_name[30];
//        int zip_code;
//        char country[50];
//    } home_address, work_address;



    return 0;
}
