package com.codewithmosh.generics;

public class User implements Comparable<User> /* for comparing two user onjects*/{
/* if we dont write <User> then the type of the parameter will be object
 * then instead of comparing with another user object we will compare with 
 * another instance of the object class
 * then we will have to do an explicit cast here and then it possible to get a 
 * casting exception at runtime so this approach is unsafe
 */
private int points;

public User(int points) {
    this.points = points;
}


    @Override
    public int compareTo(User otherUser) {
        // this < o -> -1 any negative value
        // this == o -> 0
        // this > o -> 1

        // if (points < o.points)
        //     return -1;

        // if (points > o.points)
        //     return 1;

        // return 0;

        return points - otherUser.points;

    }

    @Override // tell the java compiler that we are overriding one of the method
              // inherited from the base class
    public String toString() {
            return "Points = " + points;
    }
    
}
