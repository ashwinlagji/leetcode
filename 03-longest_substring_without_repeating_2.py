# More optimazation
# sliding window :optimized

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        chars_in_window = []
        max_len = i = 0
        j = 0
        while i< len(s) and j < len(s):
            
            if s[j] not in chars_in_window:
                chars_in_window.append(s[j])
                max_len = max(max_len, j+1-i)
                j = j+1
            else:
                chars_in_window.remove(s[i])
                i = i+1
                        
        return max_len