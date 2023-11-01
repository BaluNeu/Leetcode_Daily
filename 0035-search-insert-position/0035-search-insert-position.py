class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i,j = 0,len(nums)-1
        while i<=j:
                mid = i + (j-i)//2
                if target == nums[mid]:
                    return mid
                elif target>nums[mid]:
                    i=mid+1
                elif target < nums[mid]:
                    j=mid-1
        return i