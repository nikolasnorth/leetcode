package easy;

import java.util.Arrays;
import java.util.Objects;

/**
 * 242. Valid Anagram
 * https://leetcode.com/problems/valid-anagram/
 */
public class Q0242 {

    // Time: O(nlog n), Space: O(n)
    private boolean isAnagram(String s, String t) {
        var sChars = s.toCharArray();
        var tChars = t.toCharArray();
        Arrays.sort(sChars);
        Arrays.sort(tChars);
        s = new String(sChars);
        t = new String(tChars);
        return Objects.equals(s, t);
    }
}
