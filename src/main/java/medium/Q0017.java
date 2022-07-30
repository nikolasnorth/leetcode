package medium;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * 17. Letter Combinations of a Phone Number
 * https://leetcode.com/problems/letter-combinations-of-a-phone-number/
 */
public class Q0017 {

    private Map<Character, String> digitLetters = new HashMap<>(Map.of(
            '2', "abc",
            '3', "def",
            '4', "ghi",
            '5', "jkl",
            '6', "mno",
            '7', "pqrs",
            '8', "tuv",
            '9', "wxyz"
    ));
    private List<String> result = new ArrayList<>();
    private String digits;

    private void backtrack(int i, String s) {
        if (s.length() == this.digits.length()) {
            this.result.add(s);
            return;
        }
        var digit = this.digits.charAt(i);
        for (var c : this.digitLetters.get(digit).toCharArray()) {
            backtrack(i + 1, s + c);
        }
    }

    // Time: O(n 4^n), Space: O(n log n), where n is the length of `digits`.
    private List<String> letterCombinations(String digits) {
        this.digits = digits;
        if (!digits.isEmpty()) {
            backtrack(0, new String());
        }
        return this.result;
    }
}
