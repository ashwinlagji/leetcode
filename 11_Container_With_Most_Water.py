# Unoptimized
# Brute force approach
# Time Limit Exceeded

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area=0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                max_area = max((min(height[i], height[j]) * (j-i)),max_area)
        return max_area