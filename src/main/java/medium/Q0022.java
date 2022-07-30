package medium;

import java.util.ArrayList;
import java.util.List;

/**
 * 22. Generate Parentheses
 * https://leetcode.com/problems/generate-parentheses/
 */
public class Q0022 {

    private int n;
    private List<String> result = new ArrayList<>();

    private void backtrack(int l, int r, String current) {
        if (l > n || r > n || r > l) return;
        if (l == n && r == n) this.result.add(current);
        backtrack(l + 1, r, current + '(');
        backtrack(l, r + 1, current + ')');
    }

    // Time: O(n 2^n), Space: O(nlog n).
    public List<String> generateParenthesis(int n) {
        this.n = n;
        backtrack(0, 0, "");
        return this.result;
    }
}
