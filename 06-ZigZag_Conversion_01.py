# Optimized
# Runtime: 48 ms, faster than 99.94% of Python online submissions for ZigZag Conversion.

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        
        index = 0
        step = 1
        
        L = [''] * numRows
        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            if index == numRows - 1:
                step = -1
            
            index += step
        
        return ''.join(L)