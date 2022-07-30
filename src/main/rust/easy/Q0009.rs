/// 9. Palindrome Number
/// https://leetcode.com/problems/palindrome-number/


/// Time: O(n), Space: O(n), where n is the number of digits in `x`.
pub fn is_palindrome(x: i32) -> bool {
    let x = x.to_string().into_bytes();
    let (mut lo, mut hi) = (0, x.len() - 1);
    while lo < hi {
        if x[lo] != x[hi] {
            return false;
        }
        lo += 1;
        hi -= 1;
    }
    true
}
