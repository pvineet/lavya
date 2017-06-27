class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        found=0
        if s == s[::-1]:
            return s
        else:
            while length > 0:
                for i in range(0,len(s)-length+1):
                    #uprint s[i:i+length]
                    temp = s[i:i+length]
                    if temp == temp[::-1]:
                        found = 1
                        palin = temp
                if found == 1:
                    break
                else:
                    length = length - 1 
            return palin
        
