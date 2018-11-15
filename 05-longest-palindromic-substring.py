# solution 1 
# unoptimized

# Runtime: 976 ms, faster than 78.83% of Python3 online submissions for Longest Palindromic Substring.


class Solution:
    
    maxlen = 0
    index = 0
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        for i in range(len(s)):
            self.findPalindrome(s,i,i)
            self.findPalindrome(s,i,i+1)
        return s[self.index: self.index + self.maxlen]
        
    def findPalindrome(self, s, i, j):
        while(i>=0 and j<len(s) and s[i]==s[j]):
            i -=1
            j +=1
        if(self.maxlen<=j - i - 1):
            self.maxlen = j - i - 1
            self.index = i+1
        