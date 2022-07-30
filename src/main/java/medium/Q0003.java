package medium;

import java.util.HashSet;
import java.util.Set;

/**
 * 3. Longest Substring Without Repeating Characters
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/
 */
class Q0003 {

  // O(n) time, O(n) space, where n is the length of `s`
  // Note: Java's HashSet.contains() and HashSet.remove() are O(1). Calling Object.hashCode() on all the possible ASCII
  // characters in `s` will lead to ~uniform distribution in the underlying hash table.
  int lengthOfLongestSubstring(String s) {
    int max = 0, start = 0;
    Set<Character> visited = new HashSet<>();
    for (int end = 0; end < s.length(); end++) {
      while (visited.contains(s.charAt(end))) {
        visited.remove(s.charAt(start));
        start++;
      }
      visited.add(s.charAt(end));
      max = Math.max(max, visited.size());
    }
    return max;
  }
}
