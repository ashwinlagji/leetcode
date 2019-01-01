# unoptimized
# Runtime: 108 ms, faster than 29.57% of Python online submissions for Integer to Roman.

class Solution(object):
    roman_dict = {1 : 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'} 
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        t = num
        div = 1000
        sol = ""

        while t>0:
            d = t / div
            if d == 0:
                div = div/10
                continue
            
            if d<=3:
                sol = sol + self.roman_dict[div]*d
            elif d==4:
                sol = sol + self.roman_dict[div] + self.roman_dict[div*5]
            elif d<=8:
                sol = sol + self.roman_dict[div*5] + self.roman_dict[div]*(d-5)
            else:
                sol = sol + self.roman_dict[div] + self.roman_dict[div*10]
            
            t = t%div
            div = div/10
        
        return sol