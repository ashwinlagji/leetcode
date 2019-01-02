class Solution(object):
    def __init__(self):
        self.value = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        total = 0
        prev_value = 0
        for c in s:
            curr_value = self.value[c]
            if prev_value >= curr_value:
                total += prev_value
            else:
                total -= prev_value
            prev_value = curr_value
        total += prev_value
        
        return total