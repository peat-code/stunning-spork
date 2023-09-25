class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # upperbound
        l = 0
        r = len(nums)-1
        pos = -1
        while l<=r:
            mid = l+r
            mid = mid//2
            if nums[mid] == target:
                pos = mid
                l = mid+1
            elif nums[mid] <target:
                l = mid + 1
            else:
                r = mid - 1

        # lowerbound
        l = 0
        r = len(nums)-1
        pos1 = -1
        while l<=r:
            mid = l+r
            mid = mid//2  
            if nums[mid] == target:
                pos1 = mid
                r = mid - 1
            elif nums[mid] <target:
                l = mid + 1
            else:
                r = mid - 1
        print(pos,pos1)
        return [pos1,pos]
