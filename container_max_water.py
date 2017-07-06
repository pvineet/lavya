class Solution(object):
    #Container with max water
    #Problem No - 11
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area=0
        n = len(height)
        l = 0
        r = n-1
        
        while l < r:
            area = min(height[l], height[r])* abs(r-l)
            if max_area < area:
                max_area = area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
