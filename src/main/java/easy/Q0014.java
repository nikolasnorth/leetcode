package easy;

/**
 * 14. Longest Common Prefix
 * https://leetcode.com/problems/longest-common-prefix/
 */
class Q0014 {

  // O(mn^2) time, O(1) space, where n is the number of characters in `strs[0]` and m is the length of `strs`
  String longestCommonPrefix1(String[] strs) {
    String result = "";
    for (int i = 0; i < strs[0].length(); i++) {
      String query = result + strs[0].charAt(i);
      for (String str : strs) {
        if (!str.startsWith(query)) {  // startsWith() is O(n)
          return result;
        }
      }
      result = query;
    }
    return result;
  }

  // O(mn) time, O(1) space, where n is the number of characters in `strs[0]` and m is the length of `strs`
  String longestCommonPrefix2(String[] strs) {
    StringBuilder result = new StringBuilder();
    for (int i = 0; i < strs[0].length(); i++) {
      for (String str : strs) {
        if (i == str.length() || strs[0].charAt(i) != str.charAt(i)) {
          return result.toString();
        }
      }
      result.append(strs[0].charAt(i));
    }
    return result.toString();
  }
}
