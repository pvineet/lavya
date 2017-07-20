class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {}
        even_cnt = 0
        odd_cnt = 0
        for i in s:
            if i in d:
                d[i] +=1
            else:
                d[i] = 1
        
        #print d.values()
        if len(d.keys()) == 1:
            return True
        
        for val in d.values():
            if val % 2 == 0:
               even_cnt += 1
            else:
                odd_cnt += 1
                
        if odd_cnt > 1:
            return False
        else:
            return True
