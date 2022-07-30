package easy;

import java.util.Map;
import java.util.Set;

/**
 * 13. Roman to Integer
 * https://leetcode.com/problems/roman-to-integer/
 */
class Q0013 {

  // O(n) time, O(n) space, where n is the number of chars in `s`
  int romanToInt1(String s) {
    int result = 0;
    char[] romanChars = s.toCharArray();
    for (int i = 0; i < romanChars.length; i++) {
      switch (romanChars[i]) {
        case 'I':
          if (i + 1 < romanChars.length && Set.of('V', 'X').contains(romanChars[i + 1])) {
            result -= 1;
          } else {
            result += 1;
          }
          break;
        case 'V':
          result += 5;
          break;
        case 'X':
          if (i + 1 < romanChars.length && Set.of('L', 'C').contains(romanChars[i + 1])) {
            result -= 10;
          } else {
            result += 10;
          }
          break;
        case 'L':
          result += 50;
          break;
        case 'C':
          if (i + 1 < romanChars.length && Set.of('D', 'M').contains(romanChars[i + 1])) {
            result -= 100;
          } else {
            result += 100;
          }
          break;
        case 'D':
          result += 500;
          break;
        case 'M':
          result += 1000;
          break;
      }
    }
    return result;
  }

  // O(n) time, O(1) space, where n is the number of characters in `s`
  int romanToInt2(String s) {
    Map<Character, Integer> charValues = Map.of(
      'I', 1,
      'V', 5,
      'X', 10,
      'L', 50,
      'C', 100,
      'D', 500,
      'M', 1000
    );
    int result = 0;
    for (int i = 0; i < s.length(); i++) {
      if (i + 1 < s.length() && charValues.get(s.charAt(i)) < charValues.get(s.charAt(i + 1))) {
        result -= charValues.get(s.charAt(i));
      } else {
        result += charValues.get(s.charAt(i));
      }
    }
    return result;
  }
}
