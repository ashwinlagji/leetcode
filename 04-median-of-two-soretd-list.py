# Solution 1 
# Invalid
# uses inbuild sort function
# time complexity != log(n+m)

# Runtime: 240 ms, faster than 4.17% of Python online submissions forMedian of Two Sorted Arrays.

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
       
        nums3 = nums1 + nums2
       
        nums3.sort()
        print(nums3)
        if(len(nums3)%2 ==0 ):
            return (nums3[len(nums3)//2]+nums3[(len(nums3)//2)-1])/2.0
        else:
            return nums3[len(nums3)//2]