package easy;

/**
 * 58. Length of Last Word
 * https://leetcode.com/problems/length-of-last-word/
 */
class Q0058 {

  // O(n) time, O(n) space, where n is the length of `s`
  int lengthOfLastWord1(String s) {
    String[] words = s.split("\\s+");  // I believe String.split() in this case is O(n)
    return words[words.length - 1].length();
  }

  // O(n) time, O(1) space, where n is the length of `s`
  int lengthOfLastWord2(String s) {
    int i = s.length() - 1;
    while (i > -1 && s.charAt(i) == ' ') {
      i--;
    }
    int len = 0;
    while (i > -1 && s.charAt(i) != ' ') {
      i--;
      len++;
    }
    return len;
  }
}
