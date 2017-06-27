class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1+nums2
        nums.sort()
        
        if len(nums)>1:
            if len(nums)%2 != 0:
                return nums[(len(nums))/2]
            else:
                return (float(nums[len(nums)/2])+float(nums[len(nums)/2-1]))/2
        else:
            return nums[0]
