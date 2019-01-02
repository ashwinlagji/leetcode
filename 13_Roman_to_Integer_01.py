class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols_two = {"CM": 900, "CD":400, "XC":90, "XL":40, "IX": 9, "IV":4}
        symbols = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        ret = 0
        while s != '':
            if s[:2] in symbols_two:
                ret += symbols_two[s[:2]]
                s = s[2:]
            elif s[:1] in symbols:
                ret += symbols[s[:1]]
                s = s[1:]
        return ret
            