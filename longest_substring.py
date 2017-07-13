class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        length = len(set(s))
        sol = {}
        while length > 0:
            for i in range(0, len(s)):
                if len(set(s[i:i+length])) == length:
                    if sol.has_key(s[i:i+length]):
                        sol[s[i:i+length]] += 1
                    else:
                        sol[s[i:i+length]] = 1
                        break
            if len(sol) == 0:
                length = length - 1
            else:
                break
        if len(sol) != 0:       
            return len(sol.keys()[0])
        else:
            return 0
                
