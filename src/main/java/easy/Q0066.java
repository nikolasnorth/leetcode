package easy;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

/**
 * 66. Plus One
 * https://leetcode.com/problems/plus-one/
 */
class Q0066 {

  // O(n) time, O(n) space, where n is the size of digits
  int[] plusOne1(int[] digits) {
    if (digits[digits.length - 1] < 9) {
      digits[digits.length - 1] += 1;
      return digits;
    }
    // Convert array to a list
    List<Integer> digitsList = Arrays.stream(digits).boxed().collect(Collectors.toList());
    int i = digitsList.size() - 1;
    while (digitsList.get(i).equals(9)) {
      digitsList.set(i, 0);
      i--;
      if (i == -1) {
        digitsList.add(0, 1);
        // Reverse list back to original order and return as int[]
        return digitsList.stream().mapToInt(val -> val).toArray();
      }
    }
    digitsList.set(i, digitsList.get(i) + 1);
    // Reverse list back to original order and return as int[]
    return digitsList.stream().mapToInt(val -> val).toArray();
  }

  // O(n) time, O(n) space, where n is the size of digits
  int[] plusOne2(int[] digits) {
    if (digits[digits.length - 1] < 9) {
      digits[digits.length - 1] += 1;
      return digits;
    }
    // Convert array to a list and reverse order
    List<Integer> digitsList = Arrays.stream(digits).boxed().collect(Collectors.toList());
    Collections.reverse(digitsList);  // O(n)
    int i = 0;
    while (digitsList.get(i).equals(9)) {
      digitsList.set(i, 0);
      i++;
      if (i == digitsList.size()) {
        digitsList.add(1);
        // Reverse list back to original order and return as int[]
        Collections.reverse(digitsList);
        return digitsList.stream().mapToInt(val -> val).toArray();
      }
    }
    digitsList.set(i, digitsList.get(i) + 1);
    // Reverse list back to original order and return as int[]
    Collections.reverse(digitsList);
    return digitsList.stream().mapToInt(val -> val).toArray();
  }
}
