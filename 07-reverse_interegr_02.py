class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x == 0:
            return 0
        
        s = str(x)
        
        if s[0] is not '-':
            n = int(''.join(reversed(s)))
        else:
            n = -int(''.join(reversed(s[1:])))

#         n = 0        
#         while x > 0:
#             r = x % 10
#             n = (n * 10) + r
#             x //= 10
        
        return n if -2**31 <= n <= 2**31-1 else 0