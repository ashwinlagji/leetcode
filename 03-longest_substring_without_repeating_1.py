# More optimazation
# sliding window more optimized
# Runtime: 104 ms, faster than 62.31% of Python3 online submissions for Longest Substring Without Repeating Characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        chars_in_window = ""
        max_len = i = 0
        j = 0
        while i< len(s) and j < len(s):
            
            if s[j] not in chars_in_window:
                chars_in_window +=s[j]
                max_len = max(max_len, len(chars_in_window))
                j = j+1
            else:
                char_index = chars_in_window.index(s[j])
                chars_in_window = chars_in_window.replace(chars_in_window[0:char_index+1], '')
                
                chars_in_window += s[j]
                j = j+1
                i = i+char_index 
        return max_len