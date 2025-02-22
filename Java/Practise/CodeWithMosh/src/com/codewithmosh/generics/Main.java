package com.codewithmosh.generics;

public class Main {
    public static void main(String[] args) {
        GenericList<Integer> genericList = new GenericList</*Integer here is redundant */>();
        var user1 = new User(10);
        var user2 = new User(20);
        // in java we cannot write if user1 < user2 as we can only 
        // compare numbers and characters. We use compareTo to 
        // compare to comparable objects

        if (user1.compareTo(user2) < 0)
            System.out.println("user1 < user2");
        else if (user1.compareTo(user2) > 0)
            System.out.println("user1 > user2");
        else
            System.out.println("user1 == user 2");


        var max = Utils.max("q", "a");
        var maxx = Utils.max(new User(10), new User(20));
        System.out.println(max);
        System.out.println(maxx);
        Utils.print(1, "a");
        // the long string we see is because of the .toString implementation
        // in .toString method of User class (inherited from object)
        // so we can override that method
        
        User user = new Instructor(10);
        Utils.printUser(user);
        //  What if we expected a list of users here
        var instructors = new GenericList<Instructor>();
        // Utils.printUsers(instructors); <- we cant do this
        // Here a generic list of Instructor is not a subtype of a generic list of Users
        var users = new GenericList<User>();
        // Now we should iterate through all instructor in instructors and add them to users
        Utils.printUsers(users);
        // But this is very tedious
        // We can solve this problem using wildcards
        // 
















        // var list = new List(10);
        // list.add(Integer.valueOf(10));
        // list.add("10");
        // list.add(new User());
        // int value = (int) list.get(1);
        // System.out.println(value);
    }
}
