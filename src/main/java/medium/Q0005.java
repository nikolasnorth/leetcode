package medium;

/**
 * 5. Longest Palindromic Substring
 * https://leetcode.com/problems/longest-palindromic-substring/
 */
class Q0005 {

  String findLongest(int l, int r, String s, String longest) {
    while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
      if (s.substring(l, r + 1).length() > longest.length()) {
        longest = s.substring(l, r + 1);
      }
      l--;
      r++;
    }
    return longest;
  }

  // O(n^2) time, O(n) space, where n is the length of `s`
  String longestPalindrome(String s) {
    String longest = "";
    for (int i = 0; i < s.length(); i++) {
      // Check odd length palindromes
      longest = findLongest(i, i, s, longest);
      // Check even length palindromes
      longest = findLongest(i, i + 1, s, longest);
    }
    return longest;
  }
}
