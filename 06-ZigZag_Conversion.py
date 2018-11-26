# optimized solution

# Runtime: 60 ms, faster than 82.99% of Python online submissions for ZigZag Conversion.

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        output = [''] * numRows
        if len(s)==1 or numRows ==1:
            return s
        for i in range(len(s)):
            parse_string_len = 2*numRows -2
            if(i%parse_string_len < numRows):
                output[i%parse_string_len] += (s[i]) 
            else:
                output[parse_string_len-(i%parse_string_len)] += (s[i])
        return "".join(output)

obj = Solution()

print (obj.convert("PAYPALISHIRING",5))