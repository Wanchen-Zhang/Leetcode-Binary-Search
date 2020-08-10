class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums is None or len(nums)==0:
            return -1
        start,end=0,len(nums)-1
        while start+1<end:
            mid=start+(end-start)//2
            if nums[mid]>nums[-1]:
                start=mid+1
            else:
                end=mid
        if nums[start]<nums[end]:
            return nums[start]
        else:
            return nums[end]
