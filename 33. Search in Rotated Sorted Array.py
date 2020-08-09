class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums)==0:
            return -1
        start=0
        end=len(nums)-1
        while start+1<end:
            mid=start+(end-start)//2
            if (nums[mid]-nums[-1])*(target-nums[-1])>0:
                if nums[mid]>target:
                    end=mid-1
                elif nums[mid]<target:
                    start=mid+1
                else:
                    return mid
            else:
                if nums[mid]==nums[-1]:
                    end=mid
                if target==nums[-1]:
                    return len(nums)-1
                if nums[mid]>target:
                    start=mid+1
                elif nums[mid]<target:
                    end=mid-1
                else:
                    return mid
        if nums[start]==target:
            return start
        elif nums[end]==target:
            return end
        else:
            return -1
