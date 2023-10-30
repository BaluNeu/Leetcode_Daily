class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def recursive_helper(left,right):
            if left > right:
                return -1
        
            else:
                mid = left + ((right - left)//2)
            
                if nums[mid] == target:
                    return mid
            
                elif nums[mid] > target:
                    return recursive_helper(left, mid - 1)
            
                else:
                    return recursive_helper(mid + 1, right)

        return recursive_helper(0,len(nums)-1)
        