# unoptimized
# Runtime: 148 ms, faster than 79.70% of Python online submissions for Palindrome Number.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x<0:
            return False
        
        rev = 0
        temp = x
        
        while temp > 0:
            rev = rev*10 + temp%10
            temp //= 10
        
        if rev == x:
            return True
        else:
            return False