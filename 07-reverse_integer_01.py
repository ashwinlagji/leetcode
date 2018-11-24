# Optimized
# Runtime: 56 ms, faster than 78.84% of Python3 online submissions for Reverse Integer.

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = str(x)
        MAX_32_bit_integer = (1 << 31)-1
        MIN_32_bit_integer = (-1 << 31)
        if 0 < x <= MAX_32_bit_integer:            
            rev = int(a[::-1])            
            return rev if rev < (1 << 31)-1 else 0

        elif MIN_32_bit_integer <= x < 0:
            rev = -(int(a[:-len(a):-1]))            
            return rev if rev > MIN_32_bit_integer else 0
        else:
            return 0