class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums) # suppose k value is greater than len(nums)
        l,r = 0,len(nums)-1
        while l<r: # loop continues untill all the elements are reversed
            nums[l],nums[r] = nums[r],nums[l]
            l,r = l+1,r-1
        l,r = 0,k-1 # 1st part -- changing the left and right values and reversing
        while l<r:
            nums[l],nums[r] = nums[r],nums[l]
            l,r = l+1,r-1
        l,r = k,len(nums)-1 # 2nd part 
        while l<r:
            nums[l],nums[r] = nums[r],nums[l]
            l,r = l+1,r-1
        # for i in range(k):

        #     element = nums.pop()
        #     nums.insert(0,element)

        # return nums

        