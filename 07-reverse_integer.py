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
            return int(a[::-1]) if int(a[::-1]) < (1 << 31)-1 else 0

        elif MIN_32_bit_integer <= x < 0:
            return -(int(a[:-len(a):-1])) if -(int(a[:-len(a):-1])) > MIN_32_bit_integer else 0
        else:
            return 0