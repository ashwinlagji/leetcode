# Optimized
# Runtime: 68 ms, faster than 13.70% of Python online submissions for Container With Most Water.

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area=0
        left = 0
        right = len(height)-1
        
        while(left < right):
            
            max_area = max(max_area , min(height[left],height[right]) * (right - left))
            
            if(height[left]<height[right]):
                left +=1
            else:
                right -=1
        return max_area


# Runtime: 36 ms, faster than 94.79% of Python online submissions for Container With Most Water.
# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         left = 0
#         right = len(height) - 1
#         max_area = min(height[left], height[right]) * (right - left)
        
#         max_number = max(height)
        
#         while left < right:
#             if max_number * (right-left) < max_area:
#                 break
            
#             area = min(height[right],height[left]) * (right - left)
#             if area > max_area:
#                 max_area = area
            
#             if (height[right] < height[left]):
#                 right -= 1
#             else:
#                 left += 1
#         return max_area