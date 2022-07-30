package easy;

import java.util.Objects;

/**
 * 28. Implement strStr()
 * https://leetcode.com/problems/implement-strstr/
 */
class Q0028 {

  // O(n^2) time, O(n) space, where n is the length of haystack
  int strStr(String haystack, String needle) {
    if (needle.isEmpty()) {
      return 0;
    }
    for (int i = 0; i < haystack.length() - needle.length() + 1; i++) {
      if (Objects.equals(haystack.substring(i, i + needle.length()), needle)) {  // .substring() is O(n) in time and space as of Java 7u6
        return i;
      }
    }
    return -1;
  }
}
