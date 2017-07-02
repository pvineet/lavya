class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negation = 1
        range=2147483648
        if x >= 0:
            y = int(str(x)[::-1])
        else:
            y = int(str(x*-1)[::-1])
            negation = -1
        
        print int(y)*negation
        if(y<range):
            return y*negation
        else:
            return 0
