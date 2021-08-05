class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        while res*res<=x:
            res=res+1
        return res-1
