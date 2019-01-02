# Unoptimized
# Runtime: 100 ms, faster than 52.23% of Python online submissions for Roman to Integer.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        interger_roman = {
            'I':1,
            'IV':4,
            'V':5,
            'IX':9,
            'X':10,
            'XL':40,
            'L':50,
            'XC':90,
            'C':100,
            'CD':400,
            'D':500,
            'CM':900,
            'M':1000,
                    }

        output = 0
        i=0
        while i < len(s):

            if(i+1<len(s) and interger_roman[s[i]] < interger_roman[s[i+1]]):
                output = output + interger_roman[s[i+1]] - interger_roman[s[i]]
                i +=2
                continue
            output = output + interger_roman[s[i]]
        return output
si = Solution()
print(si.romanToInt("XL"))