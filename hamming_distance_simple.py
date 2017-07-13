class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        return bin(x^y).count("1")
            
    def hammingDistanceBrute(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        distance = 0
        
        while True:
            if x%2 != y%2:
                distance += 1
            x = x/2
            y = y/2
            if x == 0 and y == 0:
                return distance
        
