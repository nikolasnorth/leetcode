package easy;

/**
 * 9. Palindrome Number
 * https://leetcode.com/problems/palindrome-number/
 */
class Q0009 {

  // O(n) time, O(1) space, where n is the number of digits in `x`
  public boolean isPalindrome(int x) {
    if (x < 0) {
      return false;
    }
    String xStr = Integer.toString(x);
    for (int i = 0; i < Math.floorDiv(xStr.length(), 2); i++) {
      if (xStr.charAt(i) != xStr.charAt(xStr.length() - 1 - i)) {
        return false;
      }
    }
    return true;
  }
}
