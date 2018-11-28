# Invalid
# if we are allowed to convert into string and use string reverse
# Runtime: 128 ms, faster than 79.70% of Python online submissions for Palindrome Number.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if str(x) == str(x)[::-1]:
            return True
        return False