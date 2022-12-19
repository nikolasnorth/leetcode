package easy;

import java.util.Map;
import java.util.Objects;
import java.util.Stack;

// 20. Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/
public class Q0020 {

    // Time: O(n), Space: O(n), where n is the length of s.
    boolean isValid(String s) {
        var brackets = Map.of(
                '(', ')',
                '{', '}',
                '[', ']'
        );
        var open = new Stack<Character>();
        for (var c : s.toCharArray()) {
            if (brackets.containsKey(c)) {
                open.push(c);
                continue;
            }
            if (open.empty()) {
                return false;
            }
            var top = open.pop();
            if (!Objects.equals(c, brackets.get(top))) {
                return false;
            }
        }
        return open.empty();
    }
}
