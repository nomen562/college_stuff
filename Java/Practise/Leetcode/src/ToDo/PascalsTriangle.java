/* 
 * 118. Pascal's Triangle
 * 
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers
directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]
 */

import java.util.ArrayList;
import java.util.List;

public class PascalsTriangle {
    public static void main(String[] args) {
        System.out.println(new Solution().generate(5));
    }
}

class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<>();
        res.add(List.of(1));

        for (int i = 0; i < numRows - 1; i++) {
            List<Integer> dummyRow = new ArrayList<>();
            dummyRow.add(0);
            dummyRow.addAll(res.get(i));
            dummyRow.add(0);

            System.out.println(dummyRow);

            List<Integer> newRow = new ArrayList<>();
            for (int j = 0; j < dummyRow.size() - 1; j++) {
                newRow.add(dummyRow.get(j) + dummyRow.get(j + 1));
            }

            res.add(newRow);
        }

        return res;
    }
}