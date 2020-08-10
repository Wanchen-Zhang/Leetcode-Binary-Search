class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if nums is None or len(nums)==0:
            return -1
        if len(nums)==1:
            return 0
        if len(nums)==2:
            if nums[0]>nums[1]:
                return 0
            else:
                return 1
        start,end= 0,len(nums)-1
        while start+1<end:
            mid=start+(end-start)//2
            if nums[mid]>nums[mid-1] and nums[mid]<nums[mid+1]:
                start=mid+1
            elif nums[mid]<nums[mid-1] and nums[mid]>nums[mid+1]:
                end=mid
            elif nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            else:
                end=mid
        if nums[start]>nums[end]:
            return start
        else:
            return end
        
