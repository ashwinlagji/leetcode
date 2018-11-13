# unoptimized answer
# Runtime: 956 ms, faster than 8.28% of Python3 online submissions for Longest Substring Without Repeating Characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        substrings = [""]
        max_len = 0
        for i in range(len(s)):
            word = ""
            for j in range(i,len(s)):
                if s[j] in word:
                    if word not in substrings:
                        substrings.append(word)
                    break
                else:                    
                    word +=s[j]
            if word not in substrings:
                substrings.append(word)
        
        return len(max(substrings, key=lambda x: len(x)))
                