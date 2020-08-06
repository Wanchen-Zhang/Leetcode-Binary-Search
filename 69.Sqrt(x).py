class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        if x==1:
            return 1
        start=0
        end=x
        while start+1<end:
            mid=start+(end-start)//2
            if mid**2<x:
                if (mid+1)**2>x:
                    return mid
                elif (mid+1)**2==x:
                    return mid+1
                else:
                    start=mid+1
            elif mid**2>x:
                end=mid-1
            else:
                return mid
        if start**2<x and (start+1)**2>x:
            return start
        elif start**2<x and (start+1)**2==x:
            return start+1
        elif end**2<x and (end+1)**2>x:
            return end
        elif end**2<x and (end+1)**2==x:
            return end+1
        else:
            return -1

