# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return -1
        start=1
        end=n
        while start+1<end:
            mid=start+(end-start)//2
            if isBadVersion(mid):
                end=mid
            else:
                start=mid+1
        if isBadVersion(start):
            return start
        elif isBadVersion(end):
            return end
        else:
            return -1
